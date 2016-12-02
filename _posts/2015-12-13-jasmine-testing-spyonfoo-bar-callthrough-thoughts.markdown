---
author: Aaron Decker
comments: false
date: 2015-12-13 06:44:59+00:00
layout: post
link: http://ard.ninja/blog/jasmine-testing-spyonfoo-bar-callthrough-thoughts/
slug: jasmine-testing-spyonfoo-bar-callthrough-thoughts
title: Jasmine - spyOn().and.callThrough() argument mutability
wordpress_id: 327
categories:
- javascript
---

Earlier this week I was using the [Jasmine testing framework](https://github.com/jasmine/jasmine) on some Angular code and wanted to use the spyOn feature to check that some of my service methods were getting called properly. "spyOn", if you are not familiar is similar to a mock system in something like Jmock or Mockito (in the Java world). The spyOn method lets you observe a method on a given object where by default it will simply replace the method with a call counter that also traps a references to the calling arguments. If you call the spied on method you can later do something like:

{% highlight javascript %}
var foo = {
  bar: function(arg) {
    // do something with your arguments
  }
}

spyOn(foo, 'bar');

// call the bar function on foo in some testing context.
// then, check it was called
expect(foo.bar).toHaveBeenCalledWith(123);

{% endhighlight %}


This will assert the method was called with the argument "123" (as a number of course). So be default the spy doesn't actually call the method, if you want it to call the actual method and just count the call as it does it you will do something like this:

{% highlight javascript %}
spyOn(foo, 'bar').and.callThrough()
{% endhighlight %}

This will cause the actual method to be called. This is very straightforward when you have arguments that are passed by value such as a number. However when you pass in an object (which is mutable) then you your expectation will be checking whatever the object referenced that may have mutated from what it was like when it was passed into the method you are spying on. So the problem is if I call foo.bar() with some object and I want to check that foo.bar() was called with the object I expect, what I really want in most cases I would argue is a deep copy of that object (i.e. a snapshot at that point in time)! I don't want the mutated object after foo.bar() does some work on it.

So I want something like: "spyOn().and.callThrough({cloneArgs: true})" which tells "callThrough" to clone those arguments when it records the call. I'm going to try to dig into the jasmine-core and see how easy it is to do something like this, although I don't know how open the guys over at Pivotal labs are to contributions to Jasmine.

UPDATE:

[I submitted a pull request to Jasmine and it was accepted](https://github.com/jasmine/jasmine/pull/1000
) which does a shallow clone. It is based off of [this issue](https://github.com/jasmine/jasmine/issues/872#issuecomment-164467203)
