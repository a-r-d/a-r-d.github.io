# Guidelines for Microservices.

I read a couple of books on microservice recently and I wanted to summarize things here that I felt were common between them. 

I think we can break these into two parts: characteristics that are more like rules or definitions, and others that are more like suggestions. Keeping this in mind, I'm going to start with things are especially imperative and end up with things that should read more like recomendations.

## Data Segregation

Microservices should connect to their own data store and not share it. Example: an auth service should have it's own database to store user 
related information and no other service should be able to connect directly to that database. 

If a service needs heavy access to the 
data of another service, consider combining them or propagating all of the data using a message queue,
batching system or data stream such as Kafka.

## Apply Postel's Law

"Be conservative in what you do, be liberal in what you accept from others"

Microservices should have a small surface area of published contracts. Avoid "Mega Services", which is where microservices will slowly evolve to contain an enourmous amount of endpoints as new requirements crop up over time. 


## You build it you run it, but if not stick to a monolith

If you are truly doing microservice architecture and you cannot rapidly provision and maintain your systems then it will be a burden rather than a boon. If you work in an organization where you have a database team, a server infrastructure team, a firewall team, a security team, a proxy team (ect...), and the developers must request work from each of these teams to deploy each new service then you should just stick with monoliths because this will become a slow death march of bureaucracy. 


## Don't version until you must, and then consider Headers

Versioning should be put off until absolutely necessary due the additional dimension of complexity it will introduce into any system. However, if you must version, a great way to do this is by using Headers, which will probably be easier for your consumers to upgrade from. Explicitely changing the URI routes can cause you to break old clients. Consider a header like so to enforce versions:

```
Accept: application/json; version=3
```

OR use a nonstandard application header like so:

```
X-API-Version: 3
```

## Use Aggressive Timeouts and Circuit Breakers

Default timeouts on many HTTP client libraries are unnacceptably long. You should be using agressive timeouts in your microservice communication layer, and ideally use a circuit breaker library to help detect and isolate failures. Circuit breaker libraries like Hystrix from Netflix can help you set up fallbacks, alerting, and monitoring. If a dependency starts to run slow you should just let the calls fail, then alert about the failure. If API calls are taking greater than 500 ms (or, ideally 100 ms) for just about any process you have a serious problem. 

Actually, if you have an API call that regularly takes more than 100 ms you may have a big problem. Here is a [really awesome talk by Ilya Grigorik of Google](https://youtu.be/Il4swGfTOSM?t=34m57s) that explains why you really only get 100 ms on the server side if you want to render a web page in 1000 ms (hint: network overhead and browser rendering is slower than you think). 

The other big reason to use circuit breakers is to prevent cascading failures of services and to allow downstream systems time to recover. In part of doing this you will also be building in fault tolerance (or at least fault handling) at every layer of interaction between services. 


## When using a Circuit Breaker Fallback, your Fallback should never fail

Ideally your fallback simply serves up static content when it fails, but if you expect to use your fallback, it should not do anything with a potential of failure. If you cannot make that work you should just skip the fallback and deal with the failure of the dependency. 


## Use semantic versioning

 - Major version: you made an incompatible API change. This is a breaking change. 
 - Minor version: you added backwards compatible functionality.
 - Patch version: you made a backwards compatible bug fix.


## When troubleshooting issues, remember the four golden signals.

Measure then try to fix. [Remember the four golden signals](https://landing.google.com/sre/book/chapters/monitoring-distributed-systems.html#xref_monitoring_golden-signals):

  1. Latency - measure response times
  2. Traffic - measure req/sec, disk I/O, network I/O
  3. Errors - measure rate of failures per request.
  4. Saturation - measure how full the service is: measure CPU usage, Memory usage, Disk usage, server I/O all relative to saturation point.

## If you have a slow service analyze performance issues using data

Again, measure then fix. Measure how long response is taking, then measure how long each step in the call takes. Is most of the time spent in the database query? Is serialization taking longer than you might expect? How many queries or API calls are you making that you can cut down?

If the problem is in the database layer, use the EXPLAIN tool to understand the query, and look at other database specific metrics. Look at the size of the result set, and see if any complex logic is performed in processing the result. 

If the problem is in other API calls to other services are those services meeting their SLAs? Can you do anything in parallel? Can anything be done in the background? Are you getting more data than you need? 



