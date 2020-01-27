---
author: Aaron Decker
comments: true
date: 2020-01-24
layout: post
slug: adding-jest-to-sharepoint-framework-react-sites-in-2020
title: Adding Jest To Sharepoint Framework React Sites in 2020
description: I recently started working on a sharepoint framework react site using typescript and I wanted to add Jest tests. Here is how to do it.
---

I recently started a project where I had to work on a yeoman generated sharepoint framework react site. This is the Microsoft recommended way to create a webpart for Sharepoint Online build with React. 

To be 100% clear, [this is how the yeoman generator was installed](https://docs.microsoft.com/en-us/sharepoint/dev/spfx/set-up-your-development-environment). 

And, [this is how the generated framework was set up](https://docs.microsoft.com/en-us/sharepoint/dev/spfx/web-parts/get-started/build-a-hello-world-web-part).


## SPFX, React, TypeScript, and adding Jest + Enzyme

This SPFX generator creates a hello world set up with React, TypeScript, Gulp, and Mocha. I wanted to use Jest and Enzyme - here is my tale of how I tried to set this up and got about 90% there. 

### First, install some more things:


{% highlight plain %}
npm i --save-dev jest ts-jest @types/jest enzyme enzyme-adapter-react-16 @types/enzyme identity-obj-proxy
{% endhighlight %}

### Wire up jest in tsconfig.json

Note: I'm just showing here what changed

{% highlight json %}
{
  "compilerOptions": {
    "types": ["jest"]
  }
}
{% endhighlight %}

### Make a setupTests.ts file

In this `setupTests.ts` file, we are going to set up the enzyme adapter

{% highlight js %}
import * as Enzyme from 'enzyme'
import * as Adapter from 'enzyme-adapter-react-16'

Enzyme.configure({
  adapter: new Adapter()
})
{% endhighlight %}


### Configure Jest options in package.json

These go in `package.json`, again just showing what changed.

{% highlight json %}
{
  "jest": {
    "setupFilesAfterEnv": ["<rootDir>src/setupTests.ts"],
    "moduleFileExtensions": ["ts", "tsx", "js"],
    "transform": {
      "^.+\\.(ts|tsx)$": "ts-jest"
    },
    "testMatch": [
      "**/src/**/*.test.+(ts|tsx|js)"
    ],
    "moduleNameMapper": {
      "\\.(css|less|scs|sass)$": "identity-obj-proxy"
    },
  }
}
{% endhighlight %}

### If you want to add code coverage, here are some additional options

These also go in `package.json`

{% highlight json %}
{
  "jest": {
    "collectCoverage": true,
    "coverageReporters": [
      "json", "csv", "text", "cobertura"
    ],
    "coverageDirectory": "<rootDir>/jest",
    "reporters": ["default"],
    "coverageThreshold": {
      "global": {
        "branches": 75,
        "functions": 75,
        "lines": 75,
        "statements": 75
      }
    }
  }
}
{% endhighlight %}

Make sure to `.gitignore` the jest directory if you add this coverage config (`jest/`).

## Now you can create tests!

Here is an example test file (`src/components/example.test.tsx`). Note that I imported react and named it `.tsx` when I'm using enzyme.

{% highlight js %}
import * as React from 'react'
import { shallow } from "enzyme";
import { ExampleComponent } from './example.txt

describe('ExampleComponent test', () => {
  it('renders OK', () => {
    const wrapper = shallow(<ExampleComponent />)
    console.log(wrapper.debug())
  })
})
{% endhighlight %}

## But wait, there is an issue with microsoft fabric!

I tried testing a React file where I imported the `Text` component from `office-ui-fabric-react` and ran up against this issue. 

It seems like these files are not being transformed and jest needs them transformed to run them. 

{% highlight plain %}
Jest encountered an unexpected token

This usually means that you are trying to import a file which Jest cannot parse, e.g. it's not plain JavaScript.

By default, if Jest sees a Babel config, it will use that to transform your files, ignoring "node_modules".

Here's what you can do:
  • If you need a custom transformation specify a "transform" option in your config.
  • If you simply want to mock your non-JS modules (e.g. binary assets) you can stub them out with the "moduleNameMapper" config option.

You'll find more details and examples of these config options in the docs:
https://jestjs.io/docs/en/configuration.html
Details:

C:\projects\MYPROJECT\node_modules\office-ui-fabric-react\lib\Text.js:1
export * from './components/Text/index';
^^^^^^

SyntaxError: Unexpected token export
{% endhighlight %}

For the record these are the various versions of things I'm using:

{% highlight plain %}
"jest": "^25.1.0",
"ts-jest": "^25.0.0",
"typescript": "^3.7.4",
"@microsoft/sp-office-ui-fabric-core": "1.10.0",
"react": "^16.12.0",
{% endhighlight %}

## Finally found the issue

I googled something like "office-ui-fabric-react jest failing export * from" and I was eventually let to [this note in the documentation for fabric that notes they have multiple outputs you can switch between](https://github.com/OfficeDev/office-ui-fabric-react/blob/master/6.0_RELEASE_NOTES.md#lib-commonjs
).  

Sure enough for jest you need to use the `commonJs` variant, and fixing everything was as simple adding this to my jest config:

{% highlight plain %}
  moduleNameMapper: {
    'office-ui-fabric-react/lib/(.*)$': 'office-ui-fabric-react/lib-commonjs/$1'
  },
{% endhighlight %}

## Final note

There is a pretty good sample repo here:
[https://github.com/SharePoint/sp-dev-fx-webparts/tree/master/samples/react-jest-testing](https://github.com/SharePoint/sp-dev-fx-webparts/tree/master/samples/react-jest-testing)

If you want to use that to get started (and then also use Fabric) you just need to make sure to add the module mapper I listed above. That should cover it (at least in January 2020).

