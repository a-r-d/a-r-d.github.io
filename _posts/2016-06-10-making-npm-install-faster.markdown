---
author:Aaron Decker
comments: false
date: 2016-06-10 16:23:13+00:00
layout: post
link: http://ard.ninja/blog/making-npm-install-faster/
slug: making-npm-install-faster
title: Making npm install faster
wordpress_id: 402
categories:
- javascript
- npm
---

I have a react project at work that has a large dependency tree (due to webpack, babel and various testing frameworks) and it ends up taking a very long time to run npm install on our build server. It is now time to fix this! It turns out there are a lot of ways to make npm install faster and there is a lot of low-hanging fruit to be plucked first. I know this is a problem lots of people have when their projects start to become large and there are surprisingly a lot of ways to tackle this issue. Here are a few  things you can look at to speed things up.



### Progess Bar:

```
npm set progress=false
```

Set progress=false is a quick way to speed up npm install, it simply turns off the progress bar output which, in the case of my build, it caused a cached npm install to go from 72 seconds to 32 seconds.



### Production Mode:

```
NODE_ENV=production npm install
```

Setting production mode in the NODE_ENV variable will cause only "dependencies" to install, skipping "devDependencies". This can be problematic for build processes because you probably do want to run tests and the test framework packages are likely in your dev dependencies. However there may be other dependencies in there that you only use for debugging or testing that is not part of your build process. If you get clever can you pare down the total number of your dependencies.



### Running A Cache Server:

```
# i used this project: https://github.com/runk/npm-proxy-cache
#on your proxy server
npm install npm-proxy-cache -g
npm-proxy-cache --expired --ttl=86400 --host=0.0.0.0

#on your build script:
npm --proxy http://proxy-server-hostname:8080 --https-proxy http://proxy-server-hostname:8080 --strict-ssl false install
```

You can run a dedicated cache server for npm with a long TTL in the cache. Probably, you are not going to be changing package versions very often (of already installed packaged). This means that you should be able to run a dedicated cache server that all of your build agents can use as a cache and never have those network requests leave your data center except when the cache is busted.



### The black box of npm (after the deps are downloaded)

Recently after I made all of the above changes to my build I noticed I still had some issues when it comes to install time and it was not network related. I did the following experiment:

  1. ran a cache server on a VM
  2. on the cache server VM I ran "watch -n 2 netstat -atp", this showed me the network connections open
  3. ran npm on my PC against my cache server
  4. while running npm I had htop open to watch CPU usage on my npm process.


Here were the results: first npm went out to download each package from my cache server and I saw tons of TCP connections open in parallel to this machine, so npm did a great job here of parallelizing all of the network activity. However, after a few seconds everything was downloaded (I know because all of the connections closed and I stopped seeing activity in the logs of my cache server) but still npm was running and using lots of CPU time. In fact, npm ran for about 10 or 15 more seconds (of a 30 second total install) with CPU spiked and no output.

Obviously, when the total number of dependencies is increased there is a lot more network activity to do, but apparently there is also a lot more processing to do with all of the dependencies after the fact. What is going on here? Hopefully in my next post I will have some answers. But until then, unfortunately, the only thing I can conclude is that the surest way to make things faster is to reduce the total number of your dependencies!
