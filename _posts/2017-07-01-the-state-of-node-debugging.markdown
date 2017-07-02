---
author: Aaron Decker
comments: true
date: 2017-04-16
layout: post
slug: the-state-of-node-debugging
title: The State of Node Debugging
description: Using chrome dev tools for node debugging
---

## Node debugging on Node 7 and 8

Rather than using ```node-inspector``` on Node 7 and 8 you can now use chrome dev tools debugger with a special flag (```--inspect```), then navigating to __"about://inspect"__ in chrome. It looks something like this:

```
# this opens the process up for debugging
node --inspect server.js

# this breaks execution immediately
node --inspect-brk server.js
```

Unfortunately, this feature does not work in the current LTS version of Node.js (version 6.11.0). Paul Irish did a [great presentation at Google IO 2017](https://developers.google.com/web/updates/2017/05/devtools-release-notes) describing the new features in Dev tools that were added to support Node.js debugging.

## You can quit using node-inspector

Ultimately you can now stop using ```node-inspector```, if you are able to upgrade to the latest version of Node. The Node Inspector is a heavy dependency to keep in your dependency tree and you should get rid of it if you can, additionally the featureset that the ```node-inspector``` project can offer has already fallen behind what chrome dev tools provides.
