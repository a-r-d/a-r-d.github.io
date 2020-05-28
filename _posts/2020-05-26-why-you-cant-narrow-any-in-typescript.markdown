---
author: Aaron Decker
comments: true
date: 2020-05-26
layout: post
slug: 2020-05-26-why-you-cant-narrow-any-in-typescript
title: Why You Can't Narrow "any" in TypeScript
description: I recently discovered you cannot narrow "any" type in typescript with a typeguard.
---

![Typescript logo](/images/typescript-logo.png){: .center-image }

I ran into an issue using TypeScript recently. In TypeScript you can do typechecks ([using typeguards](https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-guards-and-differentiating-types)) in your code to effectively "narrow" a type.

I'll explain - if you have a union type that could be one of several types you may want to "narrow" this in your code so that you know what type your object is after a certain point in the code.

What was surprising to me is that you cannot "narrow" a type of `any`!

I found a discussion [here on stack overflow](https://stackoverflow.com/questions/36940687/why-does-typescript-not-narrow-the-any-type-in-this-type-guard), and [a comment from a TypeScript maintainer here](https://github.com/Microsoft/TypeScript/issues/1938#issuecomment-72994925) but apparently this is a purposeful design decision.

I'll show you the code I was trying to do this with - [here is a code sandbox](https://codesandbox.io/s/inspiring-microservice-dszyi?file=/src/index.ts),
in case you are interested in seeing this in action.
