---
templateKey: article-page
author: Aaron Decker
title: Adding Jest To Sharepoint Framework React Sites in 2020
slug: adding-jest-to-sharepoint-framework-react-sites-in-2020
date: 2020-01-23T18:51:33.884Z
cover: /img/blog/logo/react-cover-logo.png
tags:
  - react
  - spfx
  - jest
  - typescript
meta_title: Adding Jest To Sharepoint Framework React Sites in 2020
meta_description: >-
  I recently started working on a sharepoint framework react site using typescript and I wanted to add Jest tests. Here is how to do it.
---

I recently started a project where I had to work on a yeoman generated sharepoint framework react site. This is the Microsoft recommended way to create a webpart for Sharepoint Online build with React. 

To be 100% clear, [this is how the yeoman generator was installed](https://docs.microsoft.com/en-us/sharepoint/dev/spfx/set-up-your-development-environment). 

And, [this is how the generated framework was set up](https://docs.microsoft.com/en-us/sharepoint/dev/spfx/web-parts/get-started/build-a-hello-world-web-part).


## SPFX, React, TypeScript, and adding Jest + Enzyme

This SPFX generator creates a hello world set up with React, TypeScript, Gulp, and Mocha. I wanted to use Jest and Enzyme - here is my tale of how I tried to set this up and got about 90% there. 

### First, install some more things:

```bash
npm i --save-dev jest ts-jest @types/jest enzyme enzyme-adapter-react-16 @types/enzyme identity-obj-proxy
```

### Wire up jest in tsconfig.json

Note: I'm just showing here what changed

```json
{
  "compilerOptions": {
    "types": ["jest"]
  }
}

```

### Make a setupTests.ts file

In this `setupTests.ts` file, we are going to set up the enzyme adapter

```javascript
import * as Enzyme from 'enzyme'
import * as Adapter from 'enzyme-adapter-react-16'

Enzyme.configure({
  adapter: new Adapter()
})
```

### Configure Jest options in package.json

These go in `package.json`, again just showing what changed.

```json
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

```

### If you want to add code coverage, here are some additional options

These also go in `package.json`

```json
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
```

Make sure to `.gitignore` the jest directory if you add this coverage config (`jest/`).

## Now you can create tests!

Here is an example test file (`src/components/example.test.tsx`). Note that I imported react and named it `.tsx` when I'm using enzyme.

```javascript
import * as React from 'react'
import { shallow } from "enzyme";
import { ExampleComponent } from './example.txt

describe('ExampleComponent test', () => {
  it('renders OK', () => {
    const wrapper = shallow(<ExampleComponent />)
    console.log(wrapper.debug())
  })
})
```

## But wait, there is an issue with microsoft fabric!

I tried testing a React file where I imported the `Text` component from `office-ui-fabric-react` and ran up against this issue. 

It seems like these files are not being transformed and jest needs them transformed to run them. 

```plain
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
```

Unfortunately I had no luck. I was using these versions:

```json
"jest": "^25.1.0",
"ts-jest": "^25.0.0",
"typescript": "^3.7.4",
"@microsoft/sp-office-ui-fabric-core": "1.10.0",
"react": "^16.12.0",
```

## Stumped...

I messed with it for hours and could not untangle the mess. 

- I tried to to explicitly transform all `.js` and `.jsx` files with `babel-jest`. 
- I tried the `ts-jest` preset [called "js-with-ts"](https://kulshekhar.github.io/ts-jest/user/config/). 
- I tried to use `transformIgnorePatterns` on `node_modules/office-ui-fabric-react`.

A complicating factor is I think all of this stuff is written for unix systems and I was doing this on a Windows system. 

Things could be broken for all kind of reasons, but honestly I think that it is just plain complicated to wire up so many interlinked components with so many transformations going on. What code is actually running where? What needs to be transformed into what in order to run? It shouldn't be this hard... but it is. 

So close but so far away! Guess I will go with the mocha setup the yeoman generator set up. 