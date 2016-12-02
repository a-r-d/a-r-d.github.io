---
author: Aaron Decker
comments: false
date: 2016-08-16 01:12:55+00:00
layout: post
link: http://ard.ninja/blog/top-5-es2015-features-use-today/
slug: top-5-es2015-features-use-today
title: 5 ES2015 Features You Should Use Today
wordpress_id: 425
---

![es2015](/images/blog/es6.jpg)

ES2015 (formerly known as ES6 and short for ECMAScript 2015) is one of the latest specifications for JavaScript, the components of which are almost entirely implemented in the latest versions of Node 6, Chrome, Firefox, and more.



**1. Block scope with "let" and "const"**

In JavaScript, a common source of errors in the code of new users has always been due to confusion about scope. Before _let_ and _const,_ when you declared a variable it would be hoisted to the top of the containing function declaration and exist throughout. Unlike in Java or C, you didn’t get a new scope inside of an _if_ block or a _for_ loop.

Not anymore. When you declare variables with _let_ or _const_ they only exist in the block that you declared them. Ultimately, there is no reason to ever use _var_ anymore, _let_ and _const_ should replace _var_ completely.

[![let-scope](http://ard.ninja/blog/wp-content/uploads/2016/08/let-scope-300x102.png)](http://ard.ninja/blog/wp-content/uploads/2016/08/let-scope.png)

**2. Arrow functions**

Arrow functions at first may appear just to be a new function declaration syntax, but they actually behave differently from traditional functions. In normal functions when you declare a function the value of "this" can be a little bit tricky because each function will create its own context.  Arrow functions don’t create their own context, so when you reference “this”, you will _ALWAYS_ be referencing the parent function. Check out this example, which shows "this" clearly belonging the parent function.

[
](http://ard.ninja/blog/wp-content/uploads/2016/08/let-scope.png)[![horse-arrow-function](http://ard.ninja/blog/wp-content/uploads/2016/08/horse-arrow-function-300x94.png)](http://ard.ninja/blog/wp-content/uploads/2016/08/horse-arrow-function.png)

**3. Promises**

Promises have been around for a while but only as features of libraries. Whether you used jQuery, Angular $q, bluebird, or something else, everyone had their own implementations of promises. Now promises are baked into the language and can be used without external dependencies. So whether you like to use Promises or Callbacks for your async control flow, now you don’t need to weigh bringing in another dependency to make the decision.



**4. Template Strings**

Template strings (also known as _template literals_) allow you to perform string interpolation and define multiline strings as well as "tagging" (a way to modify the output of a template string with a function). To create a template string all you have to do is use backticks (` `) instead of quote marks, and you will be able to do string interpolation rather than concatenation.

[![template-string](http://ard.ninja/blog/wp-content/uploads/2016/08/template-string-300x44.png)](http://ard.ninja/blog/wp-content/uploads/2016/08/template-string.png)

**5. New Object Syntax**

I'm going to cheat on #5 here and throw in a bunch of new syntax related to manipulating objects because it is all so cool. This includes Destructuring, Object property shorthands, the spread operator, and the new class declaration syntax. Destructuring, in particular, can be very nice and you will quickly find yourself thinking to apply it in all sorts of convenient ways. Check out the example below:
[![destructuring](http://ard.ninja/blog/wp-content/uploads/2016/08/destructuring-300x156.png)](http://ard.ninja/blog/wp-content/uploads/2016/08/destructuring.png)

Next, I want to show a quick example of object property shorthand and use of the spread operator:

[![shorthand and spread](http://ard.ninja/blog/wp-content/uploads/2016/08/shorthand-and-spread-300x88.png)](http://ard.ninja/blog/wp-content/uploads/2016/08/shorthand-and-spread.png)



There are too many new features in ES2015 to detail in one short blog post, but [here are some free egghead.io videos ](https://egghead.io/courses/learn-es6-ecmascript-2015)that can take this introduction a bit further.
