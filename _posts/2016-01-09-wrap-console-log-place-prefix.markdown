---
author: Aaron Decker
comments: false
date: 2016-01-09 22:15:26+00:00
layout: post
link: http://ard.ninja/blog/wrap-console-log-place-prefix/
slug: wrap-console-log-place-prefix
title: How to wrap console.log in-place with a prefix
wordpress_id: 358
description: Wrapping console.log so that you can add timestamps, script names, whatever else to node logs.
categories:
- javascript
---

There is a npm module called [console-stamp](https://www.npmjs.com/package/console-stamp) that is pretty nice and simple - whenever you print using the global 'console' methods it prefixes everything with a timestamp in whatever format you specify. Well, I was curious how to do this and it is something I would describe as easy but not simple unless you are very familiar with "Function.prototype.apply". The method I'm going to show you is actually adapted from [Secrets of the JavaScript Ninja](http://www.amazon.com/gp/product/193398869X/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=193398869X&linkCode=as2&tag=ultralightgea-20&linkId=2LEOR3OFOCROOM4F)![](http://ir-na.amazon-adsystem.com/e/ir?t=ultralightgea-20&l=as2&o=1&a=193398869X). It is a simple two step process:

  1. create a "wrap" method that will call a given method with a "wrapper" method you define.
  2. Run the "wrap" method on the function you want to wrap and define the wrapper you will apply around it.


[(JSBin example of the following code)](https://jsbin.com/dacunogedo/1/edit?js,console)
{% highlight javascript %}
// you will call like: wrap(console, 'info', fn);
function wrap(object, method, wrapper) {
  // get reference to target method off the function (original method)
  var fn = object[method];
  // replace it with this new method:
  return object[method] = function() {
    // apply the wrapper
    // "[fn.bind(this)]" will actually just be the original method that will
    // be an argument in your wrapper
    return wrapper.apply(this, [fn.bind(this)].concat(
        // "arguments" will be args you call the wrapped method with.
        Array.prototype.slice.call(arguments))
      );
    };
}

wrap(console, 'info', function(original) {
    // The first thing in arguments will be the original method,
    // so let get rid of it in our copy
    var args = Array.prototype.slice.call(arguments, 1);

    // Apply the original method with the prefix as the first arg and the
    // info message as the following args
    original.apply(this, ['test info prefix: '].concat(args));
});

// This will print --> "test info prefix: test info message"
console.info('test info message');
{% endhighlight %}
