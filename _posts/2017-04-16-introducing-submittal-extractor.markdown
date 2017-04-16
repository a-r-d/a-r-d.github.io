---
author: Aaron Decker
comments: true
date: 2017-04-16
layout: post
slug: introducing-submittal-extractor
title: Introducing Submittal Extractor
description: Submittal Extractor is a Saas application I have been building over the past 6 months with the help of Messer Construction Co. in Cincinnati OH.
---

[![Submittal Extractor (http://submittalextractor.com)](/images/blog/blue_trans_cropped_700.png){: .center-image }](http://submittalextractor.com)

## Building a Product

So I have been wanting to build a Saas app for some time now, and I figured the best way to do it would be to go directly to a potential customer and ask about what kind of problems they had that I could solve with software. Maybe that sounds naive, but that is what I did with Messer Construction. They told me about a problem that was pretty small in scope: it was slow and labor intensive to pull important information from architectural specification documents.

Let me explain: when a General Contractor works on a large construction project they work with an architect that will provide a specification document. These specification documents are in something called "MasterFormat" and they are often between one and five thousand pages long. There are entries in this document called "Submittals" and they need to be pulled out to keep track of because they will require action to be taken.

#### Let me give you an example of a Submittal:

```
1.3  SUBMITTALS
    A. Product Data: For each type of cold-formed steel framing product and accessory.
    B. Shop Drawings
        1. Submit shop drawings including elevations of all walls.
        2. Include layout, spacings, sizes, thicknesses, and types of cold-formed steel framing; fabrication; and fastening and anchorage details, including mechanical fasteners.
        3. Indicate reinforcing channels, opening framing, supplemental framing, strapping, bracing, bridging, splices, accessories, connection details, and attachment to adjoining work.
        4. Shop drawings shall bear stamp of Professional Engineer, registered in The State of Ohio, who performed design calculations for members and connections.
```

## Extracting The Submittals from a PDF

So after I understood what the ask was, I got to work prototyping it to see how it could be done. There are a couple of problems here:

  1. You need to get the text from the PDF file.
  2. You need to programmatically recognize and extract the "Submittal" entries from the text.
  3. You need to handle different variations on the MasterFormat spec, because apparently no two architects format these the same exact way!
  4. You need to create an way for the user to submit documents and get their output.

Ultimately the end result was that I could not be 100% accurate, but I could achieve more like 80% or 90% accuracy with 80% or 90% of documents. There was always be some crazy formatting the breaks the extractor, even though there was a spec that architects were supposed to follow.

## What is the output?

After extracting all of these submittals the goal was tabulate them into a spreadsheet so they could be easily searched. So the program is doing the follow things:

  1. Takes in a PDF
  2. Converts PDF to Text, extracts the data.
  3. Cleans up the data and spits out an Excel file.

From the Excel file a project manager can the build what is called a "Submittal Register" or a "Submittal Log". They can upload this into a project management system like Viewpoint, Prolog, Primavera P6, or ProCore.

#### To give you an idea, this is what the output looks like:

[![Submittal Extractor Example Output](/images/blog/example-output.png){: .center-image }](/images/blog/example-output.png)


## The Productized Service Offering

Unfortunately the extraction process still takes some human touch in that a user has to inspect the format of the document and choose the appropriate pattern matching parameters. I have not yet come up with a foolproof way to detect the format and automate this process. It only takes _me_ a few minutes to do, but I didn't want to expose this burdensome process to the user.

Given that issue, I decided to offer a productized service: the customer submits a document, then I run it through the system and provide the result for a flat rate fee. Otherwise, each customer would need to be trained in how to use the software and if they did not choose the appropriate parameters they would possibly not be happy with the result (which would also be bad).

Originally I built the application with a user login system thinking that users would purchase a subscription and login then perform their own extractions, but for now I have decided to focus on offering the a-la-carte document at a time service version.


## More on the User Interface

I am by no means an expert on user interfaces, which makes the productized service even better for me: I only have to build a couple of pages. The pages are:

  1. The purchase / document submission page. [Order Now Page](https://submittalextractor.com/a-la-carte)
  2. The Status page where users can download their Excel document.
  3. The receipt page.

And that is it, all of the machinery is on the backend and I have interfaces already built for the enterprise version that I am using behind the scenes to perform the extraction. Now I only have to focus on a few customer visible interfaces.


## A Generous Refund Policy

Because the formatting can be so difficult to work with, and PDF files can be corrupted or impossible to parse, I also feel strongly that it is important to offer demos and do full refunds if I could not perform the extraction well.

If I do a good job, and the customer gets what they want out of the process I would expect them to come back to have their next spec document processed. And if for some reason I can't do the work, I want to know that there is no risk to give it a try, and I won't charge them if they are not happy.


## Selling the Product

The thing I didn't understand going into this project was how difficult it would be to reach customers. I have been trying a combination of cold-emailing, and posting on forums but so far the customers I have received have been  referred though Messer Construction.

Being a software developer without experience in sales or marketing I vastly underestimated how hard the actual hard part of this venture would be: reaching customers interested in my product. This is where the real learning comes in. The product is very specific and difficult to explain and there are few competing products so potential users don't even know this type of solution exists.

And by the way, if you are reading this and you can help with software sales please get in touch (aaron@ard.ninja).



## The Endgame

In the end, does it make sense for me to try to run this product myself? It is a niche market and I don't have the resources to sell it aggressively but I can imagine it would be particularly useful packaged with bidding software or project management software. I'm interested in talking to construction software companies to try to do a partnership or to sell to directly and integrate this product into their suite of products. Again, if you know anybody and you are reading this, again, please get in touch.
