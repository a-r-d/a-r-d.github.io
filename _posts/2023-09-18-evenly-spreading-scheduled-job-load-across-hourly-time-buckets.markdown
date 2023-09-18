---
author: Aaron Decker
comments: true
date: 2023-06-08
layout: post
slug: 2023-09-18-evenly-spreading-scheduled-job-load-across-hourly-time-buckets
title: Evenly spreading scheduled job load across hourly time buckets
---

At Bounty we have a lot of nightly jobs that do things like "Update all changed products for each store once a day". Working within the constraints of AWS lambdas you usually end up doing fan outs w/ SQS queues because lambdas have a 15 minute timeout & additionally you might or __might not__ want to different things in parallel.

The typical procedure to do this in our stack looks something like this:

1. Create a lambda to enqueue a message to SQS for each active store
   a. This is usually based some criteria usually if they have active subscription, etc.
   b. I do a bulk enqueue here so this relatively quick
   c. I will carefully choose either FIFO (and the params for this) or classical queue depending on upstream rate limits.
2. Create another lambda to read the SQS messages and do the actual job for the given customer (store).
   a. You can adjust how many messages a single invocation will consume, just base it on how long it takes to process one record.

You will notice this has three pieces of infrastructure:

1. Lambda that enqueues messages.
2. SQS queue.
3. Lambda that consumes the queued messages.

## Reducing infra with one simple trick.

What if you can get rid of the enqueue function & the SQS queue?

One trick I have been using is creating a single lambda that is scheduled to run every hour that attempts to evenly spread out the load of processing a batch of records throughout a 24 hour period.

What this accomplishes is having to only use a single lambda on an hourly schedule.

How does it work? I take the modulo of the ID of the record set I am interested VS the size of the time bucket interval and process just that batch for the given time interval. Note in the example below there is a conversion because I use UUIDs (which conveniently are randomly distributed, so I should get even-ish sized buckets of records). 

```javascript
const ids =
  (await prisma.$queryRaw) <
  Array <
  { id: string } >>
    `
      select id
        from "ShopifyStore"
          where (@ ('x' || translate(id::text, '-', ''))::bit(64)::bigint % ${intervalTotalSize}) = ${interval}
          and
          active = True
          and 
          "hasActiveSubscription" = True
    `;
```

For the above my `intervalTotalSize = 24`, and `interval = new Date().getHours()`. Therefor I divide my processing up in 24 buckets evenly throughout the day.

Additionally, if you wanted, you could do this on a minute level fidelity and divide into 60 buckets processed once per hour. You could also do combinations based on hour + minutes.

But mostly, I am doing this for things where we have several hundred to several thousand records that need to processed only once per day. For this sort of thing I think it scales quite well until you start to see timeouts on the lambda (again, the limit is 15 minutes) so depending on the job size it can be quite robust.

The additional benefit is that you are hammering upstream APIs in many small bursts throughout the day, instead of say, one massive burst at 5 AM every day.

Here, you can see what this looks like on a real working lambda that runs 24 times per day:

![image of cloudwatch metrics](/images/blog/aws/cloudwatch-metrics-24hour-scheduled-job-load.png)
