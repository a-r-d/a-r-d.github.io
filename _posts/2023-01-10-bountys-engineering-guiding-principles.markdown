---
author: Aaron Decker
comments: true
date: 2023-01-10
layout: post
slug: 2023-01-10-bountys-engineering-guiding-principles
title: Bounty's Engineering Org Guiding Principles
description: Some guidelines I wrote down to help introduce new engineers to how I want the Bounty team to operate and ship code for the business.
---

**Preface:**

The principles below are both a goal state of what I believe makes a strong engineering mindset and a response to my personal bad experiences of weak management and leadership at previous employers.

A lot of this is about optimizing good results in terms of product for the business. The outcome we are looking for is "get shit done" but that’s more nuanced than just "go fast". 

There is a balance here: we are not making medical devices or rockets, but we are dealing with money & lots of traffic on Shopify stores so stuff had better be right, or at least recoverable if it goes wrong. 

1. **We write code to serve the business. The business exists to serve customers.** **Code is a tool to solve this problem.**
    1. Solve problems for the business. If the business dies, we die. 
    2. Product, Ops and Sales specifically are our direct customers.
    3. Communicate with the business when changes are made.
    4. We don’t write code for it’s own sake. We don’t write code to satisfy our intellectual curiosity, fun as that may be. 
        1. If you want to scratch that itch that’s great, do this by making RFCs & other design documents or building prototypes to prove out concepts to the rest of the team before they are incorporated into the primary systems. 
2. **Prefer simplicity over complexity**
    1. Example: did you end up with something it’s impossible to get visibility into when it goes wrong? Simplify it!
3. **Write code that your co-workers can understand, maintain, and debug.**
    1. Example 1: Ask does the code you are writing match the code around it? E.g. are you pulling in a pattern into a code base where this is out of place? Can everyone you work with read and understand the code you are writing? 
    2. Example 2: did you do something that has some hidden or out of the ordinary behavior? Make it as obvious as possible what is going on and write documentation as way to help deal with disbursing this technical knowledge.
    3. Anyone on the team could end up maintaining your code or fixing a bug in it. Think about this before you commit. 
4. **Untested code should be assumed to be broken**
    1. A production feature is not done until it is tested. Preferably it has automated tests on it and it was QAd in both a development environment and a production environment. 
    2. A production feature is not done until you have observed (and can continue to observe) users using it in production. 
5. **Build fault tolerant systems**
    1. What can go wrong will go wrong, and probably in a confusing way that will be hard to debug. Build systems in a way that they can fail gracefully. 
    2. Things will go wrong at the worst possible time, possibly in combination with something else. 
        1. Distributed systems are complex systems and they tend to fail in complex, cascading ways.
6. **Be paranoid**
    1. Anything connected to the internet will attempted to be exploited sooner or later.
    2. Do anything with money and people will try to scam / steal.
7. **Prioritize visibility and metrics**. 
    1. Ship code with good visibility, when you ship new code verify it works and have ways to easily check that it’s functioning as expected.
    2. Have alerts if things go wrong
    3. Log generously so you can proactively solve issues when they crop up
    4. design system in such a way that you can debug and recover from issues and have some kind of understanding of what went wrong.
8. **Ship features regularly**
    1. Ship features that work
        1. If your code doesn’t work, it should fail gracefully
            1. If it can’t fail gracefully, it had better alert the engineering team
9. **Prefer shipping incrementally and often to shipping big features all at once less often.**
    1. We want to reduce the length of the feedback cycle, recognize issues immediately and reduce the risk associated with big sweeping changes all at once
    2. Migrate incrementally, think about how you will interrupt existing customers, affect their expectations, and our promises to them.
    3. If we have to break a contract or expectation, it needs to be discussed with product and support teams to understand and anticipate blowback.


### Some other thoughts

There are some other things I didn't incorporate into this around support and day to day work on pull requests. 

I have written before about [pull requests and code reviews](https://www.ard.ninja/blog/2021-06-14-doing-a-good-code-review-should-be-simple/) in that they should not be a place to get into stylistic debates and they should be reviewed for correctness and reviewed quickly to unblock other team members. 

I will post another thing about managing support engineering and how we do our support rotations and responding that kind of workload. 
