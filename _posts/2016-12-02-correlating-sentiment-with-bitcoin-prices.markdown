---
author: Aaron Decker
comments: false
date: 2016-12-02
layout: post
link: http://ard.ninja/blog/correlating-sentiment-with-bitcoin-prices/
slug: correlating-sentiment-with-bitcoin-prices
title: Correlating Sentiment with Bitcoin Prices
description: Is it possible to correlate bitcoin prices from chat logs on a bitcoin exchange?
---

### What is Sentiment and how can I correlate it with bitcoin prices?

I have been wanting to write about this for a long time. I have several years worth of chat logs from the [btc-e bitcoin exchange](https://btc-e.com), as well as price data, and I want to try to see if they correlate.

I have all this data due to running [The Trollbox Archive](http://trollboxarchive.com) since about 2013. The "trollbox" is what the chat window on the Btc-e exchange is affectionately referred to by regulars, however I have ceased to be regular, and never traded very actively begin with, though I did a lot of mining back when solo miners could do it profitably.

I have long suspected that you could predict when a given cryptocurrency will sell off or rise steeply by watching the chatter in the chatbox, but I have not been able to prove it. At one point I even had some queries running to pull out counts of the word "sell" and "buy" and plot it on a graph vs price, but at best I found only a lagging indicator.

I have been frustrated by not being able to explore this unique opportunity more thoroughly, because I have strong gut feeling that it should be possible to find some leading indicator of price change. There must be some way to predict prices just by listening to and analyzing what people are saying in aggregate.


### Neural network based classification problem.

I just started studying neural networks recently, which I am going to use to tackle this problem, so now is the perfect time.

I have been working on a dataset of rotten tomatoes reviews with a group at work. The inputs into the neural network are the words of the reviews, and the outputs for training the network are the discreet ratings of 1-5 stars for the movie.

Similarly I think you could break down price change deltas (e.g. maybe like: -3%, -1%, 0%, +1%, +3%) of given price change over the next 1 minute from when words were chatted. From this you may be able to train a network to find a leading indicator. Once you do that, you can trade profitably on that information.
