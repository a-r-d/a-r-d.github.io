---
author: Aaron Decker
comments: true
date: 2016-12-17
layout: post
slug: java-vs-dot-net-for-recruiters
title: Java Vs .NET for recruiters
description: Java vs .NET explained to recruiters
---

## What is the upside of understanding these technologies?

Surprisingly often I get recruiters contacting me about .NET jobs. I have history of Java jobs, I have Java on my resume, on my Linkedin profile there are only references to Java and nothing related to .NET at all.

Now, I know some of this is recruiters spamming indiscriminately. I understand that recruiting is a numbers game, and that ultimately this works. Here is what I would like to propose to you: this is probably effective but ultimately could be much more efficient.

What if you could improve your lead response rate by 50% overnight? I think, if you could contact the same amount of leads, but be 50% more accurate you could potentially get 50% more placements.

What I am proposing to you is to actually filter Java jobs to Java developers and .NET to .NET developers. I know, I know, maybe it's a lot of work, or maybe your system cannot even make these distinctions. But it should be able to and I would like to explain to you why there is a difference.


## Operating system differences and web developers

Okay, you may understand that there are different programming languages, and that Java and .NET are different programming languages. Java is a C-Style language owned by Oracle and .NET is a platform owned my Microsoft. Actually, there are a couple of .NET languages: C#, VB, and F# (there are more).

Fundamentally .NET is a Microsoft product: you develop on _Windows_ and you deploy to _Windows servers_. However, Java is meant to be cross platform so Java developers might be using Macs to develop, but in practice 98% of Java developers deploy to some variant of _Linux_. Windows and Linux are totally different operating systems and there is a totally separate set of skills around administering servers running these operating systems.

So, a big difference here is not the languages themselves, but the operating systems that people are running their software on. As a Java developer, I would never be interested in a .NET in large part because my linux experience would go to waste.


## Ecosystem differences

Unless you happen to be a programmer yourself, another thing you may not know is that choice of programming language alone is often superficial, and the true characteristic that sets languages apart is the ecosystem behind them.

Let me give you an example: the Java ecosystem has a popular open source framework called [Spring](http://spring.io/) which is used for web development. It actually takes more effort to learn and use the many parts of Spring than it does to learn Java itself. If you have a job requirement for Java + Spring, if you find a .NET developer your company is likely going to reject them.

On the .NET side for web development there are [ASP.NET MVC](https://www.asp.net/mvc), ADO, LINQ, and many other frameworks that are commonly used and all will be exceedingly foreign to your average Java developer.

Databases _can be_ another big difference. Java is commonly used with Oracle, MySQL, Cassandra, or any number of other data storage systems. .NET shops on the other hand seem to lean understandably toward MsSQL Server.


## Other Java-related languages

There are a few languages that compile to Java bytecode that you should also know about. When I say _"compile to java bytecode"_ I know that is probably confusing, so let me draw an analogy. These languages use Java (the JVM -_Java Virtual Machine_- more precisely) as a foundation they build a structure on top of it. So the plumbing still hooks up to the JVM underneath, but the facade is something else.

The languages are Groovy, Scala, Kotlin and Clojure to name a few. This is actually what .NET is like too: C#.NET and VB.NET build on top of the common .NET runtime. But again, you have the same issues: the language itself is in this case somewhat superficial, the parts where are experience really matters are the ecosystems built up around these two differing technologies. Because underneath of a Groovy app and a Clojure app the plumbing is the same.



<!---

Maybe do a diagram showing the ecosystems. It would be cool to include this as
a sort of infographic.


--->
