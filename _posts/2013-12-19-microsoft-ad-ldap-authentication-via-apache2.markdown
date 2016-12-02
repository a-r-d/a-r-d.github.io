---
author: Aaron Decker
comments: true
date: 2013-12-19 22:58:50+00:00
layout: post
link: http://ard.ninja/blog/microsoft-ad-ldap-authentication-via-apache2/
slug: microsoft-ad-ldap-authentication-via-apache2
title: Microsoft AD LDAP authentication via Apache2
wordpress_id: 244
categories:
- Active Directory
- apache2
tags:
- mod_proxy
- php
---

Previously I looked at how you can use Apache2 as a reverse proxy with SSL to expose applications inside of your firewall securely from one endpoint with a single SSL cert. Most corporate IT networks will be using a Windows domain controller so next you may be wondering how to secure your intranet pages using Microsoft AD LDAP authentication via Apache2.

It is actually quite do-able although the config takes some effort. First you will want to enable the module "mod_authnz_ldap". If using ubunutu you can do:

```
sudo a2enmod authnz_ldap
```

Now that that is done lets take stock your your AD Domain. Let's say that your company is called "Mr Waffles" and your domain was called "MRWAFFLES" and then the FQDN was set up as mrwaffles.ad.com on your Active Directory server. This means your base DN is likely "DC=mrwaffles, DC=ad, DC=com". Okay, now your users are perhaps stored under Organization Unit "Users" ("OU=Users"). So this would make the search container: "OU=Users,DC=mrwaffles, DC=ad, DC=com". To Recap:

```
Domain: MRWAFFLES
FQDN: mrwaffles.ad.com
Base Dn: "DC=mrwaffles,DC=ad,DC=com"
User container: "OU=Users,DC=mrwaffles,DC=ad,DC=com"
```


Alright, now that we know what our AD Server looks like we can continue. Personally I am using this for a reverse proxy server so I have a proxy pass in my Location tag. But you can ignore this if you like. Before I show you what you came for let me explain some things:

  * mod_authnz_ldap uses a user to bind that is NOT the one logging in. Create a user with read privs on AD for this purpose. I called mine "authuser" and set a password of "authuserpass".


  * For the authuser - make sure to put the domain in front of the name for the bind!!! (see AuthLDAPBindDN below)


  * The "?sAMAccountName?sub?(objectClass=\*)" is the search query and is absolutely required. I can confirm this works on win2k12 AD domain controller


  * You can filter on groups, I just did any user.




```
Order deny,allow
Deny from All

AuthBasicProvider ldap
AuthType Basic
AuthName "MR Waffles Network Auth Required"

AuthzLDAPAuthoritative off
AuthLDAPURL "ldap://domain-controller-ip-here:389/ou=Users,dc=mrwaffles,dc=ad,dc=com?sAMAccountName?sub?(objectClass=*)"    

AuthLDAPBindDN "mrwaffles\\authuser"
AuthLDAPBindPassword "authuserpass"

Require valid-user
Satisfy any

ProxyPass  http://internal-ip-here/
ProxyPassReverse  http://internal-ip-here/
```

One more note. This is just basic auth, not form based so it has some downsides of course. Also note when you login you just put in username and pass, not domain prefix, not email, just username.

You may also be interested in see how you do this with PHP. First install the module you need:

```
apt-get install php5-ldap
```

An equivalent login would be:

{% highlight javascript %}

function authAD( $usr, $pass ){
	global $message;
	$ad = "YOUR DOMAIN CONTROLLER IP";
	$cxn = ldap_connect($ad);
	$domain = "YOUR DOMAIN\\";

	if( $usr == "" || $pass == "" ){
	    $message = "username / pass not set";
	    return false;
	}
	$ldap_usr = $domain."".$usr;
	$ldap_pass = $pass;
	$bind = ldap_bind($cxn, $ldap_usr, $ldap_pass);

	if($bind){
            return true;
	} else {
            $message =  "Authentication failed";
            return false;
	}
}

{% endhighlight %}


As you can see it is waaaaay simple with PHP. They are just doing a simple bind.
