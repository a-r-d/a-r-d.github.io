---
author: a-r-d
comments: false
date: 2016-01-09 20:01:57+00:00
layout: post
link: http://ard.ninja/blog/javascript-constants-using-object-defineproperty/
slug: javascript-constants-using-object-defineproperty
title: JavaScript constants using Object.defineProperty
wordpress_id: 354
categories:
- javascript
---

I work on a pretty large Angular project everyday at work that has a very polluted global namespace due to what I think are meant to be "constants". Actually, the are just variables defined on the window object in all caps that contain a lot of strings and some numbers meant to be used as codes and other things like that. They could be overwritten at anytime so this is just a disaster waiting to happen. 

ES6 has "const" which creates a read only reference value, but that will just result in a whole lot of globally defined constants (that actually are constants now). We still need to fix the global namespace pollution! Ideally we would put all of these on one object and make an interface to all of these constants. But aren't JavaScript object mutable? Well actually, we can fix this...

Object.defineProperty() is a very interesting ES5 method that allows you to add properties to an object than can be writable, enumerable, and configurable. By default when you use defineProperty it makes properties that are not writable (writable and configurable is set to false) which to us means read only and is exactly what we want. 

Here is an example of this in action. This object has a method for adding properties that can be come constants, not on the global namespace, and we can then freeze this container when we are done if we like.

[javascript]

const ConstContainer = {
    add: (k,v) => {
        if(ConstContainer.hasOwnProperty(k)) return false;
        Object.defineProperty(ConstContainer, k, {value: v});
    },
    // format as array of arrays: [['key', 'value'], ['key', 'value']]
    addMany: (arr) => {
        arr.forEach((iter) => {
            ConstContainer.add(iter[0], iter[1]);
        });
    }
};

ConstContainer.add('KEY1', 'VAL1');
ConstContainer.add('KEY1', 'dupe val');
console.log(ConstContainer);

ConstContainer.addMany([['KEY2', 'VAL2'], ['KEY3', 3]]);
console.log(ConstContainer);
console.log(ConstContainer.KEY1);

// when done, you can freeze to counter all further mutability:
Object.freeze(ConstContainer);

[/javascript]
