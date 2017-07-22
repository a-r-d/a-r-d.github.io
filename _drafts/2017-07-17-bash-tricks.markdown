---
author: Aaron Decker
comments: true
date: 2017-07-20
layout: post
slug: bash-tricks
title: Bash Tricks
description: Some Bash Tricks I never knew about
---

## Various ways you can do evals

Use backticks inline.
```
$ echo "hello "`python -c 'print "world "*10'`
```

Output:
```
hello world world world world world world world world world world
```
