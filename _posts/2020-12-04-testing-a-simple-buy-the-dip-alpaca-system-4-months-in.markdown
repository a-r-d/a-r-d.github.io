---
author: Aaron Decker
comments: true
date: 2020-12-04
layout: post
slug: 2020-12-04-testing-a-simple-buy-the-dip-alpaca-system-4-months-in
title: "Testing A Simple \"Buy The Dip\" Alpaca System (4 Months In)"
description: I put a very simple buy the dip system live a few months ago against Alpaca to see what would happen. 
---

![Buy the dip stats](/images/blog/buy-the-dip-stats.png){: .center-image }
_Screencap of the current state of this system._{: .center-image }

## Background

In my last experiment with Alpaca's trading platform before this one [I built a tool to help you trade press conferences](https://www.ard.ninja/blog/2020-06-28-donnie-pump-covid-press-conference-trading-system/), but it wasn't "hands free". 

For my next experiment I wanted to build something I could just set loose in the market and forget about and just come back to later to see if everything worked as expected. And I wanted to do this over a long period of time to give me confidence before I tried to build something more sophisticated. 

## "Buy The Dip"

So what is the simplest thing that can work and probably not go wrong? That's right - I decided on a "Buy The Dip" strategy. 

So here is was I did. I programmed a very simple lambda function (I used Serverless framework and deployed to AWS Lambda) that would place limit orders below the current price of a given stock when triggered. 

## The details:

I started by depositing $1000 into the account and I picked a stock that traded for a small numeric value that was likely to experience moderate volatility - I picked Barrick Gold (symbol: $GOLD) which is a large cap gold miner. Gold had recently been moving around a lot when I wrote this.  

1. At 10:30 AM EST trigger lambda function (I decided on 10:30 because there is often odd volatility when the market first opens, so I wanted to catch moves that play out during the rest of the day).
2. The function places 3 limit orders
3. Order 1: limit BUY 1 share @ 2% below current quote
4. Order 2: limit BUY 1 share @ 4% below current quote
5. Order 3: limit Buy 1 share @ 7% below current quote

All of these orders were marked `time_in_force: "day"` so they just automatically cancelled at the of the day and I would place them again the next day. 

## The Results

The system traded very infrequently. There was only one instance in August through December where 2 consecutive limit orders actually did fill. This was on November 23rd when some vaccine news came out and Gold prices got hammered.

StartingEquity: 8/14 - $1000
Ending Equity: 12/4 - $974.47

Mostly this was because the price of Barrick Gold has fallen quite a bit since August, and I have 10 shares of it now in this account. So a loss of about $25. 

But if I had just bought 10 shares of $GOLD at [$26.99, the close price](https://finance.yahoo.com/quote/GOLD/history?p=GOLD), Barrick is currently at $23.48 so I would be down $35. So buying the dip helped significantly in a falling market here. 

However this really silly because I could have just built a few backtests and run this strategy through them to see if it was good or not. The real purpose here was to test if the system worked and see how reliable Alpaca is, which it did and it is! 

![The actual trades the system made](/images/blog/buy-the-dip-trades.png)

## The code.

I'll post [the bulk of the code here in this gist.](https://gist.github.com/a-r-d/2b473e26e79d844c248478ca62980e16)

Nothing particularly fancy about this, except one thing I will share here is the cloudwatch schedule string I used to trigger this. Remember it goes 10:30 am mon-fri every weekday (cron is in UTC, so 10 am UTC is 14:00).

```
cron(30 14 ? * MON-FRI *)
```

I was happy this the results of doing this on AWS Lambda with serverless framework. I had zero issues with it. 

## Could this actually be useful?

Yeah, I think it could but again this was more about just trying to get something working and see if it would hold up consistently for a long period of time. 

I do think something like this would be very useful for accumulating thinly traded small cap or OTC stocks over a long period of time. 

One thing I was thinking would be great to have something like this for is accumulating the various Fannie Mae / Freddie Mac preferred shares. There are a ton of ticker symbols for these on the pink sheets and they are thinly traded and sometimes make wild and irrational moves. Sometimes I think people will just randomly liquidate positions in these but really the only thing that matters for these shares is the progress of the lawsuits and [the recapitalization plan](https://www.wsj.com/articles/fannie-freddie-tap-wall-street-banks-to-advise-on-recapitalization-11592252631).










