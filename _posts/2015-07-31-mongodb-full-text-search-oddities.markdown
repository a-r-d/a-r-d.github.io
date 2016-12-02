---
author: a-r-d
comments: false
date: 2015-07-31 01:39:05+00:00
layout: post
link: http://ard.ninja/blog/mongodb-full-text-search-oddities/
slug: mongodb-full-text-search-oddities
title: MongoDB Full-text Search Default Oddities
wordpress_id: 324
categories:
- mongodb
---

### MongoDB for full-text search on 300k items


Recently I decided to use MongoDB's full-text search indexing feature for a dataset of about 300k products where I indexed the name of each item. On average I would say that the name fields were 200 to 300 chars and primarily simple english text. Overall I was very very impressed with the performance of MongoDB for this application - all of my test queries were easily sub-second on an EC2 t2.medium instance (which is 4 gb memory and 2 vCPUs at time of writing). 



### Oddly, MongoDB does 'OR' on multi-word queries



So there are a few oddities in the default options when it comes to MongoDB fulltext search. First, the way you specify which fields on your collection to index is different in that there can only be one full text index on each collection. So while you can index multiple fields, there is only one index you can search on per collection. 

[javascript]
// I am using Mongoose with Node
// example index:
MongooseModelToIndex.index({ name: 'text' });
[/javascript]

As eluded to in the title of this section by default when search on the text index of a collection it will do an OR on each word so if you search 'Robots are cool' you will probably just get a bunch of results for 'cool' on the first few records. The way around this is to take into account textScore and sort on this:

[javascript]
// Again, I'm using Mongoose with Node
MongooseModel.find({'$text': {'$search': keyword}},{score: {$meta: "textScore"}}).limit(limit).sort({score: {$meta: "textScore"}}).exec(function(err, data) {
    return cb(err, data);
});
[/javascript]

Anyways, that's all. Just wanted to record this peculiarity. 

