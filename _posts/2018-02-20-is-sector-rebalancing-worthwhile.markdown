---
author: Aaron Decker
comments: true
date: 2018-02-20
layout: post
slug: is-sector-rebalancing-worthwhile
title: How Does Sector Rebalancing Impact Returns?
description: I do some backtests with sector rebalancing and figure out if it is worth doing!
---

![In a hammock in Maui](/images/blog/lake-in-winter.jpg){: .center-image }
_Photo taken at Lake Minnewaska, Minnesota_{: .center-image }

I have read investing books in the past that harped on "sector rebalancing" as a good idea. Reasons commonly given are: reducing your risk profile, or to attempt to keep risk profile constant, or even to increase overall returns (via mean reversion). But what really happens?

First, what is a sector? In this context it means asset class - specifically bonds, equities, emerging markets, or real estate. It could also mean gold or cash. 

Second, what is rebalancing? It is when you fix the percentages of your portfolio in each asset class, and then periodically make trades to keep this percentage constant. I am going to do some backtests to see what happens when you sector rebalance.


## Experiment 1: never rebalance vs monthly rebalance (VOO, VT, BND, VNQ, VWO)

I'll do this experiment a few times with different ETF compositions. Here is composition #1

1. 25% VOO (Vanguard S&P 500 etf)
2. 25% VWO (Vanguard emerging markets etf)
3. 10% VT (Vanguard total world stock market etf)
4. 25% BND (Vanguard total bond etf)
5. 15% VNQ (Vanguard real estate etf - mostly REITs)

So you can see I'm trying out a group that should gives us a few different sectors. Bonds, US stocks, foreign stocks, and real estate. Let's see how it does with just buy and hold from __January 1 2004 to February 16th, 2018__. [QuantConnect Code is here](https://gist.github.com/a-r-d/5d271f01c29f15b8b68a4409e62c282c).

![Sector allocation no rebalancing](/images/blog/sector-tests/sector-allocation-no-rebalance.png){: .center-image }

#### Okay, great, let's do the rebalance monthly and see what happens:

![Sector allocation monthly rebalancing](/images/blog/sector-tests/sector-rebalance-monthly-1.png){: .center-image }

### Experiment 1 Conclusions

For this composition, monthly sector rebalancing reduces overall returns while also reducing max drawdown and increasing sharpe ratio. So less volatility but less overall return. 


## Experiment 2: no rebalance vs monthly rebalance (VTI, VWO, BND)

This is going to basically be Jack Bogle's three fund portfolio in equal portions. Again time frame is __January 1 2004 to February 16th, 2018__.

1. 33.3% VTI (US Equities, total market etf)
2. 33.3% VWO
3. 33.3% BND


![Three fund no rebalancing](/images/blog/sector-tests/three-fund-no-rebalance.png){: .center-image }

#### Alright, now here is the 3-fund with monthly rebalance

![Three fund with rebalancing](/images/blog/sector-tests/three-fund-with-rebalance.png){: .center-image }


### Experiment 2 Conclusions

Again basically the same results, monthly sector rebalancing reduces overall returns while also reducing max drawdown and increasing sharpe ratio. So less volatility but less overall return. 

What is remarkable is how rebalancing ends up having so little effect overall in a 14 year period. For the most part, you just pay more in fees. 


## Experiment #3 All, US Equity sectors

OK so what if we just invest in different US equity sectors (e.g. financial, technology, utilities, ect) and rebalance between these monthly? Will we see any alpha? Will it hurt returns?

We will invest in equal portions of the following ETFs:

1. VGT - Technology
2. VDE - Energy 
3. VCR - Consumer Discretionary
4. VFH - Financials
5. VHT - Healthcare
6. VPU - Utilities


![sectors no rebalancing](/images/blog/sector-tests/equity-sector-no-rebal.png){: .center-image }

#### Now here is the equity sectors with monthly rebalance:

![sectors with rebalancing](/images/blog/sector-tests/equity-sector-with-rebalance.png){: .center-image }

### Experiment 3 Conclusions

This time the results are somewhat different. Drawdown is actually slightly worse with rebalancing during 2008, but returns are slightly increased. Sharpe ratio is basically the same. The surprising thing is that this time we beat buy and hold by using rebalancing, even after fees. There must be some mean reversion at work here, but the difference may not be statistically significant. 


## Experiment 4 - Rebalance on the Dow Jones Components.

Because we saw a more interesting result with equity sector etfs, what if we rebalance between 30 or so individual stocks? I will try this on the Dow Jones components from Jan 1 2016 to Jan 1 2018. The other change I'm making to this experiment is to start the account with 1 million dollars, just to reduce the effect of trading fees on the outcome.

Without rebalancing:

![dow jones 2 years no rebalancing](/images/blog/sector-tests/dow-jones-2016-to-2018.png){: .center-image }

With rebalancing:

![dow jones 2 years with rebalancing](/images/blog/sector-tests/dow-jones-with-rebal-2016-2018.png){: .center-image }

### Experiment 4 conclusions

We didn't do much here except for pay more in taxes and fees due to the churn. 


## overall conclusions

All we can really say is that if you had rebalanced monthly over the last 14 years with a variety of portfolios it would not have made much of a difference. The result is a little surprising because I would have expected rebalancing to do much worse than not rebalancing. 

If you consider that you are continually buying into weaker markets and selling the stronger ones, it seems that you will be clipping your winning allocations all of the time. But there must be some mean reverting process at work here where the weaker markets become stronger again.

Overall I think the result of this is fairly inconclusive and you would need to examine this system over a much longer time period to see if it will make a big difference.  



