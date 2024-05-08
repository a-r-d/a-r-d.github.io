---
author: Aaron Decker
comments: true
date: 2024-05-08
layout: post
slug: 2024-05-08-how-I-built-bountys-internal-customer-service-tools-using-retool
title: How I built Bounty's internal customer service tools using Retool
---

As CTO of Bounty, I frequently encountered a high volume of customer service issues. Managing these, especially in a small startup environment, was challenging.

#### What is Bounty?

Bounty is an app that detects, tracks, and rewards users for their branded content on platforms like TikTok and Instagram.

The main Challenges:

- Operating as a marketplace introduces multiple complexities.
- Handling pass-through payments adds another layer of complexity.

Examples of specific issues:

- Failure to detect videos.
- Inaccuracies in tracking views.
- Dissatisfaction from brands or creators.
- Issues with payments / fraud / or some other exception.

The sheer volume of issues necessitated a full-time customer service role, alongside a manual review process for each video, adding to our overhead.

## Using Retool

I am primarily a backend developer, but even if I weren't and wanted to make React apps all day, it would be an extreme waste of time to write production-level code that only one internal employee will ever use.

However, there must be some way for a non-technical employee to do things that directly manipulate data in the system. So unless they know SQL and can write Node.js scripts, you are going to have to come up with some solution.

The solution, of course, is code-light tools like Retool.

## Why I Like Retool

Retool is nice because:

1. It supports multiple environments (I use PRODUCTION + STAGING in my systems).
2. It lets you connect to PostgreSQL, call APIs, make cron jobs (workflows), and modules (reusable components).
3. It has its own internal PostgreSQL database you can use for stuff like notes on customers.
4. It has a ton of features and all the components are basically drag + drop.
5. You can make custom React components if you need (which we did for embedding TikTok videos in the review tool).

## Background - How Does Customer Support Work?

If you think about the tasks a customer support employee needs to do, it's basically this:

1. Talk to a customer and understand their complaint.
2. Research the issue & determine an appropriate solution.
3. Solve it themselves OR kick it up to a higher level - and ultimately to engineering.

In large companies, you usually have levels of support. The lowest level can do minor things but they usually need to kick it up higher for complex tasks. The highest level at a software company would be kicking it up to the engineering team.

The engineering team built the app so they should be able to solve any problem. They understand how the data is stored and can manipulate it directly (hopefully correctly & safely).

But kicking a small problem up to engineering is like paying $200/hr to a person picking fruit.

Even worse, if you take time away from the core engineering team, the new features on your product will not get built.

## Why would you need to build internal tools?

It should be obvious at this point, but the goal is to automate common support tasks so that employees with little to no knowledge or training can handle them (i.e., the cheapest hourly staff).

Traditionally, the way to mitigate this is to build tools for customer support (CS) staff.

Many times, this is custom work.

It's your custom database. It's your custom user schema. It's your custom billing system. You literally can't make an off-the-shelf tool to handle this stuff.

What that means is you had an internal tools team building stuff for CS staff.

So you need another X number of engineers on staff to simply more efficiently solve problems to keep the other engineers from being bombarded with support issues.

Retool mitigates this - A LOT.

## The apps I have built with Retool

With Retool, you drag & drop UI components onto a page and then wire up events to SQL queries or API requests to internal API endpoints you have built.

I'll list out some of the stuff I made for my CS staff:

### User lookup tool

You have to look up a user's account to diagnose an issue right?

![user lookup tool](/images/blog/retool/user-details-viewer-app.png){: .center-image }

### Store details tool

You have to look up various information about a given store customer to diagnose issues as well.

![user lookup tool](/images/blog/retool/store-dashboard-lookup.png){: .center-image }

### Video review tool

We have a person review & rate every video our customers pay for:

![user lookup tool](/images/blog/retool/screenshot-approval-tool-app.png){: .center-image }

### Manually associating an instagram reel

Sometimes for whatever reason our system doesn't pick up a submitted video. The CS team needs a way to manually resolve this.

![manually assoc instagram video](/images/blog/retool/manually-assoc-instagram.png){: .center-image }

## Building Retool apps

So you might be thinking "great, all I need is Retool." That's definitely not true.

You still need help from a developer. In fact, you probably need your best backend developer who understands the systems you created very well to make Retool apps.

But, they can crank these things out QUICK!

They can probably make:

- 1 low complexity app per hour
- 2-3 medium complexity apps per day
- 1 high complexity app per day

Just by themselves. So in one week of focus, you can probably have 80% of your customer service issues that get kicked up to engineering teams handled.

And why a backend developer? Because often you will need to write a custom API and expose it from your infrastructure. There are just things you can't do by only talking directly to the database.

Anytime you need to call a specific code library, interface with e.g., some random AWS service like a Queue, you are probably going to need to write a custom backend endpoint. But the good news is your backend can do that easily with no help from anyone.

## Partner with an Expert (me)

I understand the intricacies of integrating tools like Retool to optimize business operations. If you're looking to enhance your customer service capabilities without overburdening your engineering team, I’m here to help. Leverage my expertise to set up and streamline your systems efficiently.

Let's work together! [You can book a 15 minute meeting on my calendar here](https://tidycal.com/aaron.b.decker/15-minute-retool-consulting-discovery-call)
