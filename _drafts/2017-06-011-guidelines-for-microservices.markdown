# Guidelines for Microservices.

I think we can break these into two parts: things that are more like rules, and things that are more like suggestions or characteristics. 

## Data Segregation

Microservices should connect to their own data store and not share it. Example: an auth service should have it's own database to store user 
related information and no other service should be able to connect directly to that database. 

If a service needs heavy access to the 
data of another service, consider combining them or propagating all of the data using a message queue,
batching system or data stream such as Kafka.

## Apply Postel's Law

"Be conservative in what you do, be liberal in what you accept from others"

Microservices should have a small surface area of published contracts. Avoid "Mega Services", which is where microservices will slowly evolve to if you are not careful and disciplined. 


## You build it you run it, but if not stick to a monolith

If you are truly doing microservice architecture and you cannpt rapidly provision and maintain your systems then it will be a burden rather than a boon. If you work in an organization where you have a database team, a server infrastructure team, a firewall team, a proxy team (ect...), and the developers must request work from each of these teams to deploy a new service then you should just stick with monoliths because this will become a slow death march of bureaucracy. 


## Don't version until you must, and then consider Headers

Versioning should be put off until absolutely necessary due the additional dimension of complexity it will introduce into any system. However, if you must version, a great way to do this is by using Headers, which will probably be easier for your consumers to upgrade from. Explicitely changing the URI routes can cause you to break old clients. Consider a header like so to enforce versions:

```
Accept: application/json; version=3
```

OR use a nonstandard application header like so:

```
X-API-Version: 3
```





