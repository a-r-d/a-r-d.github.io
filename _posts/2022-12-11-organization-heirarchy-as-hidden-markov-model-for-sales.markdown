---
author: Aaron Decker
comments: true
date: 2022-12-11
layout: post
slug: 2022-12-11-organization-hierarchy-as-hidden-markov-model-for-sales
title: Organizational Hierarchy as a Hidden Markov Model - For Sales
description: Thinking about modeling large organizations through the lens of a hidden markov model to get to a "yes" in the sales process.
---

## Hidden Markov Model

I'd be surprised if you are technologist and you haven't encountered Markov Chains in general and Hidden Markov Models in specific. But, to give an intro quoting form wikipedia:

> A hidden Markov model (HMM) is a statistical Markov model in which the system being modeled is assumed to be a Markov process — call it X — with unobservable ("hidden") states. As part of the definition, HMM requires that there be an observable process Y whose outcomes are "influenced" by the outcomes of X in a known way. Since X cannot be observed directly, the goal is to learn about X by observing Y

So to summarize: you have system with a process you don't understand fully but you can model it as going through some unknown states in order to get to some observable end state.

## Sales as an HMM

I was thinking recently how this is a good way to think about the sales process with a large organization. Say there is a large company (take Coca Cola as an example) and you want to sell them your software for $50,000 a month.

You know the possible end states - **Yes**, **No**, etc. But you don't initially know the decision makers who are capable of agreeing to this $10,000 a month sale, and you dont know all the boxes you need to check the the different departments to get to "Yes" state.

Job titles vary greatly from one org to the next - e.g. maybe the CEO is actually very checked out of the day to day operations and talking to them won't get you anywhere for your sale. Perhaps the VP of marketing is the person to talk to!

I think the sales process is about collecting refinements to this model to update who does what until you know enough states to get to a "Yes".

In addition to finding the initial point of contact, you have other hidden states you need to navigate. Do you need to make various compliance people happy if they are capable of blocking the deal? Do you need to make some IT VP satisfied in order to onboard the client? These are all things you need to learn to complete sale.

Eventually you get a clear model of how the organization works and you can do up-sells and keep the relationship going (as an aside - wouldn't it be interesting to have a marketplace of power structures or organizations where you can purchase this insider knowledge?).

An additional interesting aspect of working with an organization is that they are made of humans with shifting power structures that change often drastically over time.

Did your main champion and point of contact get fired or quit? Well, that could be a huge problem and this customer might churn without a contact like this.

You have to keep this model up to date!
