---
author: Aaron Decker
comments: true
date: 2022-08-14
layout: post
slug: 2022-09-21-building-an-engineering-org-one-year-in
title: Building a (software) engineering organization one year in.
description: Lessons learned, pain points, and my developing management philosophy.
---

## Creating structure

I'll quote something I saw on tech Twitter and I can't find the original source but I'll update this if I do:

> You're not a bored gifted kid you're someone who derives self worth from accomplishing clearly defined tasks under a hierarchical power structure and you're struggling because you've been asked to self direct.

I personally believe, (myself included) a lot of software engineers fit this description as workers in the workforce. In the millennial generation (which I am right in the middle of) there were many overachievers who were great at getting good grades and racking up accomplishments but this came within the structured and clearly defined environment of schooling.

After going through college getting dean's list every quarter (except for that one...) you are spit out into a workforce where much of the day seems like pointless busy work and you look around and wonder why everything is so dysfunctional. There is little direct feedback on your performance except once a year when you get a 2%-4% salary bump. Your output seemingly has no observable or measurable impact.

I have worked for a lot of fortune 500 employers (5 of them) and I will be absolutely clear: first impression, many of them felt like _adult day care_ and there was a lack of meaning tied to the work I was doing on a day to day basis. But what I realized later of course is that I was playing the wrong game: I needed to figure out what the business goals of the organization are (my bosses boss, and etc up the ladder, their pain points) and go about figuring out to have some meaningful impact on them. It's a political game in some ways because you will hear one thing in an all-hands but then you talk to the VP of engineering and realize he/she has completely different set of problems and that's what you should be doing if you want to be noticed (and get promoted, etc).

In fact, it's a surprisingly _self-directed_ game. There is no clear road map and every organization has different problems and key stakeholders.

I think many people hate corporate life so much because it's hard to understand what to do to make an impact. People dream about starting an organic microgreens farm because they think they will be able to see the output of their labor, but what they actually want is to _right now_ move the needle on a business and get a direct reward as a result (and do it on a short timescale) and feel pride.

## Making the same mistakes

I'm head of engineering at [Bounty](https://bounty.co) and I found myself making a lot of the same mistakes. I knew what to do. My co-founders knew what to do. But it actually takes a lot of energy to transmit goals down to who you hire, and the tighter a process you run the easier it actually is to do.

I fell into the mistake of thinking everyone wanted to be completely self directed and figure out what to do. When I look in the mirror, that's not even what I personally like. I like to have **clear tasks** with **clear goals** and **see meaningful outcomes quickly**. It just happens to be a little easier if you are a founder and you are having to make the critical decisions around product and market so you _know_ directly what the pressing issues are you need to resolve.

The KPIs, OKRs, and North Star metrics are easy to make fun of (especially when done poorly) but ultimately they are important ways of clearly communicating down what matters. But it needs to be done and clarified on an individual level as well, and a manager needs to continually tie in directly what each member of the team is working on to these.

## Minimizing arguments and creating clarity

If you tell a direct report that **infrastructure change X** is a priority one day, and then tell them **user feature Y** is a priority the next day you invite argument and push back. This is a huge mistake, and the tone, the priorities and direction needs to be both crystal clear and consistent.

I'm writing this both as an observation of what works and as a goal state (it's incredibly hard to stay consistently on message as a leader but it's hugely undermining to your authority if you do not).

In military circles there is a well known quote from Douglas MacArthur:

> Never give an order that won't be obeyed.

The implications are obvious: if you do this not only have you undermined your authority and legitimacy you also destroy team morale. So before you tell your team to do something you need to think firstly if they can even physically **do** what you are asking, followed by **if** they will do it, and finally how much push back you will get. The right conditions need to be created to before you ask them something hard.

I'm still learning the ins and outs of this.

## Creating consistency

One of my great regrets is that I did not use a very strict framework with the codebase that has a lot of clear documentation (I used Express and laid down very little structure, but I should have used e.g. NestJS or Ruby On Rails or Spring Boot). Right now I'm considering how to transition to something that extremely clearly defined and tighten up the architecture. Why?

Because we keep doing code reviews that bleed into architectural discussions and stylistic discussions. It's my observation that these are poisonous to productivity and getting PRs moving and merged.

I would rather pick up a book and say "we are doing this and you can always consult this book" than have it as something we have continually debate about on an ongoing basis. It's an incredible productivity time suck.

## Velocity and code reviews

Broadly most people would agree a code review should cover at least these things:

1. verification requirements are met (base functionality & UX - does it work & does it work well?)
2. identification of obvious errors & security issues
3. identification of _potential_ errors based on other knowledge of the system
4. consistency with overall code base and architecture and style

But if you don't have #4 nailed down and it turns into a debate, it's just a waste of time until you do nail it down. And again, this undermines authority if there is not a clear direction on what to do.

I have observed across many teams and work environments that although code reviews should be just "about the code" it's very easy to spark personal animosity during these. Brief textual statements of criticism do not carry the soft tone a reviewer would likely have in person and can easily be taken negatively by the author.

I once worked on a team of 8 where **one single person was a hardcore TDD adherent** and the other 7 were not. On many of his code reviews he would remark about how it looked like the "code was not written TDD style" and the tests were not adequate. What was the point of this? It simply made everyone pissed off at each other, held up every review with an argument and the checked-out manager just let this happen over and over again. Unless the direction is set that "yes we are all doing TDD now", this is just destroying morale and productivity.

Code reviews block the merging of code and flow of work. They should be done to ensure code quality but they need to be limited in scope due to how much they impede velocity, so put simply: minimize the stuff that can be argued about by having it decided before hand.

I'm still evolving my thinking on this but I have internal debates all the time about _pair programming_ Vs _independent work + strict code reviews_. You need a second set of eyes on the code to ensure quality but you want it to be as efficient as possible. I'm still of an opinion that pair programming 100% of the time is a gross misuse of resources. But it's certainly not a waste just 20% of the time...

## In summary

As a leader you are responsible for creating the culture and organization in which your teams of engineers will swim every day. It's hard to create structure, expectations, clarity, and consistency. You are by definition bringing order to chaos and chaotic elements will creep in and continually need to be fought back against. You are fighting entropy and it's not easy.

But expecting everyone to completely self-direct (especially in a new organization) is a fools errand. The only time this works is if you have personal relationships which each member and there is an existing loyalty and set of expectations. Building a new hierarchy from scratch is whole lot harder.
