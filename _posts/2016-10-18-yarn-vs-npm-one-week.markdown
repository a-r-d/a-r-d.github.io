---
author:Aaron Decker
comments: false
date: 2016-10-18 12:27:17+00:00
layout: post
link: http://ard.ninja/blog/yarn-vs-npm-one-week/
slug: yarn-vs-npm-one-week
title: Yarn vs npm one week in
wordpress_id: 506
---

![yarn package manager](/images/blog/yarn.jpg)

If you hadn't heard, last week Facebook open sourced a new javascript package manager called [yarn](https://yarnpkg.com/). It is awesome.

Yarn install is **significantly** faster than 'npm install' and resolves dependencies deterministically, regardless of declared order (unlike npm). Yarn creates a lockfile when you run the install and once this is done once, it does not need to recreate the lockfile until you change the dependencies. Due to this precomputation of dependency resolutions, the install command run very fast. Oh, by the way, there is no "install" command required, you just call "yarn" and it runs install by default.

Yarn also supports private registries, which I can tell you does work since we are using a private registry at my client site. You just have to create a ".yarnrc" file and put a line in like:

```
registry "http://your-registry.your-company.com"
```


Okay so all of this stuff is great - quicker installs, deterministic resolution of dependencies, and a kind of built in shrinkwrap system. The big issue I have discovered so far is this: yarn does not deduplicate dependencies as well as npm does. In fact, in one project I'm working on which gets built with webpack when I used yarn to install my dependencies I got 6 copies of React in my vendor file output. When I was using npm I got way fewer duplicate packages pulled into my vendor file (only one copy of React for sure). Although [it seems like they are working on it judging by this issue](https://github.com/yarnpkg/yarn/issues/579).

However, even though yarn does not de-dupe very well yet, you can still do ["yarn install --flat"](https://yarnpkg.com/en/docs/cli/install) and manually choose your duplicate package resolutions. This will create a "resolutions" entry in your package.json which forces yarn to pick specific versions. This is actually a great work around, and will make your final build nice and small if you are outputting a bundle to be consumed by a browser.
