---
author: Aaron Decker
comments: true
date: 2021-06-14
layout: post
slug: 2021-06-14-doing-a-good-code-review-should-be-simple
title: Doing A Good Code Review Should Be Simple
description: I talk about why it's a good idea to use a checklist with code reviews and how subjective PR sizes when it comes to code.
---

How do you do a good review? Personally, I think you should follow a checklist. All too often I see that code reviews will miss important bits and instead folks will spend a lot of time enforcing style or arguing about architecture but instead will miss the bigger picture.

Often times there is no standard and different team members will look for totally different things in a code review. Why do we do software development this way?

## The checklist

1. Does the code meet the minimum requirements of the task assigned?
2. Does the code work and not have any major issues? Are obvious error scenarios handled?
3. Does the code violate the overall architecture of the code base? Could anything be done better to fit within the existing architecture? (This is where you enforce patterns)
4. Are there tests over the code?
5. Is there documentation around any new behaviors or features added? If it was a bug, was this fix documented somewhere and efforts made to prevent the same bug in the future?
6. Is the code formatted & styled in the manner expected?

## How big should a PR be?

How big should a chuck of code being reviewed be? Good question. There is a lot of contention here because it makes sense to review a full working feature, and it also makes sense to never review more than some arbitrary small amount of code at a time (e.g 100 lines of code).

All in all, small PRs are better and easier to review. The downside is that you can miss the bigger picture and it is easier to have major architectural issues sneak in with small PRs.

Bigger PRs are difficult because they are hard to review all at once. It's easy to miss things. They take a long time for the reviewer to prepare and the reviewe to respond to feedback and make fixes against.

A difficulty arises in a change that needs to be done across many layers of architecture of an application. Will your app compile or will it blow up with errors if you limit the PR size to only 100 lines of code? Are you going to have to work in feature gates if you do small PRs? Will you have a lots of dead code temporarily existing until the full feature is done?

These are all good questions and a lot depends on the maturity of the application (and it's requirements), the quality of the code base, the trust between members of the team, and how well the application is architected.

## Team code base review

Have you ever sat down with your engineering team and just reviewed the existing code base on your project as it stands? I've done this before but not often. Why don't we do this very regularly as an industry?

Wouldn't it be good to periodically take stock of the entire code base in your application as it stands and do this? How often should you do it? Once a month? What architectural issues would you uncover and what changes would you end up making?

Ideally you want to catch issues in the PR phase, but how do you do that if you never get the opportunity to holistically review the larger picture? 

## Summary

With PR sizes: what I'm saying is that all of this is very **subjective**. But as a team & and an organization you should think about these decisions and make guidelines.

Regardless of the rules around making a PR though, I think you should always use a checklist as a code reviewer. It removes a lot of the arbitrary feelings involved in an inconsistent review process.
