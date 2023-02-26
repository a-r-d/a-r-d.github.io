---
author: Aaron Decker
comments: true
date: 2023-02-10
layout: post
slug: 2023-02-26-uuids-over-autoincrementing-ids-are-so-much-better-its-not-even-close
title: UUIDs are so much better than autoincrementing ids and it's not even close
description: A year and a half ago we started building a startup and I chose to use UUIDs as primary keys and it turned out to be such a good choice.
---

Back in Nov 2021 when I started building [Bounty's backend architecture](https://www.bounty.co/) I chose to use UUIDs for all of our primary keys in our postgres database that powers the majority of the current application and the benefits have been remarkable.

As recently as earlier in 2021 I had worked on large system dealing with money using integer Ids in a RDMS and it made me very nervous seeing all the things that could go wrong...

## First the drawbacks.

For many years people have been taught in school to use `BigInt` autoincrementing Ids as primary keys. The first time I remember seeing something different was when I used Mongo for the first time back in 2013. They had this object id system that was a random string. I believe this was done so you could shard the database easily across writer instances. It's hard to have multiple writers into a collection if they all have to coordinate who gets to increment the integer for the primary key next so that was the solution.

But there are drawbacks. A UUID looks like this: `7c82deda-9461-4128-af05-d8c3acd16c47`

Obviously, it's larger than an integer, and takes some CPU time to generate it randomly. You also will need to have a `createAt` timestamp field and index that field if you want to order by time, whereas with an autoincrementing integer primary key you are going be able to simply sort on the primary key.

But aside from the efficiency of an integer PK, thats where the benefits end imo.

## Security benefit - no id incrementing attacks

One of the most common vulnerabilities in web applications is object id incrementing. Officially, this vulnerability [is called "IDOR" - Insecure Direct Object Reference](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html). 

Example: You look at your browser and you see it say `/customer/12345/invoice/23399430` what happens if you modify this and hit `/customer/12345/invoice/23399431`? Well, if your developer didn't think about this you can see somebody's elses invoice.

How about doing that with a UUID? You can't. The keyspace is too large to guess which others might exist.

This vulnerability should never exist in the first place if you have careful programmers (should always check permissions on object access in APIs), but trust me it's all over the place in modern web apps.

## Operations benefit - no copy paste mistakes

We happen to have a lot of customers that do weird things and file support tickets. We deal with payments so there is always some edge case.

Let me tell you - your ops team is copy pasting ids and doing stuff in your internal dashboards you made them (we have like 40 retool apps 😂) and they are going to make mistakes because they are human.

It's totally possible to make a mistake if they mix up `userId` value 10001 with `orderId` value 10001. But if it's UUIDs? No they can't no overlap.

You need 2.71 quintillion UUID generations for `1ccccb76-206f-4abc-930b-09ee47764874` to collide with that same UUID in another table.

## Code benefits - developer mistakes are mitigated

Just as your ops team WILL mix up copy pasting ids from one table to another, you developers will do the same thing at some point.

You will have a function with a signature like: `freezeBankAccount(bankAccountId: number)`

In a million lines of code somebody is going to pass in a `userId` to that instead of a `bankAccountId` to that and it's going to freeze a random user's bank account because the primary key ID keyspace of type integer is going to almost certainly overlap between the tables named `User` and `BankAccount`.

You make this mistake with a UUID? What happens?

Nothing, you will see an error in the logs after deployment of "BankAccount not found" in the function named `freezeBankAccount` because there is no overlap.

You identify the cause (the wrong ID was passed to the function call) and put in a fix.

What if you had used integer ids and made this mistake? 2 weeks later you will find out because there have been a 100 support requests of people unable to access their bank accounts and now you have a massive operations cleanup issue on your hands. Worst case in a large organization it runs silently in production for months before you get wind of it and now there is a ton of fallout to deal with.
