---
author: Aaron Decker
comments: true
date: 2018-08-27
layout: post
slug: pros-and-cons-of-various-secret-systems
title: The Pros and Cons of Various Secret Storage Systems
description: I talk pros and cons of various systems of how to get your secrets deployed to prod running your server!
---

![Photo by Zbysiu Rodak on Unsplash](/images/blog/rodack-unsplash.jpg){: .center-image }
_Photo by Zbysiu Rodak on Unsplash_{: .center-image }

How do you deploy your secrets to your production server? There used to be many
ways to do this, and now that most people are deploying using Docker containers
and various orchestration systems there are even more!

## Define "secret"

For the purpose of this article I am talking about configuration info like database
passwords and API tokens that a server needs to run.
These may include certificates as well but you should assume
I am just talking about data that can be stored as text.


## Commit them to git (put them in the code)

OK we are starting off with a bad one.
For reasons that are maybe obvious committing your application secrets into the
git code base of the app is a bad idea. However it is the least complicated option
and a lot of people end up doing this because on the face of it you probably trust your
server, your machine, and your code repo to be secure. The big downside here is that now
every copy of the repo has all of the secrets (probably in plain text) and they
are buried in the history of the repo even if you change them.

It becomes an increasingly dangerous option the more people have access
to the code and the servers running the code.


## Manually deploy them to a specified spot

A few times I have seen a system that worked like this: your application looks for
config files in the home folder (or somewhere similar) on startup, and
when you deploy your application to new servers or change secrets, you must
manually copy the new secret config file up to each server.

Problems with this:
 1. Probably only works with VMs that persist
 2. Creates a lot of work every time you change a secret
 3. How do you make sure they are in sink across your production servers?
 4. Where do your store the master copy of the config file? On someone's personal machine?

The good thing about this is it's probably much more secure than keeping
the secrets in the git repo with the code. As long as you make sure permissions
are set correctly on the server you can probably make it so that secrets are not
compromised even if someone gains shell access to the server as a non-root user.


## Use a centralized (or decentralized) config server

It is hard to talk about this one succinctly because there are so many implementations
of centralized configuration servers. I have seen horrible implementations and great
ones.

First, I will tell you about a bad one. I have seen this implemented in such
a way that write access to a web portal where you could enter config info
was secured via LDAP SSO for which any domain account apparently worked, but read access
appeared to be wide open and secrets were stored in plain text along with all of the
other config info. Also if this server went down your application would not start.

A good example of this would be Spring Cloud Config server where you can configure
encryption and various backing stores. Another option I have heard of is
Hashicorp Vault, but admittedly I have never used it.

With any config server based solution you have a few concerns:
 1. How does config server securely identify a your server?
 2. Is it OK to transmit this stuff over the network?
 3. How complex is the code to retrieve the secrets from the server? What happens when it fails, or the secrets update, ect...?
 4. How does the config server store the secrets?

Because of all of the added complexity I don't really like the idea of using a centralized
config server to store secrets (with the exception of things like the  
AWS Secret Management Service I mention below because that removes a huge maintenance
burden).


## Commit encrypted secrets to git, supply the decrypt key to the server

This is another option that I've seen used a lot which adds a bit of security
around using git as a storage mechanism.

The general idea is that you somehow encrypt the secrets before your commit to git,
and just keep encrypted values in the application config files. Then, when the application
is running, the only thing that needs to be injected into it is the decryption key.

This is a little bit complicated because your application needs to know how use
some sort of decryption library but aside from that you get a lot of flexibility
because you only have one secret key you need to inject to the production runtime now.


## Bake secrets into the docker image for your application

This is possibly the worst option, or maybe equally as bad as committing them
directly to git (unencrypted). The reason being that in a lot of installs of
docker servers there is no authentication required. Even if there is a lot of the time
only publishing images requires any permissions and everything is readable.

Even if this is not the case and your docker image server is highly secure,
you have the same problem with code repos: a lot of people and servers must
have access to the docker
images if you are building anything of any meaningful size.


## Deploy to orchestration with secret management (e.g. kubernetes)

This is actually my favorite option because I like using kubernetes, and having
kubernetes able to store and mount secrets into pods is very nice.

If you are not familiar, kubernetes is a container orchestration system. You
can deploy a docker image to kubernetes and specify how many copies you want
running and how you want it to scale. Also, in the deployment you can define
volumes you want to mount to the containers. Kubernetes has an API that you can
upload secrets to and then reference to be mounted into containers.

Docker swarm secrets work in a similar manner. The downside this method
is that you still need a way to store
the secrets before your put them into the orchestration system. And you
need to deal with consuming the secrets via either a config file
mounted to the filesystem or environmental variables.

One way of storing your secrets (to be later injected to pods via kubernetes api)
is by storing them encrypted in git using something like ```git-crypt```.


## Inject them using your build system

This is either OK or bad depending on exactly how you implement it. If your build
system can store secrets in a safe manner and it is useful for your workflow it may be a
nice idea. Not every build system has fine grained permissions or a system that allows
you to encrypt secret data.

The main issue is that the build context is probably not when you need the secrets. It
would work great if you are using ansible to deploy to VMs and you wanted to copy secrets up
to them as a deploy step, but if you are deploying containers like most people are, it is not that helpful
to have secrets at build time but not at runtime.


## AWS Secrets Manager, Azure Key Vault or Google Cloud Key Management

This is an option if you are running on a large cloud service provider. The one
I have researched is [AWS Secrets Manager (link to a youtube intro)](https://www.youtube.com/watch?v=Y3Gn_iP3FlE)
. You can store key/value pairs of secrets that you create in the AWS dashboard, and
there are integrations in the AWS SDKs to get them out into your application. You
decide what IAM roles can get your secrets.

I actually like this option a lot if it's something you can do in your org. The downside
is the tight coupling between your code and your cloud provider, but depending on how long
lived your service may be, this is not necessarily a problem.

When people mention this as a reason not to use services like these
it makes me think about the argument for using an ORM "_because you may switch
databases_". I think most people can attest that _you don't just switch databases_ lightly,
and if you do, you probably did it to change the data structure and at that point
your ORM code is trash anyway. To some degree I think the same argument applies about
switching cloud providers. It is a huge amount of work, the implementation of the
secrets system is the least of your worries.
