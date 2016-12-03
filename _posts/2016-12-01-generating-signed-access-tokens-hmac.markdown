---
author: Aaron Decker
comments: false
date: 2016-12-01
layout: post
link: http://ard.ninja/blog/generating-signed-access-tokens-hmac/
slug: generating-signed-access-tokens-hmac
title: Generating Signed Access Tokens (HMAC)
description: I talk about what a hashed message authentication code is, and I give an example in javascript
---

### Generating Signed Access Tokens

Building simple access tokens a very common task when building an API. It is also a good topic for an interview question. In addition to a general authentication token, you may need to generate any number of other tokens including tokens for password resets, email verifications or api keys. A very interesting kind of access token is on that stores data that signed with a secret key. This actually allows you pass around data that cannot be tampered with and it keeps you from having to store the token in the database.

### Hash Based Message Authentication

What I have just described above is actually something called HMAC - hash message authentication code. It is a very simple algorithm which we will implement below.

### How Does It Work?

In simple terms you have a secret key that you store on your server, some data that you want to build into the token and a signature created from these parts. Later, you will decode the data and signature and try to rebuild the token from these parts with your secret key. If it matches, your access token is valid. The coolest thing is that you can store an expiration time, a user id, an email - basically any piece of extra data on your token. Again, all of this is achieved securely without any database required.

### THE SECRET KEY

It can be as simple as a random string in a config file like so:

```
var secret = 'skKaTT2dJRXSH3sMxkZ2aWY95jfTeX';  
```

Making it very very long is pointless because any HMAC algorithm will shorten it to a specific length.

### BUILDING THE TOKEN DATA

In this example, we are going to build the body as a JSON object, stringify it, and encode it as base64. This way it should be safe to pass as a URL parameter if need be.

{% highlight javascript %}
var data = {  
    expires: (new Date()).getTime() + 1000*60*60*24,
    userId: EjuKNCcMjUaxk
};

// encode it as base64 so it is HTTP safe.
var tokendata = atob(JSON.stringify(data));  
{% endhighlight %}

### BUILDING THE SIGNATURE

This is the root the work - the HMAC algorithm. It is essentially a function that takes 3 arguments: the key, the data, and the hashing algorithm you will use. There actually a ton of very nice javascript implementations here. And if you read the article it states that it is sufficient to do something like var sig = sha1(key + sha1(key + message)) and the key padding is not critical to security. Needless to say, we will not re-implement HMAC to RFC spec mainly because it is a bit of a pain to do with browser-based javascript.

### TESTING IT OUT

[Here is a jsbin where you can see the HMAC system in action](http://jsbin.com/jaleyewudo/1/embed?html,js,console). We generate a signed token that stores some information and then later we are able to parse the information back out of the token. In this way you can create that tokens that have expiration dates and pass other information all without using a database. Make sure not to store any secret information on the message as it is still visible, just not possible to tamper with!


### Full code, copy of what is on jsbin

Here is a copy of the HTML + JS that you need to see this working, in case the JSBin link did not work for whatver reason

{% highlight html %}
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>JS Bin</title>
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/core-min.js"></script>
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/hmac-sha1.js"></script>
</head>
<body>
</body>
{% endhighlight %}

{% highlight javascript %}
// secret HMAC key
var secret = 'skKaTT2dJRXSH3sMxkZ2aWY95jfTeX';

var data = {
	expires: (new Date()).getTime() + 1000*60*60*24,
    userId: 'EjuKNCcMjUaxk',
    randomData: 'hello'
};
// encode it as base64 so it is HTTP safe.
function createTokenData(data) {
  return btoa(JSON.stringify(data));
}
var tokendata64 = createTokenData(data);
console.log('Token Data: ', data, tokendata64);

// note that I have included SHA1 HMAC creator from here:
// http://code.google.com/p/crypto-js/
function hmac_sha1(key, message) {
  //console.log('Creating HMAC for message: ' + message);
  return CryptoJS.HmacSHA1(message, key).toString();
}

// this takes strings
console.log('Computing HMAC...');
var signature = hmac_sha1(secret, tokendata64);
console.log('The signature: ', signature);

// token delimeter will be a tilda. It should be safe in a GET query param
var accesstoken = signature + '~' + tokendata64;
console.log('Our access token: ', accesstoken);

// We will pull the data backout into a javascript object
// and check to see if the signature is valid!
function parseToken(token, secretkey){
  // split by token delimeter
  var parts = token.split('~');
  var signature = parts[0];
  var data = parts[1];

  var verifysig = hmac_sha1(secretkey, data);
  var tokenInformation = {
    data: JSON.parse(atob(data)),
    signature: signature,
    valid: false
  };
  if(signature === verifysig) {
    tokenInformation.valid = true;
  }
  return tokenInformation;
}

var parsed = parseToken(accesstoken, secret);
console.log('Parsed token Data: ', parsed);
if(parsed.valid) {
  console.log('Parsed token has a valid signature!');
}
{% endhighlight %}
