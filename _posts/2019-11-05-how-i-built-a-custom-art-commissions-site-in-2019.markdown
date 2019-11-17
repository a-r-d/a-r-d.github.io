---
author: Aaron Decker
comments: true
date: 2019-11-05
layout: post
slug: how-i-built-a-custom-art-commissions-site-in-2019
title: How I Built A Custom Art Commissions Site In 2019
description: I talk about my experience of building a custom art commissions site using MERN stack in 2019.
---

![A Banner for the site I ended up building](/images/blog/starshine-banner-5.jpg){: .center-image }
_A banner for the site I ended up building_{: .center-image }

Late last year my girlfriend Meridith's side hustle was blowing up and she was spending a ton of time on administrative tasks, which of course with me being a software engineer made me want to help her automate everything.

What was this side hustle you ask? __Pet Portraits__. She's a classically trained artist (she went to [RISD](https://en.wikipedia.org/wiki/Rhode_Island_School_of_Design)) working on her own art career but to pay the bills she ended up doing a ton of pet portrait commissions and it kept spreading via word of mouth. 

She was spending too much time emailing back and forth with people to get photos and contact info and accept payments. Yeah! I can solve this!


## The business process

So let's think about the current ordering process. It goes something like this:

```
> Customer: Hey I heard you do pet portraits, can you paint my dog? 
> Meridith: Sure! Do you have a good photo?
> Customer: How about this photo?
> ... *Meridith explains the kind of photo she needs*
> Customer: How much does it cost for size "x"?
> ... *Meridith gives pricing info for various sizes*
> Customer: Can you mail it to this address?
> ... *collects mailing address*
> Customer: OK, how do I pay you?
> ... *more back and forth*
```

Okay, you get the idea. It's like 20 emails by the end of it. It would be much easier to make a site that tells you all of the important information about the photo and the pricing and collects all of the required information (and photos).

So I made an order form with these steps:

1. Upload Photos
2. Pick order type (shows size & number of subjects options)
3. Shipping destination - collect address
4. Billing info - collect email / phone / let them enter coupons
5. Order confirm + pay (shows subtotal then trigger stripe checkout)

## So I decide to built a custom site

I decided to build something custom instead of using Shopify or Squarespace. I figured "hey I can throw this together in a weekend!". I knew I needed to make something pretty complex where the customer needed to upload images and I figured I might as well build this instead of using some janky plugins. 

Plus, I'm a software engineer, I got this!

## The tech stack I chose.

I like to call myself a "full-stack developer", but I will admit my front-end skills are a little rusty. In fact, this would be great practice! 

I ended up going with MERN stack, and I used [Create React App](https://github.com/facebook/create-react-app) as my foundation. For my component library I chose [Ant Design](https://ant.design/) which I had never used before (and some of the docs are in Mandarin) but I don't mind a challenge. 

I used Stripe for payments, AWS SES for email. Just set it all up on a single server on a cloud provider because there was not going to be a lot of traffic. I just threw this thing up on a linux box behind an nginx server and Lets Encrypt was nice and easy to set up. Anyway, I've done all that stuff a million times that was not the hard part. 


## OK site is done right?

Nope, not yet. Again I am a little rusty at dealing with frontend stuff. There are a ton of things I had to end up dealing with that I didn't even think about. I ran into some issues. 

## Social Sharing 

You may not realize this but there are special meta tags that dictate how a link for a website will show up when you share it on Facebook or Twitter, for example. 

Yeah... So for example, if you don't tell Facebook what title, description and image to show your link previews with it is going to look like junk when you share it.

So you need some stuff on your site like this in the header:
```
<meta property="og:title" content="Starshine Pet Painting"/>
<meta property="og:description" content="Beautiful Hand Painted Art As Unique as your pet."/>
<meta property="og:image" content="https://www.starshinepetpainting.com/images/overlay-logo2-small.jpg"/>
<meta property="og:url" content="https://www.starshinepetpainting.com"/>
```

Which sucks, because obviously the first time she shared this to Facebook it looked like crap. Protip: [Facebook has a tool](https://developers.facebook.com/tools/debug/sharing/) you can use to make sure all this stuff is set up correctly. 

## In-App Browser (for instagram and facebook)

Also, here is a thing you may or may not know: mobile traffic exceeds desktop internet traffic these days.

Yeah, you probably did know that. Ok here is another thing: a lot of mobile web traffic is actually coming from in-app-browsers from the facebook or instagram apps for example.

Did you know that sometimes, depending on the phone OS, these in-app-browsers are really super out of date? Also did you know it is [very difficult](https://stackoverflow.com/questions/27199489/how-to-debug-on-facebook-internal-browser-mobile) to debug this junk? 

Well, I do. Now. 🤦

So what do you do when you photo picker component mysteriously doesn't work on the in-app-browser in facebook in some random Android phones? 

**Put in a polyfill and hope it works** (which it did, thankfully🙏).

## The general front-end woes

Generally speaking, I still had to do all the things that are hard about front-end. That means testing on multiple browsers (including IE 10), and multiple phone OSes. I still had to test on a bunch of different screen sizes so that means testing on everything from 4k down to 320px wide mobile devices. 

Somehow this all seemed more stressful than normal since if it didn't work I would be turning away paying customers, and it would not be some kind of internal business application like I was used to working on. Or better yet, the backend of a server where I don't have to worry about any of this stuff!


## Everything just took longer

I guess I didn't realize the reality of things is now that everything is being shared socially and it is super hard to get traffic from Google. So what we ended up doing was just focusing on how things looked in all the various social media platforms and they all have their special quirks and meta tags and whatever.

Doing the backend even took longer than I thought. The whole goal was to make this quick and easy so I didn't build an auth system since I didn't want people to need to create accounts and all of that, but that meant triggering a emails that had a lot of content in them. Stripe is to easy to use but there still a decent amount of coding involved to handle error scenarios and all of that. 

Ecommerce is a lot more complicated than it first appears. You have to collect a lot of information to successfully fulfill an order and there are lot of things that can go wrong. You have to effectively communicate to the user what you are selling and answer all of their questions or they will just bounce. I'm still [not sure I did that totally effectively in the landing page](https://www.starshinepetpainting.com/), but hey, that is a work in progress!

## Pivoting to $30 Sketches

One weekend in Novemeber we had the opportunity to do an in-person popup show at a local community market where Meridith decided to quick 20 minute sketches for $20. We called them "$20 Dog Doddles", well that was an enormous success, I don't think we had any downtime the whole weekend, and on an hourly basis this was just as profitable as doing more fully rendered paintings.

We had acheived __product market fit__. So we redid the website and started to offer a $30 sketch option (to cover shipping) and the price point just makes the whole thing so attractive to a much wider audience. Here is a screenshot of the landing page for the $30 sketch option:

![the new $30 option banner at the pet painting site](/images/blog/sketches.png){: .center-image }

The other cool thing was since I built the site custom it was pretty trivial to lift any component I needed up one level and refactor the code to handle more order types and prices. In the update to the site I even put in a cool [timelapse background header video](https://www.starshinepetpainting.com) of Meridith drawing a dog. 

## So what did I learn?

Anything you are selling these days needs to be optimized for social sharing. This takes a fair amount of work and experimenting. 

__In-app-browsers are a huge pain__, but facebook and instagram don't want the user to leave the app, so they are here to stay. You just have to deal with it and polyfill if you can.

Ecommerce sites are hard to make and they have a lot edge cases. But it was a good experience and now I have the ability to really customize the order process for this niche of custom commission pet painting.

Finally I think another big lesson is that you need to __try different things until you find something that is really a hit__. The fully rendered portraits starting at $150 a commission (for just a small 5x7) are too expensive for most people, and the more stylized quick $30 sketch option appeals to a much wider audience. So by trying out these different ideas we figured out something that was still economical to produce but had a much wider appeal.
