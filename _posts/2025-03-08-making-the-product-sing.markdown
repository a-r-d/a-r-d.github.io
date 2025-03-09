---
author: Aaron Decker
comments: true
date: 2025-03-08
layout: post
slug: 2025-03-08-making-the-product-sing
title: Making the product sing
description: your b2b saas needs to sing to users like never before. But also it's easier than ever before.
---

![SMR](/images/blog/ai_convo_leadtruffle.PNG){: .center-image }

I'm building a new product now and I'm focusing on customer experience like I've never been able to do before.

I watch in Posthog every day to see frustration clicks.

I listen to what customers say: mention once it's on my radar. Two customers mention it and it's got my attention. Three customers and it's in the app that day.

I have my entire product's feature set written out in English with a mapping of every page and link and I iterate over it with o1 and r1.

Bryan and I watch almost every conversation that comes in [LeadTruffle](https://leadtruffle.com) and we probably will continue to do so until there is so much volume we can't anymore.

## Just do the extra effort.

Claude 3.5 10/22/2024 release was a game changer for me. I was never a great frontend developer. At Bounty for the last three years I had engineers doing that for me.

Now I have Claude doing it for me.

I go through the app as a user every single week and just do all the really annoying painstaking stuff to make things "just work" for users.

Or rather, Claude is helping me do that and I don't care if it's 1000 lines of code get that interaction **perfect** in the UI. Claude is happy to do it.

## Ai coding sucks.

No it doesn't, you suck.

You suck because your code is complex and has too many abstraction layers. You did some cargo cult event based monads or something.

Your code is a reflection of your weak clarity of though in the design process.

You might not be weak on logic but you were weak on the implications of the style you used.

If you can't see sharp edges in your minds eye and lay them out for another entity to understand how do you expect to employ anyone to help (AI or human)?

Pretend there is a gun to your head. Make it work. It's your problem if you can't use a powerful new tool.

## How are you making this work?

I have simple clean design database to frontend.

```
DB table schema -> db access layer -> tRPC procedure -> Client side feature -> page -> components.
```

I can take any vertical slice and throw the entire thing into context.

I write features one vertical slice at a time.

## It doesn't help with maintenance on complex systems.

Right, that's true. Why is your system so complex?

Ok too bad it's already complex... so at least the AI can help you do research on solutioning or vendors or technology constraints.

LLM's can help with everything: we deal in abstractions using text. LLM's are the golden hammer.

## Employing engineers in this new paradigm.

Ideally I would like to never be forced to hire another technical employee. Every employee is a communications channel that comes with it's own problems. The goal is to have as few of them as possible, and every additional employee reduces coherence and weakens the centralized vision. It's an interfacing issue between my brain, my vision, the customers and the product as it is.

At some point (fingers crossed) yes we will have so much business we will get overwhelmed. But is there a better way to deal with this?

My preference would be for the AI agents to get much better and my job becomes 100% planning, design, and code review. Eventually my entire job should be tuning the context that goes into the agents and distilling the output of activity in the application and conversations from customers.

I will continue to have so much more context than any employee or AI agent will ever have. Or perhaps, different and insightful context that only a human can have. As long as my customers are humans my job should be to take human intuition and feedback and put them into the context of my AI agents.

Is that what building looks like in the future?
