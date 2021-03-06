---
author: Aaron Decker
comments: false
date: 2016-09-09 00:12:31+00:00
layout: post
link: http://ard.ninja/blog/version-control-git-new-developers/
slug: version-control-git-new-developers
title: Version Control and Git For New Developers
wordpress_id: 462
description: Why version control and especially git is important for new developers to learn.
---

![git](/images/blog/git.png)

I'm teaching a Java 101 class as an Adjunct at Cincinnati State every Wednesday night this semester and I decided I would post the class demos I use up on GitHub each week. When I asked the class if they knew what Github was only a few hands went up. When I asked the class if they knew what version control was, basically the same few hands went up. Based on that, I felt compelled to write up this intro.

Arguably one of the most important tools you will use as a developer is your version control system. Version control is so important it probably falls behind only the programming language, editor, and OS you are using.

If you are a new developer just learning how to program you are probably still transferring your class assignment files around on flash drives or some file sharing system. **Version control solves this problem and so much more**. Version control can serve as a way to store code, preserve history, and even act as a backup system for your programs. Most people also integrate their version control into their build and deployment system in an automated way so that they can use version control to deploy new versions of their code to production.

### What else?

Version lets you collaborate with other developers. _Git_, which is probably the most popular version control system used today, is used widely in the industry and makes working with others on the same codebase fantastically easy. I won't go into the gritty details here, but imagine that you and another developer are working on the same code base, apart, and then after a few days you need to merge your changes back together combine your project once again. Git gives you great workflows to help accomplish this feat, mostly automatically too.

_Github_ is an online git hosting platform. They make it super easy to share Git repositories and collaborate with others. They have workflows that are designed to make it painless. In fact, the steps are so simple I can outline them here:

  1. Find a project you want to work on
  2. Fork the project (this creates a copy for you)
  3. Modify your copy of the project
  4. Submit a "pull request", which lets the original owner review your changes and merge them into the original project.
  5. Pull back the merged version from the original owner and repeat!


If you are new developer it is hard to understate how important it is to learn a version control system. Version control (and likely Git), is something **you will use every single day at work**. So it makes sense to become proficient at this before you even start working. I would strongly advise every new developer to create a Github account and play around with learning how git works, and maybe even collaborate with somebody on a project to get a feel for how pull requests work.

Lastly, let me just mention that git can be hard! You don't have to use it from the command line, but many people (myself included) do so exclusively. Don't worry though, there are tons of GUI based git tools you can use if you want.

I'll leave everyone with this great tutorial from Github:

https://try.github.io/levels/1/challenges/1
