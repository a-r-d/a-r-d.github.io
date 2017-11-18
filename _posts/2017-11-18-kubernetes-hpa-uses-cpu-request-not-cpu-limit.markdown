---
author: Aaron Decker
comments: true
date: 2017-11-18
layout: post
slug: kubernetes-hpa-uses-cpu-request-not-cpu-limit
title: Kubernetes HPA uses cpu.request not cpu.limit
description: A full site build with React and Redux using "Create React App"
---

![kubernetes](/images/blog/kubernetes.svg){: .center-image }

## One Day I noticed an odd thing on a deployment

Recently, I was looking at a deployment with a few dozen pods in it and I noticed something odd about the resource usage. There had been some trouble in the past where this service always seemed to scale and be under hight load. This particular morning when I checked the HPA, it seemed to show around 40% CPU usage, even while my dashboard was reporting that this service was not getting much traffic.
I shelled into a few pods and ran top, only to find the CPU usage was hovering around 5% in most pods. According to another dashboard every pod was using around 100 millicores to 150 millicores (10% to 15% of a single core, so not much).


## Checking on the cpu resources

Next I inspected the details of the deployment and the pods. As it turned out the helm chart was configured in an odd way. It looked something like this:

{% highlight plain %}
resources:
  request:
    cpu: 300  
  limit:
    cpu: 4000
{% endhighlight %}

This service had comically low requested CPU resources and comparatively high CPU resource limit. This was throwing everything out of whack as it turns out. Some research reveals how these numbers are used to calculate resource usage in different places. Here is what it meant:

 1. When you run top in docker it is looking at percentage used out of ```requests.limit```.
 2. When the HPA CPU% used it looks at percentage used out of ```request.cpu```.

Ah, so docker showed low CPU usage (as did the JVM stats), and kubernetes showed high relative usage (which is what HPA was using)!


## So why is it bad to have requests and limits on CPU far apart?

It's not necessarily bad it just throws all of your HPA autoscaling calculations totally out of whack. So normally you may set your HPA to autoscale at 50% to 60% CPU, then when the services starts to encounter load, the HPA has time to scale up the number of pods in the deployment so your service can handle the traffic coming in. Now, you could set your HPA to scale 500% cpu usage, and it will scale when the pods are using 1.5 CPU cores (if your r```equest.cpu``` is 300, like above), but that seems odd.

When you set the ```request.cpu``` very low relative to ```limit.cpu``` (and low relative to baseline usage) it causes the deployment to scale under light load. This costs extra money and if you use something like application level caching it puts more load on downstream services too.

Depending on where your metrics are driven from it will screw things up to. If I have metrics being reported out of JVM stats on the pods, then I am not going to see high CPU usage until well after the deployment has scaled up to the max number of pods, and in the process draining all of the resources in the cluster and costing tons of money.
