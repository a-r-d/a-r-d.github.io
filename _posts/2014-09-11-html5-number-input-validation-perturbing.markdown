---
author: Aaron Decker
comments: false
date: 2014-09-11 03:55:02+00:00
layout: post
link: http://ard.ninja/blog/html5-number-input-validation-perturbing/
slug: html5-number-input-validation-perturbing
title: HTML5 Number Input validation is perturbing
wordpress_id: 311
---

I am talking about this for reference:

{% highlight html %}

<input type='number' id='ourtest' />

{% endhighlight %}

Did you know according to the HTML5 spec the Number Input validation will cause the value to be read as an empty string if anything but a number is input? So lets suggest a scenario where this sucks: what if I want to allow an empty input OR allow a valid number? Now I can't do that because if an invalid number is entered and you do something like $('#ourtest').val() it will return and empty string ('').

One work around is to set the input to be require and default the value to zero. This will cause anything that is not a number to be read as invalid. However this doesn't truly accomplish our goal of allowing valid input or no input, now does it?

Example:

{% highlight html %}

<input type='number' id='ourtest' value='0' required/>

{% endhighlight %}

Fortunately there is also a 'validity' attribute on browsers that support the more advanced HTML5 inputs. You can do something like the following to check validity:

{% highlight javascript %}

function checkNumber(){
	var val = $("#ourtest").val();
	var elem = $("#ourtest");
	if(elem && elem[0] && elem[0].validity){
		// valid
		if(val != '' && elem[0].validity.valid && elem[0].validity.badInput == false) {
			return true;
		// invalid
		} else if(elem[0].validity.valid == false && elem[0].validity.badInput == true){
			return false;
		// empty
		} else {
			return true;
		}
	} else {
                // invalid or validity not supported
		return true;
	}
}

{% endhighlight %}
