---
author: Aaron Decker
comments: true
date: 2020-06-28
layout: post
slug: 2020-06-28-donnie-pump-covid-press-conference-trading-system
title: "\"Donnie Pump\" a Presidential Press Conference Trading System."
description: For a while it seemed like everyday in March of 2020 there was a White House press conference. This is an experiment building a system to help trade against this.
---

![Screencap of the March 13th 2020 Rose Garden Press Conference](/images/blog/press-conf-screenshot-1.png){: .center-image }
_Screencap of the March 13th 2020 Rose Garden Press Conference._{: .center-image }

## The Inspiration

The photo above is a screenshot of the CNBC stream of the infamous [Rose Garden Coronavirus press conference](https://www.youtube.com/watch?v=mB6mzESzUf0) where the Trump administration trotted out a bunch of Fortune 500 CEOs on March 13 2020. This was a few weeks into the COVID-19 pandemic and after the market had started to sell off in earnest. The market had hit a 7% down trading halt the day before, so they were trying to instill confidence.

I was watching this live, dumbstruck as they brought out one CEO after another of a major publicly traded corporation and I watched the charts as stocks for these individual companies spiked almost immediately after each CEO spoke.

This was the inspiration for building a tool to help trade these daily Coronavirus press conferences.

It seemed like just about every press conference the president would mention a specific publicly traded company and then seconds later the stock would start to move up. Typically, I noticed the stock might move up anywhere from 3% to 10% over the course of about 5 or 10 minutes and then either even out or revert back to where it was.

To me, this seemed like an easy thing to profit from programmatically. My friend [Marcus Wood](https://www.marcuswood.io/) agreed.

## The Idea

I went to work with Marcus on the idea that weekend. At first we were thinking we could just do this without human interaction [as people do with Trump's tweets](https://medium.com/@maxbraun/this-machine-turns-trump-tweets-into-planned-parenthood-donations-4ece8301e722) but after toying with that idea we realized how complex it actually is.

The process goes somewhat like this:

1. You need to transcribe the speech from the press conference to text
2. You need to pick out individual publicly traded companies that are mentioned (e.g. "McDonalds")
3. You need to convert these company names to ticker symbols ("McDonalds" --> "MCD")
4. Understand if this is good, bad, or old news (won't move the market).
5. Make an appropriate trade
6. Exit the trade at an appropriate time

Well, as you can see that is fairly complex and there is a lot to go wrong in there. What we settled for is something that instead of taking the human out of the loop just makes it easy for a human to quickly make the trade and operate the system.

## The Product

What we ended up with was this:

1. The system would transcribe the speech and match company names to tickers from a curated list
2. We show these in the UI and make it easy to trade into them quickly
3. The orders would go in and then automatically exit after a certain move up or a stop loss when they moved against us.

So for this system the user would enter the trade with the click of a button (e.g. allocate 50% of the cash to this trade) and would be able to quickly exit with the click of a button as well. The trades would also automatically exit if the position moved a certain amount.

## The Implementation

I had been wanting to try out the [Alpaca trading API](https://alpaca.markets/docs/) for a long time and finally this was my chance. I implemented the backend APIs to connect to the account, make trades, stream data, look up quotes, track positions, and basically everything you need to do open up a trading account.

Marcus went to work on the UI and we built out what ended up being the basis of a trading platform we could implement multiple ideas in ([which he wrote a little bit more about here](https://www.marcuswood.io/products/suri)).

The backend is written in Node.js, where in addition to connecting to Alpaca to trade and get market data I wrote the component which would take transcribed speech from the client and try to match this to a list of known publicly traded companies. This was harder than it seemed. There are a lot of common words like "corporation", "technologies", "partners" and even "health" which came up frequently in press conferences but were also in the names of many companies.

There are thousands of companies listed on NYSE and NASDAQ so what we ended up doing is building a curated list of names we thought were worth trading against. If I had a lot of time and a team of people I could do this a lot better against every listed company and would solve the problem differently.

Developing the rest of the platform was interesting - I hadn't worked on many things where a real-time UI was so important. Sure, server side code has to be fast. But it's a little different when the client and server need to be in sync so tightly.

What we ended up doing was shoving basically everything through a WebSocket connection. No RESTful architecture or GraphQL for this one! Everything was a WebSocket event. Marcus moved the client to use [MobX](https://mobx.js.org/README.html) which was designed for this sort of thing. The UI is written in React.

One other thing to note: the speech transcription was surprisingly easy because modern browsers actually have speech to text built in. We used the [Speech Recognition API and it worked great](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition).

## A Demo

I made a little GIF of a clip of the Rose Garden press conference when the president brings out the CEO of Target and he name drops some other companies. You can see our system taking the raw text and finding the company and ticker. By the way, don't worry: this is just a paper trading account for testing orders, I don't actually have negative $123k in my account.

![gif of the rose garden press conference demo](/images/blog/rose-garden-presser-demo-1.gif)

[Here is a link to the full-size version](/images/blog/rose-garden-presser-demo-1.gif)

## Placing Orders

Alpaca has some cool order types. One of which [is a "Bracket" order](https://alpaca.markets/docs/api-documentation/api-v2/orders/) which allows you do multiple things at once. For this project I wanted to enter a market buy when I heard the name e.g. "McDonalds" but then I also wanted to put in 2 limit orders based on this market order. I wanted to put in a stop loss to sell out of the position in case it moved against me, and I wanted to put in a limit order to sell at a higher price to take profits if I was right.

They allow you do just this with a single API call. The payload looks like this:

{% highlight javascript %}
{
  "side": "buy",
  "symbol": "SPY",
  "type": "market",
  "qty": "100",
  "time_in_force": "gtc",
  "order_class": "bracket",
  "take_profit": {
    "limit_price": "302"
  },
  "stop_loss": {
    "stop_price": "299",
    "limit_price": "298.5"
  }
}

{% endhighlight %}

So this is saying I want to buy at market, and then take profit at 302 (if we get that high), or I want to put in a stop limit that will hit the books if we get to 299 and then trigger if get down to 298.5.

Another thing I did was make sure we had a "Liquidate Positions" button on the UI so we could manually exit things if we wanted to, as well as a "Cancel Orders" button in case we wanted to cancel any limit orders sitting on the books. I initially wanted a big red "DUMP EVERYTHING!" button just in case I wanted to get out fast and panicked, but we made some reasonably sized and accurately named buttons instead.

## Summary

I've written a few automated systems based on trend following and mean reversion patterns before, but I've never built anything to make myself a platform to trade as a human operator directly. It presented some unique things to think about, and I keep thinking of new ideas I want to implement.

I really hope that Alpaca starts to support options trading and futures markets soon because I have a couple of ideas around doing pseudo-arbitrage between commodities and equities related to those underlying commodities in a programmatic manner. They have a really great API that is easy to work with but I'd like to see a lot more features from it. I'm still using Quant Connect for backtesting new ideas at this point.

Till next time!

