---
author: Aaron Decker
comments: false
date: 2014-09-11 04:07:47+00:00
layout: post
link: http://ard.ninja/blog/android-4-1-4-2-gpu-rendering-dom-repainting/
slug: android-4-1-4-2-gpu-rendering-dom-repainting
title: Android 4.1 and 4.2, GPU rendering and DOM not repainting
description: tl;dr - CSS "translate3d" is buggy on certain android versions
wordpress_id: 314
---

Did you know that using some CSS attributes on native android browsers will cause the browser to kick into a special GPU rendering mode? Did you know that this is buggy on android 4.1 and 4.2 and will cause certain areas of the DOM to not be repainted when they change? Well it appears to be true and is very very tricky to diagnose if you have a site laden with CSS.

The specific CSS attribute I encountered this with was the following:

{% highlight css %}
-webkit-transform: translate3d(0,0,0);
{% endhighlight %}

This attribute is commonly used as a performance hack from what I have seen. I have also read it can be used to trick the DOM into being repainted... however in this case on android 4.1 and 4.2 it was doing just the opposite. On Android 4.4.4 this appears to be fixed! Android 2.x also seems immune to this bug!

**Just a warning there are more '-webkit-transform' attributes that kick off GPU rendering than the one I mentioned!**
