---
author: Aaron Decker
comments: false
date: 2016-02-02 02:50:42+00:00
layout: post
link: http://ard.ninja/blog/git-tip-replace-master-branch-fresh-copy-upstream/
slug: git-tip-replace-master-branch-fresh-copy-upstream
title: 'git tip: replace your master branch with a fresh copy from upstream'
wordpress_id: 367
categories:
- git
---

Sometimes for whatever reason you screw up and get your local master branch into a nasty inconsistent state. Maybe it was an accidental merge or accidental commits but you just want to start over. Here is how to replace your local master branch with a fresh copy from upstream.

{% highlight bash %}
# you cannot delete the branch you are on, so move to something else.
git checkout           

# delete local master (if not fully merged do ‘-D’. In this case I did have to use capital D)
git branch -d master          

# get changes from upstream master           
git fetch upstream master                

# make a fresh master branch
git checkout -b master upstream/master   

# force push to origin, it will blow away your old master
git push origin master -f               
{% endhighlight %}

There are easier ways to do this, but conceptually this is, in my opinion, easy to follow and it cleans up your remote as well (if you accidentally pushed a dirty branch).
