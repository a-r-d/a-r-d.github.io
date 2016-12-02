---
author: a-r-d
comments: false
date: 2016-07-03 16:10:49+00:00
layout: post
link: http://ard.ninja/blog/web-push-notifications-web-workers/
slug: web-push-notifications-web-workers
title: Web Push Notifications with Web Workers
wordpress_id: 407
---

Did you know that you can now send push notifications to a browser even when the user is no longer on the page? The [notification API](https://developer.mozilla.org/en-US/docs/Web/API/notification) allows you to pop up OS level notifications from JavaScript. With [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) you are able to register a worker permanently in a browser that will handle these notifications offline. I'm going to outline how to do this with Google Chrome and Google Cloud Messaging. 

[Before I go into details, the sample code for all steps and components is here.](https://gist.github.com/a-r-d/44aeb60d60dccc5b35f5543db968fd81)



### Here is an example workflow, with the accompanying diagram. 






  1. Browsers asks for permissions to send notification.


  2. Register your web worker web worker.


  3. When registration comes back, subscribe to push on the registration object.


  4. when subscription endpoint comes back from the API, then you need to send this ID to your server.


  5. Fire off push notifications to the endpoint id from your server (this is the push notification subscription ID).


  6. Listen in your worker for "push" event and show messages.



[![](http://i.imgur.com/qP5OiZc.png)](http://i.imgur.com/qP5OiZc.png)
