---
author: Aaron Decker
comments: false
date: 2014-06-11 03:24:16+00:00
layout: post
link: http://ard.ninja/blog/trollboxarchive-com-technology-overview/
slug: trollboxarchive-com-technology-overview
title: Trollboxarchive.com Technology overview
wordpress_id: 302
categories:
- cryptocurrency
---

![tba logo](/images/blog/tba-1.gif)

## Background

A little over a year ago I created a site called [Trollboxarchive.com](http://trollboxarchive.com) along with the help of my friend John Hoey. The idea was to log the chat records from the chat window on Btc-e and figure out when the "whales" were making big trades. Fontas (an infamous pump and dump trader) quickly became the focus of the site and today still remains the most searched user on the site.

[Trollboxarchive.com](http://trollboxarchive.com) started as a joke and an experiment but quickly became popular in the crypto trading community. I ended up putting more time into trollboxarchive than I ever thought I would because I became curious as to whether you could time the market based on keyword frequency (spoiler: you can't I think). Other people were interested in following the trades of whales much like investors follow Carl Icahn or Warren Buffet.


## The Original Stack


The site was originally some simple PHP scripts that would allow you search against a very simple MySQL schema. I used 2 InnoDB tables to build the entire site. I had 2 python scripts running on 1 minute cron jobs on the server to pull the chat data and quote data. Originally I only had search data but soon started collecting quotes for the currencies so you could see the price + chat history together. The quote tables were also quite simple. Everything was on a single small VPS box hosted with a small start-up hosting company.


## Problems Develop


The original server stack was using plain old Apache2. We started getting 10 thousand page views a day and the database grew to well over a gigabyte very quickly. InnoDB was the right choice because row-level locking and lots of simultaneous reads and writes but it was the wrong choice because no support for fulltext indexing on TEXT columns. It soon became apparent the main feature people wanted was search. The site quickly became unusable.


## Solution: Sphinx search and Memcached


Wherever I could cache I started using Memcached. This enabled me to do some very cool charts and data analysis but didn't solve my search issue. That came in the form of Sphinx search: a very very fast full text search engine capable of connecting directly to MySQL and indexing the data. Sphinx proved to be amazing and great to work with. I highly recommend it. I currently have 2 gigs of messages indexed and the search is always under 50 ms it seems.


## Apache is Still SLOW and Code Creep


More problems: at this point I am adding more AJAX for fun and making the site very interactive. If you hover over any timestamp a box pops up loading the price of bitcoin at that time. If you sit on the front page the latest chats will load every few seconds. This results in Apache becoming overwhelmed and eating all of the memory on the VPS. MySQL is still hogging memory at this point too, but Memcached + Sphinx has helped. Finally the site's code is becoming large and disorganized. This site was done without a framework as it grew organically from 2 PHP scripts ('latest chats' and 'search chats').


## Node.js + Express


Recently: I rewrote the site in Node.js using the express framework. It went very quickly and express was a dream to work with. The site is finally organized and code is very clean because I did an almost exact translation so blueprint was detailed. I am still using MySQL, Sphinx and Memcached with the Async library to keep myself free of callback hell. The jade templating language is a amazingly nice and I was able to use it to great effect. The lesson is this: might as well start the project correctly because it may grow! I also had to do annoying things like re-write all the old URL paths to the new URL paths with 301 redirects so I don't get a big Google ranking hit.


## Deployment: Varnish and Forever


A simple node Application is not comparable to architecture of Apache2 by any means so the node app should be served behind a proxy server if you want have multiple apps on the same server. I chose to use Varnish because I still have some PHP sites (the [coincepts.org](http://blog.coincepts.org) wordpress blog for example) I want to run from Apache on the same VPS box. Varnish also has the added benefit of being an HTTP accelerator so I hope it will speed the blog. This is where I have evolved the system to - the new trollboxarchive node app and the all of the other PHP sites are running behind varnish. I am running node from "forever" and load is not even comparable. It is like a dream (well, so far). I even added a voting system!


## Conclusions


It is best to start correctly with a good a architecture and firm plan. Obviously this project was just an experiment and for fun but it became more. I want [trollboxarchive](http://trollboxarchive.com) to be a record of the crypto trading community and all the good times we had during 2013. It may also be a record of the good times we are yet to have in 2014. I hope so anyway.
