---
author: Aaron Decker
comments: false
date: 2016-08-16 01:12:55+00:00
layout: post
link: http://ard.ninja/blog/top-5-es2015-features-use-today/
slug: top-5-es2015-features-use-today
title: 5 ES2015 Features You Should Use Today
wordpress_id: 425
description: top 5 es2015 features I think you will get the most benefit from.
---

![es2015](/images/blog/es6.jpg)

ES2015 (formerly known as ES6 and short for ECMAScript 2015) is one of the latest specifications for JavaScript, the components of which are almost entirely implemented in the latest versions of Node 6, Chrome, Firefox, and more.


## 1. Block scope with "let" and "const"

In JavaScript, a common source of errors in the code of new users has always been due to confusion about scope. Before _let_ and _const,_ when you declared a variable it would be hoisted to the top of the containing function declaration and exist throughout. Unlike in Java or C, you didn’t get a new scope inside of an _if_ block or a _for_ loop.

Not anymore. When you declare variables with _let_ or _const_ they only exist in the block that you declared them. Ultimately, there is no reason to ever use _var_ anymore, _let_ and _const_ should replace _var_ completely.

{% highlight javascript %}
// you use them just like "var"
let x = "Hello";
const y = "world!";

// let and const are block scoped
if(true) {
  let someVar = "some value";
}

// var would have been hoisted, but what happens when we do this?
console.log(someVar);


// Remember that problem of what happens when pass a var iterator by ref in a loop?
// use var in a loop, see what happens
const refsVar = [];
for(var i = 0; i < 3; i++) {
  refsVar.push(function() {
    return i;
  });
}

// what do you get when you map over these functions?
console.log(refsVar.map((func) => {
  return func();
}));


// Using let fixes that issue.
// use let in a loop, see what happens compared to above
const refsLet = [];
for(let j = 0; j < 3; j++) {
  refsLet.push(function() {
    return j;
  });
}

// what do you get when you map over these functions?
console.log(refsLet.map((func) => {
  return func();
}));

{% endhighlight %}

## 2. Arrow functions

Arrow functions at first may appear just to be a new function declaration syntax, but they actually behave differently from traditional functions. In normal functions when you declare a function the value of "this" can be a little bit tricky because each function will create its own context.  Arrow functions don’t create their own context, so when you reference “this”, you will _ALWAYS_ be referencing the parent function. Check out this example, which shows "this" clearly belonging the parent function.

{% highlight javascript %}
function Animal(params) {
  this.type = params.type;
  this.voice = params.voice;

  setTimeout(function() {
    console.log(`This classic function: the ${this.type} says ${this.voice}`);
  }, 5)

  setTimeout(() => {
    console.log(`This arrow function: the ${this.type} says ${this.voice}`);
  }, 10)

}

// What happens when you instantiate this ?
// What happens when the arrow function runs ?
const duck = new Animal({
  type: 'duck',
  voice: 'quack'
});

{% endhighlight %}

## 3. Promises

Promises have been around for a while but only as features of libraries. Whether you used jQuery, Angular $q, bluebird, or something else, everyone had their own implementations of promises. Now promises are baked into the language and can be used without external dependencies. So whether you like to use Promises or Callbacks for your async control flow, now you don’t need to weigh bringing in another dependency to make the decision.

{% highlight javascript %}
const p1 = new Promise(
  function(resolve, reject) {
    setTimeout(function() {
      resolve('promise is done!')
    }, 100);
  }
);

// Promise { <pending> }

p1.then(function(data) {
  console.log(data);
}).catch(function(err) {
  console.error(err);
});

// the promise will resolve after 100 milliseconds
//  -> "promise is done!""
{% endhighlight %}


## 4. Template Strings

Template strings (also known as _template literals_) allow you to perform string interpolation and define multiline strings as well as "tagging" (a way to modify the output of a template string with a function). To create a template string all you have to do is use backticks (` `) instead of quote marks, and you will be able to do string interpolation rather than concatenation.


{% highlight javascript %}
const [x, y, z] = ['var 1', 'var 2', 'var 3'];

const interpolation = `
    1. ${x}
    2. ${y}
    3. ${z}
`;

console.log(interpolation);
/**
  Looks like this, preserves formatting:

    1. var 1
    2. var 2
    3. var 3

**/
{% endhighlight %}


## 5. New Object Syntax

I'm going to cheat on #5 here and throw in a bunch of new syntax related to manipulating objects because it is all so cool. This includes Destructuring, Object property shorthands, the spread operator, and the new class declaration syntax. Destructuring, in particular, can be very nice and you will quickly find yourself thinking to apply it in all sorts of convenient ways. Check out the example below:

{% highlight javascript %}
let arr = [1, 2, 3];

let [a, b, c] = arr;

// a=1, b=2, c=3
{% endhighlight %}

Next, I want to show a quick example of object property shorthand and use of the spread operator:

{% highlight javascript %}
// spread operator into an array
const arr = [1,2,3];
const arr2 = [...arr, 4, 5];

// now arr2 contains [1,2,3,4,5]
{% endhighlight %}

{% highlight javascript %}
// we need to create an object to demonstrate object property shorthand
const person = {
  name: 'Elon Musk',
  jobTitle: 'CEO',
  favoriteThing: 'Rockets'
}

// destructure out these keys
let { jobTitle, favoriteThing } = person;

// Jeff bezos also happens to own a rocket company, so let's reuse those.
const anotherPerson = {
  name: 'Jeff Bezos',
  jobTitle,                 // <--- the key is the variable name, no need to write twice!
  favoriteThing
}

console.log(anotherPerson);
// { name: 'Jeff Bezos', jobTitle: 'CEO', favoriteThing: 'Rockets' }
{% endhighlight %}

There are too many new features in ES2015 to detail in one short blog post, but [here are some free egghead.io videos ](https://egghead.io/courses/learn-es6-ecmascript-2015)that can take this introduction a bit further.
