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

