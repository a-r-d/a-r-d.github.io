---
author: Aaron Decker
comments: true
date: 2016-12-21
layout: post
slug: shutting-down-trollboxarchive
title: Shutting Down Trollboxarchive
description: Why I'm Shutting Down Trollboxarchive.com, some stats and some explanations
---

## What was the trollboxarchive.com?

Back when there were only a few bitcoin exchanges (and very few alt-coin exchanges - i.e. exchanges for Litecoin, Namecoin, ect) Btc-e.com was one of the most reliable and most fun places to trade. Much of this was thanks to the chat window on the front page of the exchange and there would inevitably be manipulations, drama, and pump and dumps going on in this unregulated market, all of which was reflected in what people were talking about in the chat.

Around this time (2013) I went in on a venture with a couple of other bitcoin enthusiasts that we called "Coincepts Technologies". We created a couple of bitcoin related websites and most of them were utilities to help miners of both bitcoin and [scrypt based alt-coins](https://en.wikipedia.org/wiki/Scrypt). For example, one enabled you to build a computer with drop down boxes and calculate how many coins per month you could mine with it, it was an affiliates site. Separately around this time, I also created an iOS app called "Cryptoticker" that pulled data on alt-coins from several exchanges.

One of these websites that we created was trollboxarchive.com. The site scraped the chat logs from btc-e.com as well as the price data, I made then made the data searchable and threw the website together in about a week or two ([I wrote in more detail here about how it evolved over time](http://www.ard.ninja/blog/trollboxarchive-com-technology-overview/)). It was pretty fun to build, and the site was getting a lot of traffic. Long story short, there isn't much traffic anymore probably for numerous reasons.

![trollboxarchive traffic stats](/images/blog/tba-traffic-screencap.png)


## Where did all of the traffic go?

Its deeply satisfying to see the 1 million pageviews number over the 3 years the site has been up. The highest month was around 60k pageviews, but recently it has been 1k to 2k pageviews per month. Previously, the cost were paid by advertisers (usually mining pools), or advertisements to our own affiliate sites, but now there just isn't enough traffic to do that. I did try to monetize the site with adsense (and to do that, unfortunately, I had to filter all of the profanity people love to use in the chat window) but it still only made about $40 all year. With the server at $80 / year and the domain renewal fees, and having to deal with backups and security updates, I figured it is time just to let it die, thus I am not going to renew my VPS this year on 12/27/2016.

A year or two ago Btc-e.com instituted a policy where you had to have $100 in your account to chat. That pretty quickly killed the community of people chatting, then they raised this to $1000 later, which further diminished the activity. At the same time, interest in cryptocurrency is not a the fever pitch that it once was. Check this google trends chart if you don't believe me:

![google trends bitcoin](/images/blog/bitcoin_popularity.png)

Additionally, you can see interest in the btc-e.com exchange has fallen precipitously too, whether that is due to other exchanges, or overall cryptocurrency interest is up to you to judge.

![btc-e.com google trends](/images/blog/btce-traffic.png)


## Thanks everyone

If you ever used the site, I just want to say thanks. Running this site over the last three years helped me learn a lot as a software developer. I picked up so many skills that the entire endeavor been invaluable to me even if it was never profitable for me to run from a time standpoint. I remember when I first started building the site it would crash often. I learned tons of tools to make it more efficient and handle the data and traffic: Node.js, Sphinx, MariaDB, Nginx, cloudflare, memcached, to name some. These are technologies that I use continue to use in my work as a web developer. So thanks everyone.
