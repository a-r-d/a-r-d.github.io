---
author: Aaron Decker
comments: true
date: 2017-03-04
layout: post
slug: when-to-use-object-pooling-in-java
title: When to use Object Pooling in Java
description: When does it make sense to use object pools in Java? Are connection pools the only object pools you should use?
---

![photo by eric wesseling](/images/blog/erics/DSC_7772.jpg){: .center-image }
  _Photo By [Eric Wesseling](https://www.instagram.com/ericwess/)_

## What are object pools?

Object pools are a design pattern that allows re-use of expensive objects. The point of an object pool is to avoid re-initializing expensive objects. Typically this works by creating an array to hold your objects then initializing, say 10 of them right up front. When you need one of these objects (like a database connection), you just grab it from the pool (_you check it out like a book at the library_) and when you are done you give it back.

This technique used to be much more common than it is now because machines used to have much less memory and in some languages the creation of objects was expensive. In Java this is no longer the case and you should almost always NOT use object pools because it is very cheap to initialize most objects.


## What is wrong with object pools?

The problem with object pools in modern Java apps is twofold: firstly objects are generally cheap to create and clean up negating the benefit of this design pattern, and secondly, it increases the old generation heap usage in way that the memory cannot ever be freed, thus increasing memory pressure and causing smaller more frequent garbage collection cycles (leading to more GC pauses and CPU usage).

There are also some more general issues with object pools (not just for Java apps). When you have an object pool you must make sure that two threads cannot use the same object the pool simultaneously, so now you must maintain synchronization. As we all know synchronization can be expensive and object pool access must synchronized across threads.

Finally, the last big problem with object pools is managing them alone requires some complexity and overhead. Even if you use a third part library like [__c3p0__](http://www.mchange.com/projects/c3p0/index.html) you will need to configure it correctly. As an example, an issue like this recently occurred at work where a project I was working on was having some performance issues. We realized we had copied some code from another team that created a connection pool with a very small number of connections and our application was having contention issues over getting connections from the pool. It took us a while to diagnose the issue, then locate this configuration parameter and bump it up.


## OK, when should I use them in Java?

Despite the downsides there actually are a couple of great places to use object pools. Some objects are long living and expensive to create, and these are great candidates for connection pooling. Database connections fall into this category and you will almost always see applications still using object pools to contain database connections for re-use.

__Here is a short of list of good objects to pool:__

 1. __JDBC connections__ in general (as mentioned already).
 2. __Threads__: Threads are expensive to create so Threadpools make a lot of sense
 3. __Large arrays__: they can take a while to allocate since memory is reserved when you size them up front so it often makes sense the keep them around if you can spare the heap space.
 4. __Random + SecureRandom__ objects - these are expensive objects to create. SecureRandom grabs a list of Security Providers in the constructor, and the both must be seeded as well.
 5. __DNS lookups__ in general are slow and should be cached. Objects involved in this can be pooled.
 6. Various __Encoders, Decoders, Serializers, Deserializers__. A lot of these are either expensive to create or free because they may call some native code via JNI. Zip Encoders for example are expensive to GC for this reason.


## What else can I use?

Actually, for some of these scenarios, like encoders and decoders for example it makes a lot more sense to use ThreadLocal variables. This will allow you do less frequent creation of these objects while also avoiding the performance hit you take around having to synchronize thread pools. Most of these objects are also inherently not thread safe and in recent versions of Java calling ThreadLocal.get() is very fast so it makes sense to use this tool when you can.

It used to be that you had to worry about using ThreadLocals due issues around memory not getting freed when deploying and undeploying web app containers but this is a less common practice these days. You could end up with the infamous ```java.lang.OutOfMemoryError: PermGen space ```. But, with tools like Docker becoming much more popular it is no longer as common to run servlet containers as shared resources. It makes a lot more sense to use embedded Tomcat or embedded Jetty and run apps in stand-alone fashion. Check out the [2nd answer on this stack overflow](http://stackoverflow.com/questions/817856/when-and-how-should-i-use-a-threadlocal-variable) for a discussion of these concerns.


## A quick example of using a connection pool in Java

In Java there are tons of great libraries that manage connection pools for you. In this example I'll show  using [__c3p0__](http://www.mchange.com/projects/c3p0/index.html). In this example I am initializing a new connection pool, setting the connection settings for Postgres, and then configuring the pool size. Finally, after initializing the pool I grab a connection from the pool.

{% highlight java %}
import java.sql.Connection;

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class CnxTest {

	public static ComboPooledDataSource cxnPool = new ComboPooledDataSource();

	public static void main(String[] args) throws Exception {

		// config for local PG SQL instance
		cxnPool.setDriverClass( "org.postgresql.Driver" );
		cxnPool.setJdbcUrl( "jdbc:postgresql://localhost/demos" );
		cxnPool.setUser("postgres");
		cxnPool.setPassword("password");

		System.out.println("Configuring the pool");
		// set up pool size.
		cxnPool.setMinPoolSize(5);
		cxnPool.setAcquireIncrement(5);
		cxnPool.setMaxPoolSize(20);

		// actually using the pool:
		Connection cxn = cxnPool.getConnection();

		System.out.println("DOne!");
	}

}
{% endhighlight %}

Here are the libraries I used to build this:

{% highlight xml %}
<dependencies>
	<dependency>
		<groupId>c3p0</groupId>
		<artifactId>c3p0</artifactId>
		<version>0.9.1.2</version>
	</dependency>
	<!-- https://mvnrepository.com/artifact/org.postgresql/postgresql -->
	<dependency>
		<groupId>org.postgresql</groupId>
		<artifactId>postgresql</artifactId>
		<version>9.4.1212</version>
	</dependency>
</dependencies>
{% endhighlight %}
