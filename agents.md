Repository Overview

This repository contains the source for a personal blog and portfolio website built with Jekyll. The README describes it as a fork of Jekyll Now—a template that simplifies setting up a blog on GitHub Pages
. The site’s configuration, including name, description, and social links, resides in _config.yml

.

Structure

    Content

        _posts/ – Markdown articles with Jekyll front‑matter, e.g. the Android article from 2014

and recent posts like the trend reversal piece from 2025

.

_drafts/ – Unpublished or work-in-progress posts.

index.html – Main landing page with background details and consulting info

    .

    blog/index.html – Lists blog posts using a Masonry-style grid.

    legal.html, fear.html, and 404.md – Standalone pages.

Layout and Styling

    _layouts/ – HTML templates; default.html defines the site header, navigation, and includes common elements

.

_includes/ – Reusable snippets, such as a contact form and a Mailchimp signup form
.
The contact form’s behavior is handled by a jQuery script posting to an external API

.

style.scss and _sass/ – SCSS stylesheets. There’s a small TODO comment about aligning the navigation vertically

    .

Extras

    algos/kama-crossover.py – A QuantConnect algorithm implementing a moving-average crossover strategy in Python

        .

        canvas-spritesheet-demo/ – An HTML/JS demo showing sprite animation on a canvas.

        research-notebooks/ – HTML exports of research notebooks.

Development and Deployment

The README explains how to customize _config.yml and run jekyll serve for local development

. When files are pushed to GitHub, GitHub Pages builds the site automatically.

There is no package.json or Gemfile, so automated test commands fail (running npm test errors with ENOENT and pytest reports no tests)

.

Next Steps

    Learn the basics of Jekyll’s Liquid templating and front‑matter. This will help you customize _layouts and create new posts.

    Explore SCSS if you plan to adjust the site’s look and feel.

    Investigate GitHub Pages’ build process if you need custom plugins or want to automate deploys.

Overall, the repo is a fairly typical Jekyll-based blog with some personal projects included for reference.
