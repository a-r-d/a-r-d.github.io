---
author: Aaron Decker
comments: true
date: 2016-12-28
layout: post
slug: algorithmic-trading-experiments-with-cryptocurrency
title: Algorithmic Trading Experiments With Cryptocurrency
description: A summary of my attempts at algorithmic trading using various strategies on cryptocurrency exchanges.
---

There are fields where dilettantism cannot cause any harm. Algorithmic trading is not one of these. Because if you are writing a program to automatically make you money, you can just as easily write on to automatically lose you money. Remember what happened to [Knight Capital](https://en.wikipedia.org/wiki/Knight_Capital_Group)? In this post I'll describe a few algorithmic trading experiments I did with crytocurrency, as someone who has never worked in this field professionally (trading) I hope I can be forgiven for any errors.


## My first naive attempts (mean reversion)

A few years ago when I first started trying to do this I took what I now know is termed a "mean reversion strategy" (after reading [Irene Aldridge's book](http://amzn.to/2inQmVl)). It was a fairly obvious place for a beginner to start, and this approach is what I had seen some people throwing together on some crypto trading forums. My implementation was crude, there were many variables I had to guess at. The algorithm works as follows:

1. Compute an average point from some previous time period.
2. Set an amount above this where you sell, place the order on the books
3. Set an amount below the average where you buy, place the order on the books
4. Every few seconds cancel all orders and repeat steps 1-3.

So what you are doing is guessing that the market has some average price and you are smoothing out the temporary spikes and drops. And, if there is a quick move that does not correct soon, you could get screwed, but overall you are providing liquidity to the exchange and absorbing a temporary excess in trades in either direction. This is good if you are making money consistently, and if your working capital gets wiped out infrequently it does not matter. But if you are making money slowly, a big move will wipe out your profits for months.

I didn't appreciate how risky this was until reading [Taleb's Black Swan](http://amzn.to/2i2wfj6). I wonder if the big market makers on the major exchanges buy call options in case of massive moves?

_Here is a diagram explaining trading on mean reversions (from quantopian)_

![mean reversion](/images/blog/mean-reversion.png){: .center-image }

This is actually what big market makers do on stock exchanges. Think about it: if you have some shares of AAPL and go to sell it, are you sure that you will have a buyer at that very instant? There may not be a specific buyer, but a market maker with deep pockets will step in to make sure there is liquidity, in exchange for a penny or so of profit. [The market maker makes money on the "spread"](http://www.investopedia.com/terms/m/marketmakerspread.asp), this difference between the lowest buy order on the books and the highest sell order on the books.  

Anyway, I never made money doing this, and I don't think I ever did it long enough to study my results with any rigor. The main problem was that Btc-e.com (the exchange I wrote the bot for) charged a 0.3% fee per trade, so I had calculate that into my trades, which turned out to be prohibatively expensive, especially since I was only trying to profit off of tiny fluctuations.


## Second attempt: A Moving Average Convergence Divergence bot

I next became interested in the idea making a trading bot that would execute momentum style trades based on a [Moving Average Convergence Divergence](https://en.wikipedia.org/wiki/MACD) strategy. This is a common day-trading strategy, its whats called a ["technical trading indicator"](http://www.investopedia.com/articles/trading/11/indicators-and-strategies-explained.asp).

The basic idea of MACD is pretty simple: you compute two moving averages, one longer (e.g. 24 hours) and one shorter (e.g. 60 minutes), when the moving averages cross each other those are buying or selling indicators. The thesis behind this is as follows: markets to tend to do next what they just did recently - i.e. if it moved up it will continue to move up.

_Here is one of the more clear images I could find demonstrating this:_

![macd diagram](/images/blog/macd-diagram.gif){: .center-image }

Interestingly, the thesis behind momentum trading and the entire MACD strategy appears opposed to that of the idea of a mean reversion strategy. On one hand you are saying a market gains momentum in each direction, while on the other hand you are saying that the market should revert to the mean. However, in practice you are looking at different time frames (on the order of seconds vs on the order of hours or days).

I tried this for a time as well but ultimately was too afraid to risk a large amount of capital. This primarily was due to backtesting results. While running another website I had amassed a large database of historical pricing data which I could run back-tests against (years worth of sub-minute quotes). I tried a fairly exhaustive set of variations in my backtests but with the 0.3% trading fee I could not find a set of parameters with which I could consistently make money over a long period of time.

Perhaps my expectations of profit margin were too high, or perhaps the fee was too high, but I just could not find a good set of backtest parameters that worked for me with what I felt was an appropriate margin of safety. I actually did run the algorithm live for a while with about $50 for it to use, but overall it never did much more than break even.


## Third attempt: Bellman-Ford style currency arbitrage.

This is another strategy that I read about in [Irene Aldridge's book](http://amzn.to/2inQmVl), and its actually currently used by many parties on real forex exchanges. I ended up making a Java library out of this one and [open sourcing it on Github](https://github.com/a-r-d/Bellman-Form-BTCe-Arbitrager).

The way this algorithm works is that you model many exchange rates between different currencies on an exchange as a graph, then using this datastructure you model each exchange rate as a weight and you look for "negative cycles" (in computer science parlance) through the graph. __In plain english this means that you try to find a path through a set of currencies where you end up with more money than what you started with__. So I could do this on Btc-e.com because there are multiple currencies on that exchange.

![example bellman form cycle](/images/blog/example-forex-trade.jpg){: .center-image }

You can guess again what kills you here: trading fees. It is a 0.3% fee to trade, and I need to make 3 trades through a cycle, __so the arbitrage has to give more than 0.9% total, which is a lot__. Secondly, these arbitrage opportunities are usually ephemeral: they last seconds a most, so you need to make all of the trades in the set of trades very fast.

One of my big annoyances was that I could not place a ["market" order](https://en.wikipedia.org/wiki/Order_(exchange)#Market_order) (fill the order at the current market price), btc-e only supported ["limit" orders](https://en.wikipedia.org/wiki/Order_(exchange)#Limit_order) (fill the order at a specific price). Well, if you place a limit order and it doesn't fill, then you must cancel it, and place the order again, and repeat this until you get your order to fill. I became very annoyed at having to deal with this, and the lag associated would kill the speed at which I could complete the trade cycles, even if I could control execution price a bit better.

Ultimately, with this algorithm I never even got the trading side working. I just wrote the code that would compute these negative cycles and realized it would not often to be profitable to make the trades.


## In the future

Trying these different strategies was intrinsically interesting, but also interesting as a software developer doing the implementation. It is not often you get to write code that so directly can make or lose money, and doing it instills in you a special level of attention to detail and carefulness. There were so many variables to consider with algorithmic trading code, and performance and timing became important as never before.

That said, I wouldn't attempt it again unless I could do so on an exchange without the tyrannical shackles of percentage based trading fees. Going forward the site I'm excited about taking a look at when I have some time is [Quantopian](https://www.quantopian.com), which appears to have a platform that allows you to write python code to trade against some major exchanges with. Let me know if you have any experience with it and suggestions for a beginner.
