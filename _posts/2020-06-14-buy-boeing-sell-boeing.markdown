---
author: Aaron Decker
comments: true
date: 2020-06-14
layout: post
slug: 2020-06-14-buy-boeing-sell-boeing
title: Buy Boeing, Sell Boeing?
description: Can you just buy every dip and sell every pop on some stocks?
---

![boeing backtest screenshot results](/images/blog/buy-boeing-sell-boeing.png){: .center-image }
_Screenshot of the backtest of the algo I describe below._{: .center-image }

Since the market crashed in March of 2020 the rebound has been swift and irrational.

Boeing, for example, is in many ways worse off than it was in March. It's clear air travel is plummeted and that airlines will impacted for years. Where will they get the money to purchase planes?

An example of one headline in April: ["Boeing customers cancel staggering 150 Max plane orders"](https://www.cnbc.com/2020/04/14/boeing-customers-cancel-staggering-number-of-737-max-orders.html).

## Buy the dip?

One thing I've noticed is that since the end of March you can basically just buy every dip and expect a pop, selling the next day. I mentioned this to a friend on Friday and decided to backtest it.

Well, sure enough it works!

I'll mention I made one modification. Originally I wrote the system like so:

1. Check if Boeing is down more than 3% 15 minutes from close
2. If yes, buy with 100% of portfolio
3. The next day, 15 minutes from open liquidate the portfolio.

This worked OK. Great actually! It returned about **25%**. But want to know what really kicked it up a notch?

Instead of just selling the next day, I only sell if the position is sitting at a realized gain. So e.g. if the next day its flat or drops another 1%, don't sell it, just keep holding on until its up and THEN sell. Of course this is completely insane and you would have to expect the market to only go up, but that's what has been happening.

Guess what? This simple system **returned a whopping 65% in two-ish months**. Yeah, I know, crazy.

Here are the raw trading logs:

![boeing trading logs](/images/blog/boeing-backtest-screenshot.png){: .center-image }

## Here is the code

Here are the details of the backtest:

- start with 100k in cash
- start at April first and go until last friday
- end up with about 165k or a 65% return.

I wrote this little script on Quant Connect. The screenshot at the top of the page is the code, and the code below is everything you need to try this out:

{% highlight python %}
class BasicTemplateAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020,4,1)  #Set Start Date
        self.SetEndDate(2020,6,12)    #Set End Date
        self.SetCash(100000)           #Set Strategy Cash
        self.SetWarmUp(0)
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)

        self.AddEquity("SPY", Resolution.Minute)
        self.SetBenchmark("SPY")

        self.targetSymbol = "BA"
        self.openPrice = 0
        self.downPctTrigger = -0.03

        self.AddEquity(self.targetSymbol, Resolution.Minute, Market.USA, True, 1.0)

        self.Schedule.On(self.DateRules.EveryDay(self.targetSymbol), self.TimeRules.AfterMarketOpen(self.targetSymbol, 1), Action(self.onMarketOpen))
        self.Schedule.On(self.DateRules.EveryDay(self.targetSymbol), self.TimeRules.AfterMarketOpen(self.targetSymbol, 15), Action(self.sellItIfHeld))
        self.Schedule.On(self.DateRules.EveryDay(self.targetSymbol), self.TimeRules.BeforeMarketClose(self.targetSymbol, 15), Action(self.buyIfDown))


    def OnData(self, data):
        pass

    def onMarketOpen(self):
        self.openPrice = self.Securities[self.targetSymbol].Open

    def buyIfDown(self):
        currPrice = self.Securities[self.targetSymbol].Price
        openPrice = self.openPrice

        # e.g. (95 - 100) / 100 = -0.05
        pctDiff = (currPrice - openPrice) / openPrice

        # if gt than loss of x
        if pctDiff < self.downPctTrigger:
            self.Debug("Buying at: " + str(currPrice) + " pct down: " + str(pctDiff))
            self.SetHoldings(self.targetSymbol, 1.0)


    def sellItIfHeld(self):
        if self.Portfolio[self.targetSymbol].Quantity > 0:

            # just making this easy to comment out
            # this is the logic that says only sell if you are sitting on a profit
            # otherwise, we just keep holding until the price moves up
            if self.Portfolio[self.targetSymbol].UnrealizedProfit < 0:
                return

            currPrice = self.Securities[self.targetSymbol].Price
            self.Debug("Selling at: " + str(currPrice))
            self.Liquidate(self.targetSymbol)

{% endhighlight %}

## Obligatory warning and disclaimer

Try the backtest yourself.

And, by the way, I'm just talking about running the backtest. This is not investment advice nor am I suggesting your actually do this. There are obvious risks with this, e.g. one day Boeing could just declare bankruptcy and the price goes down and never recovers. This is for entertainment only.
