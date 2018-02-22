---
author: Aaron Decker
comments: true
date: 2018-02-19
layout: post
slug: the-basic-math-of-trading-for-income
title: The Basic Math of Trading for Income
description: I break down some of the math of trading for a living to help me understand how to build a worthwhile trading system. 
---

![In a hammock in Maui](/images/blog/hammock-baldwin-beach-2-sm.jpg){: .center-image }
_Photo taken at Baldwin beach, Maui_{: .center-image }

Right now I am working on building trading systems.

In general I am looking to build specialized systems that don't scale. What do I mean by "don't scale"? Well when it comes to managing money the law of large numbers takes effect quickly. You cannot generate a high rate of return with a very large portfolio, you just cannot put enough money into small high risk trades that will be profitable. Luckily, I don't have a lot of money so I can do that things that _don't scale_.

So, for example, with fifty-thousand dollars [you could theoretically trade VWAP fluctuations back and forth](https://www.investopedia.com/ask/answers/031115/what-common-strategy-traders-implement-when-using-volume-weighted-average-price-vwap.asp) in Nvidia stock all day long and make a large profit. If you have 1 billion dollars, you cannot buy that much Nvidia in a single day without sending the price up to the moon. So a small portfolio can get a 200% return on investment yearly, while the large fund manager will struggle to achieve more than 10% consistently. 

For me, it has been helpful to understand the mindset of an active trader, a person trying to take a living out of the market every day. This is what my automated system will be trying to achieve, so let's break down the numbers when thinking about trading for income. And full disclosure here: I have not successfully done any of this __yet__, so this is just an exploration of the math!


## How many days can you trade, and how much should you make per day?

If you are trading in Equities in the US, that is about 5 days per week. It winds up being something like 240 days per year. I think it is helpful to work back from how much money you want to make a year or day and then understand how much profit you need to make on each trade, and how often you will need to do that. 

So let's say you want to make $500 per day. $500 per trading day ends up being $120k per year. I will put it in bold, since this is our reference point.

__$500 per day * 240 days per year = $120,000__


## How much can you make per trade?

So the answer to this question is two-fold: how much capital do you have to risk, and what kind of return can you make on your trades? Below is a table I built to show the relationship between profits, position size, and percent return on a trade. 

| Capital Risked vs. Pct Return  | 0.25% | 0.5% | 1 %  |  2%  |  4%  |  8%  |
| ------------------------------ |:-----:|:----:|:----:|:----:|:----:|:----:|
| __$1,000__                       | $2.50 | $5   | $10  | $20  | $40  |  $80 |
| __$3,000__                       | $7.50 | $15  | $30  | $60  | $120 | $240 |
| __$5,000__                       | $12.50| $25  | $50  | $100 | $200 | $400 |
| __$10,000__                       | $25   | $50  | $100 | $200 | $400 | __$800__ | 
| __$15,000__                       | $37.50| $75  | $150 | $300 | __$600__ |$1,200| 
| __$20,000__                       | $50   | $100 | $200 | $400 | $800 |$1,600|
| __$30,000__                       | $75   | $150 | $300 | __$600__ |$1,200|$2,400|
| __$50,000__                       | $125  | $250 | __$500__ | $1000|$2,000|$4,000|
| __$100,000__                       | $250  | __$500__ |$1,000|$2,000|$4,000|$8,000|
| __$200,000__                    | __$500__ |$1,000|$2,000|$4,000|$8,000|$16,000|


I marked the line in bold where you would make $500 or more based on the capital you risk for the return you get. Initially, you can see on very small intraday moves (0.25% or so), you need a large amount of capital to see a reasonable return. Alternatively you may notice you can trade small when there is a lot of volatility but that likely increases downside risk as well, and you may not always be able to find the volatility when you need.

This table is evidencce of why you probably shouldn't attempt day trading unless you have a decent bankroll. The math just doesn't work out. If you are just trading small moves you need to be well capitalized, and you need to be able to do it many times per week if not every day. So the [pattern day-trader rule at 25k](https://en.wikipedia.org/wiki/Pattern_day_trader) seems like a bit of a moot point when you look at this table, you need much more than 25k to be effective in generating real income. 


## Understanding Expectancy

Okay, so above we are just trying to figure out how many **winning** trades it will take to get to 
that yearly amount of money you want to draw. We actually need to know a few more things to figure out how much money we can draw off the account. 

So firstly, not all trades will be winners. In fact, depending on your strategy the majority could be losers. Most strategies can be categorized as "mean reversion" or "trend following". In general a good mean reversion strategy has a high win rate with a low payout. And trend following typically has a high payout with a low win rate. 

Expectancy is a formula. 

__E = ( Pw * Aw ) - (Pl * Al)__

{% highlight text %}
Pw = Winning percentage
Aw = Average Winner
Pl = Losing Percentage
Al = Average Loser
{% endhighlight %}

## An Example of Expectancy in a system

I will use a trend following strategy as an example. Markets are probably well [described as fractal in nature](https://www.investopedia.com/terms/f/fractal-markets-hypothesis-fmh.asp) so you can theoretically trend trade on many different time scales, but for this example we will use an example of trend trading on a time scale of about a month. 

Here are the rules of a trend following strategy we will calculate expectations for:

 1. You find a stock that seems to be trending up (somehow, using some indicators, for example). 
 2. You buy in and set a trailing stop loss 15% below your buy-in price. 
 3. You close the trade by letting the trailing stop get triggered

 The results of this system are as follows: 80% of the time stop gets triggered at an average loss of 12% and 20% of the time the stop gets triggered at a win, with an average win of 50%. Bad win rate but high win percentage. Expectancy is as follows:

{% highlight text %}
  Let's say the bet is $10,000

  Expectancy = (($5000 return) * 25% winrate) - (($1200 loss) * 75% lossrate)
             = $1250 - $900
             = $350  per 10k trade on average
{% endhighlight %}

So in this particular trade if you risk 10k on average you will make $350. But what if you can only do this once a month and you only have 100k in capital? That is only $3500 per month or $42,000 per year.


## How often can you trade your strategy?

The next question is this: if you have a trade that should have a positive expectancy you are going to want to do it as often as possible. But you only have a finite amount of capital and when you are in the trade the capital is allocated. So if you are doing long timeframe momentum trades maybe you can only 5 of these per year, and if you only have 1 winner a year you don't have a system that you can rely on for income. 

You probably need to do something more like this: look for a trade you can put on a few times per day. It should have a low but positive expectancy. You are probably looking at very small price moves of 0.5% or less, so you need to trade really large. So let's pretend we are intraday trading a strategy that only takes a few minutes to execute when the setup is right.

You trade intraday price fluctuations in small cap stocks, on average your win rate is 60% and you make 0.5% per win. When you lose or break even your average loss is 0.3% after fees and thanks to your tight stop losses.  

{% highlight text %}
    Each of this trades you trade with capital of $20,000

    Expectancy = ($100 return * 60% winrate) - ($60 loss * 40% lossrate)
               = $60 - $24
               = $36 per 20k trade on average
{% endhighlight %}

Obviously that won't work unless you can trade that well 20 times per day. Will you have a setup to make this trade 20 times per day? Unlikely (unless we are talking about an algorithm). So you really are going to want to risk more capital per trade. Realistically you need to do something like 100k and try to do it 5 times a day. Even then the market must cooperate **very** often, and what if this only works in raging bull markets?   

If you don't have at least 100k or 200k it seems like it would be hard to make this work. Especially when you factor in expectancy and how often you will need to trade. 


## A more reasonable approach

So if you are looking for income it seems hard to do longer term trend trading because you can't put in a lot of trades. You need a lot of trades to have a decent income. And if you are just trading minor fluctuations it also will be hard to make it work because you will need a lot of capital and you will be risking a lot of capital every trade. If you risk a lot of capital, even with a stop loss and there is something like a flash crash and your stop gets blow through hard. 

You want to figure out some middle ground here. 


## Risk, stop losses, position sizing, and correlation

__Ideally, you should risk 1% of principal per trade.__ Many famous traders say something along these lines and it is [Ed Seykota's rule of thumb](http://www.seykota.com/tribe/risk/index.htm) which he has mentioned in several interviews. So if you have 100k only risk $1000 a trade. But does that mean you can trade 10k at a time with a 10% stop loss? I think so. The stop may get blown though and you get slippage down to 20% occassionally but that works out to be only 2% and it seems OK to risk 2% some of the time. 

__It does not seem OK to risk 100k on a trade with a 1% stop loss!__ What if it blows though your stop so quickly you lose 5% before the order fills? This is _slippage_. Now you just lost 5k or 5% of your bankroll. And how about trades where you trade $1000 and can lose 90% or make 90%? That seems pretty safe as well, as long you don't a bunch of these open at the same time and they are all highly correleted. 

What do I mean by highly correlated? Well if you have 10 positions in _out of the money_ calls open and the positions are about $2000 each all on different tech stock and the NASDAQ bull market falls off a cliff, well you just lost everything. It doesn't matter that those calls were spread across 10 different stocks, those calls are going to zero, all of them, because all those tech stocks are correlated and move together. You just lost $20k or 20% of your bank roll in one highly correlated fell swoop.


## OK so what is the ideal position sizing and expectancy for a 100k bankroll?

If you have 100k I think it will be very difficult pull $500 a day on average out of the market. You would have to have some killer edge. More likely you would need to have a lot more cash to trade with before you can pull $500 a day in income. But if that is the size of your bankroll, what is ideal sizing?

If you ride up earnings day momentum you could potentially ride a 2% or 3% move in a short period of time. Do that with $20,000 and a tight stop and you could probably have a three or four hundred dollar expectancy (__again, assuming you have a high win rate and a tight stop__). It is probably reasonably safe to do this because with that much volume you won't get stopped out with a lot of slippage. That sounds like reasonably safe sizing, but I would love to hear feedback on that. 



## Putting the return rates in perspective

All of this needs to be put into perspective to make sense of it. So relative to what indexing
the S&P500 gives you, what do some of these returns look like? Well historically US equities 
return something like 9% a year, and that is at the high end of the estimate. 

Do you know what a daily 0.25% return rate looks like? So let's say you don't compound the money at all. What do I mean by that? I mean every day you make 0.25% and you take out winnings. So you risk 200k every trading day (240) and you take out $500, you do that 240 times in a row successfully. __If you add all of these up without compounding, that is a 60% return rate year over year (240 * 0.0025 = 0.6).__ If you were to compound that daily the rate would be much higher.

A 60% return rate is unheard of for a professional money manager. The [best big money managers on their best streaks have been able to deliver something like 20% or 30% compounded over a decade](https://www.investopedia.com/university/greatest/peterlynch.asp). I'm talking about people like Peter Lynch, Warren Buffet, and George Soros here. 60% is more than 6x what the index yields passively investing. 

The only way this is possible is [with a real edge](https://www.investopedia.com/articles/active-trading/022415/vital-importance-defining-your-trading-edge.asp) and a small amount of capital. Otherwise the law of large numbers applies and market outperformance becomes exponentially harder.







