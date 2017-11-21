---
author: Aaron Decker
comments: true
date: 2017-11-19
layout: post
slug: react-native-android-app-as-a-module
title: React Native Android app as a Module
description: I talk about how I used React Native in Android as a module that was part of a larger Android app
---

![kubernetes](/images/blog/react-native.jpg){: .center-image }

## Can you embed React Native into larger native Android app

The answer is yes. It gets more complicated if you need to ship your React Native app
component as just part of a larger application and have to deliver as only an AAR file, but
still the answer is yes. The thing that is lacking is a good guide on how to do this.

## Background info and application structure.

So I work on a team that ships a small component of a larger mobile application. In fact, there
other teams shipping other components too. The structure looks like this:

{% highlight plain %}
*Big Native Android Application*
  | --> lots of native code directly in the main app codebase.
  |
  ----> Components from team A for feature X
  |
  ----> Components from team B for feature Y
  |
  ----> SDK from team C used by all other components
{% endhighlight %}


If my team (Team A) wanted to be able to use React Native, we had to continue to ship our
components exactly as before, via an AAR file. It is possible but there are some things to consider.

## Starting from the React Native tutorial

I am going to start with the [React Native tutorial](https://facebook.github.io/react-native/docs/integration-with-existing-apps.html) and correct things that will trip you up if you try this. There are 500 open issues and almost 200 open PRs on React Native as I write this. You will run into trouble, so here are things I encountered.


Firstly, I did this in November of 2017. I found out that it is very important to lock down all of your dependency versions for everything. Here is what my package.json looks like:

{% highlight plain %}
{
  "dependencies": {
    "react": "16.1.1",
    "react-native": "0.50.3"
  },
  "scripts": {
    "start": "node node_modules/react-native/local-cli/cli.js start",
    "bundle-android": "react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/myapp/src/main/assets/index.android.bundle --assets-dest android/myapp/src/main/res"
  }
}
{% endhighlight %}



## Lock your dependencies in your Android project.

A very serious error is made in the tutorial:

{% highlight plain %}
dependencies {
    ...
    compile "com.facebook.react:react-native:+" // From node_modules (DONT DO THIS!!!!)
}
{% endhighlight %}


Seriously, don't do the "+". Lock it to a version. A much smarter thing to do is to lock it to version ``` 0.50.3 ```, which is the version I have used in the package.json file.

Why lock it down? I will tell you why. It is because if you misidentify the path to the node modules in the line
in the maven config you will have major compilation issues. I did this exact thing because I made a directory inside of the "android" directory in my project.  Why does this break things? Well, it is because in Maven Central there is a very old version of
React Native published (version 0.20.something) which is going to not compile. This is not easy to discover unless you list our the dependencies, because reffing to ```node_modules``` directory wrong will just fail silently!

{% highlight plain %}
allprojects {
    repositories {
        maven {
            // This is line that refs node modules I am talking about. If you
            // have compile errors, you probably need another "../" in there somewhere.
            url "$rootDir/node_modules/react-native/android"
        }
    }
    ...
}
{% endhighlight %}


## Setting up your React Native project as a module.

Actually this part went smoothly. I created a new module under my project and moved the
code that loads my bundle and instantiates the React Native component  into this module.
I think made the main runnable part of the app consume the module. The module produces and AAR file
that include the activity that starts the React Native component as well as my bundled assets. You
may have some trouble making sure that the javascript code bundle is included in the
assets but this can be fixed with some entries in the gradle build file.


## Publish React Native to your maven instance for your Apps team.

The goal is to be able to seamlessly hand off your components to your apps team so they
can consume your project just like any other. Well in this case your apps team
must now somehow consume the React Native android AAR file (version 0.50.3 was about 2.3 mb), which is a dependency of the
AAR file you will ship.

[React Native is not published to Maven Central anymore](https://github.com/facebook/react-native/issues/13094). So you need to get them this exact library version.
I had trouble trying to compile the dependencies into my module, and you probably wouldn't want to do that anyway
just in case another team is using React Native. My solution was to publish the React Native android
library to our internal Maven repo so that the apps team could just pick that up automatically.


## Testing it out on a device.

Create a new project, then consume your published AAR module and try to instantiate the react activity.
Just make sure to reference the React Native library in some way so that the one dependency will load.

I had some trouble testing the application on actual device, however. I ended up making some modifications to my ```build.gradle``` file
that had to do with making different APKs for different processor architecture. But I think the most important
part of is to include this ```react.gradle``` file from node modules.

{% highlight plain %}

apply from "../../node_modules/react-native/react.gradle"

{% endhighlight %}
