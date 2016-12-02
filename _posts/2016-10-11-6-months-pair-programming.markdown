---
author:Aaron Decker
comments: false
date: 2016-10-11 16:27:44+00:00
layout: post
link: http://ard.ninja/blog/6-months-pair-programming/
slug: 6-months-pair-programming
title: 6 months of pair programming
wordpress_id: 488
---

![pair programming](/images/blog/pairing.jpg)

I have been pair programming at my job for 6 months straight now. Nearly every day, all day, pair programming.

I knew what I was getting into: I was told before I joined that I would be pair programming. I went into it with an open mind and wanted to give the practice a totally fair shot. So how did it go after six months?


### The upsides

I have never been on a team that is so close and comfortable with each other before, and I think that is in large part due to pair programming. We actually work very quickly and get lots of work done for the most part (unless we are externally impeded, then pair programming doesn't help much). I also think that a lot of the productivity is due to the constant communication from pair programming.  

Interestingly, pair programming is pretty good for solving problems. When two people are working on a hard problem and neither knows how to do it both can break away and research. When you both come back, compare notes, and try things, you can often come to solutions faster than I think most people would alone. Importantly though, you have to both push each other to actively try solutions rather than dither and debate about approaches because endless debates can happen as well.

Another serious upside is that for the most part when the entire team is pair programming, the entire team gets to learn much more of the code base. Sections of code don't get isolated to the point where only one team member can maintain them if there are always two sets of eyes on everything.

Usually, mistakes are caught quickly. When two people are running the logic in their heads as it is being written the outcome is that a lot fewer bugs are actually committed. And, on this particular project, I can honestly say this is just about the cleanest code I have ever worked on at a jobsite.


###The downsides

While pair programming is pretty great for solving problems (debugging, refactoring, and ops tasks generally) I don't actually think pair programming is good for writing code. Firstly, when you code and pair program it is very hard to ["flow"](https://en.wikipedia.org/wiki/Flow_(psychology) or get "in the zone". In fact, I miss getting into the flow state so dearly that I often go home and write code or write blog posts with much more enthusiasm than I used to because it allows me to feel that mindset.

There is something about getting in the zone that is just so intellectually satisfying that I miss it so much that I actively seek it out when I am not getting it at work. I'm pretty sure I like programming so much mostly because of _flow_. So that is a serious downside that feels pretty insurmountable, to me at least.

Secondly, it is actually pretty slow for writing code. If one person starts to get going they have to stop and explain to the other what they are doing as they do it. Otherwise, your counterpart will just start checking email or updating documentation and that is not really the point of pair programming.


###Agreeing on Tools

Another serious downside of pair programming is that everyone has to agree on tools. This is a huge deal to some and irrelevant to others. When I came onto the team I inflicted oh-my-zsh on everyone but when I wanted to use vim or vim-mode for our various editors I got some (obviously understandable) resistance. That slows me down because I'm used to those shortcuts. Alternatively, if you are used to using tmux (a terminal multiplexer) then suddenly your pair would have to agree to use tmux (and learn the commands for tmux) if you want to work together.

Even simple things like git workflows can be really annoying when pair programming. For a couple of years now my git workflow has been: stage using tig (a command line git tool), then commit from the command line. I am used to doing it that way. However, if your pair wants to use git GUI tools in IntelliJ or some other third party tool, they may balk when you whip out tig.


###How does it compare it to other activities?

Programming is a creative endeavor in many ways. True, many programmers are mathy and often deeply analytical and traditionally we don't think of people like that as creative, but I disagree with that notion. Can you image "pair graphic design"? Or perhaps "pair creative writing"? That actually sounds like a recipe for complete disaster. However something like "pair bench chemistry" sounds fairly reasonable, every step will be double checked. Working in pairs obviously is also optimal for things like piloting aircraft. I'm not sure where programming falls in this continuum of activities, but for me, I have been pleasantly surprised that pair programming has worked as well as it has.

I think the key point here is that every software project is different. Some software projects are a bit like writing a novel. Other software projects are more like constructing a Boeing 747. So it isn't really fair to make a simple analogy when it comes to software engineering.


### Would I do pair programming in the future?

This is certainly a personal bias, but ultimately *I believe that the individual is most productive when he/she has the most control over their own work and environment and I would avoid pair programming in the future*. However, I think that whether or not pair programming is effective depends on the size of your project / organization. I believe pair programming is very effective when used on large projects with many organization integration points.

I think the optimal environment for solo programming is this: small project, with few integration points, few team members, and clearly defined purpose. I think this environment would allow for the most creativity and productivity as a solo programmer, and this is the kind of project that I have personally enjoyed the most in the past. Remember, many of the best or most interesting software projects have been written primarily by very small teams or as solo efforts (unix, C, linux (initially), BitTorrent, Bitcoin).

So overall, it has been an interesting experience, but I think that given the choice I would not do pair programming again mainly due to the loss of "flow" and the restrictions on tools I want to use. But, if you want to work on a huge complex system, it does make a lot of sense to pair.


**Note**: I edited this post because I didn't mean to actually come down so hard and negatively on pair programming. I actually do think it makes sense to use it, especially for larger systems and organizations. But, personally, I don't like the restrictions it places over the ways I would like to do my own work and the frequent experiments I like to do with my own tooling and work environment.
