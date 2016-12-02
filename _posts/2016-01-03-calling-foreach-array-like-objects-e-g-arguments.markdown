---
author: a-r-d
comments: false
date: 2016-01-03 19:01:59+00:00
layout: post
link: http://ard.ninja/blog/calling-foreach-array-like-objects-e-g-arguments/
slug: calling-foreach-array-like-objects-e-g-arguments
title: Calling "forEach" on array-like objects (e.g. arguments).
wordpress_id: 344
categories:
- javascript
---

I am readying through "Secrets of A JavaScript Ninja" right now and learning tons of helpful little tricks. The coolest thing I saw in there recently was the section on array-like objects, e.g. "arguments". So it is pretty simple - all of the array methods exist on Array.prototype and you can use the function method "call" and "apply" on these. Surprisingly this works great, so now you can do forEach, slice, ect on your arguments objects even though it is not an array.

{% highlight javascript %}
(() => {
	function callMe() {
		// slice the "Arguments as an array"
		return Array.prototype.slice.call(arguments, 1);
	}

	function callMeIter() {
		console.log('Is forEach on args: ', arguments.forEach);

		Array.prototype.forEach.call(arguments, function(iter){
			console.log('Iter on args: ', iter);
		});
	}

	console.log('multiArgs sliced test: ', callMe(1,2,3,4));
	console.log('Foreach on arguments: ');
	callMeIter(1,2,3,4);
})();
{% endhighlight %}


ALSO FYI arrow syntax is now in Chrome so you can make your iife like this:

{% highlight javascript %}

// Cool 
(() => {
    // write your code in the iife here
})();

// lame!
(function() {
    // write your code in the iife here
})();


{% endhighlight %}

That looks way cooler right? I think so...
