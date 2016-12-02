---
author: a-r-d
comments: false
date: 2016-09-24 19:14:15+00:00
layout: post
link: http://ard.ninja/blog/how-npm-scripts-really-work/
slug: how-npm-scripts-really-work
title: How npm scripts really work
wordpress_id: 476
tags:
- javascript
- node
- npm
---

When using npm you probably know all about npm install and some of the flags for global installation and saving dependencies. If you publish packages you probably know a few more. But I want to talk a little bit about the mechanics of how npm scripts really work and why you should use them. Using npm scripts ultimately makes it so that you can stop installing npm packages globally.


### npm scripts

You probably have used "npm test" and "npm start" before. However, it makes a lot of sense just to use npm scripts for parts of your build tooling. The advantage npm scripts is that rather than installing things like testing frameworks and transpilers globally, you can install them local to the project and then npm will look in "./node_modules/.bin" when it runs scripts.

Any package that has a binary defined in its packages.json will have a symlink places under "node_modules/.bin", and when you run an npm script this location will effectively be on the $PATH. That means you don't need to globally install utilities, you just have project dependencies and let npm resolve everything for you.

e.g. define a script like this (where babel is defined as a dependency):

```
"scripts": {
    "compile": "babel -d lib/ src/",
}
```

Then, run it like this:

```
npm run compile
```

This is exactly the same as running:

```
./node_modules/.bin/babel -d lib/ src/
```


### Stop installing npm packages globally

The point of this article is that you don't need to install tooling globally, you can just use npm scripts and npm will resolve the binary location at a project level for you. It is much more consistent to do compile and test steps this way, especially if you have many different javascript projects going on simultaneously. On top of that, if you don't install npm packages globally, you don't have to worry about permissions issues (which many people neglect to fix, opening their systems to vulnerabilities from post-install scripts.
