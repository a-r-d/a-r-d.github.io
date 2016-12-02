---
author: Aaron Decker
comments: false
date: 2015-12-30 00:53:18+00:00
layout: post
link: http://ard.ninja/blog/fun-semicolons-javascript/
slug: fun-semicolons-javascript
title: Fun with semicolons in JavaScript
wordpress_id: 333
categories:
- javascript
---

So people always say that in JavaScript semicolons are optional but you had better use them anyway. The often cited case is the return statement.

{% highlight javascript %}
function foo() {
  console.log('executing foo!')

  // even though there is no semicolon, we just return immediately
  return
  {
    data: 'data'
  }
}

console.log(foo());
{% endhighlight %}

[Jsbin link](https://jsbin.com/qitewovuho/edit?js,console).

In JavaScript you can make new code block "{ }" anywhere you want and it is perfectly valid, it will just execute when the code path hits it. Another funny thing is that for some reason an if without a body and semicolon following it is valid (e.g. "if(true);" will not throw any error). So if you bring these two things together you can get a weird thing like this:

{% highlight javascript %}
function foo() {
  console.log('running foo...')

  if(false);
  {
    console.log('code block in if statement executed')
  }
}

foo()
{% endhighlight %}

[jsbin link](https://jsbin.com/kodejibowe/edit?js,console).
