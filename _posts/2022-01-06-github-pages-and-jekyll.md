---
layout: post
author: thomas
canonical_url: https://aista.com/blog/github-pages-and-jekyll/
---

Once every year I force myself to learn something completely new. Over the years this has resulted in
that I've got dozens of hobbies, such as playing 5 music instruments, dabbling with acrylics, being
quite capable of creating art with cheramics, etc. This year I started early, and I focused on
[Jekyll](https://jekyllrb.com/), and I am seriously impressed so far. To explain why, let me
give you some facts about this website.

1. It's hosted 100% free by GitHub as a [GitHub Page](https://pages.github.com/).
2. I spent no more than 5 minutes setting up a [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) for it.
3. It's exclusively served as _static content_. No databases, no server side rendering, no CGI. Pure old fashion static HTML, JavaScript, and CSS.
4. It's _blistering fast_ due to being served by one of the largest server infrastructures on the planet, GitHub's infrastructure of course.
5. Each individual page scores 70-80 percent on all SEO metrics.
6. All my content is managed using Git in a [GitHub repository](https://github.com/polterguy/polterguy.github.io).

Basically, Jekyll and GitHub pages combined seems to me to be one of those odd ball things, so weird in nature,
yet still so amazing, it becomes almost impossible to ignore. Managing my website with zero credit card
requirements, using nothing but Git as my _"CMS"_, never having to care about DOS attacks, intrusion attempts,
or any other moving parts, makes my life so much easier it's simply impossible to ignore. And Jekyll you might
ask? Ohhh my God what a spectacular tool! Simply amazing! It kind of works like a CI pipeline on GitHub's
servers, building my static content on every push towards my site's master branch, re-deploying the static
content once the process is done. I freakin' adore the thing to be honest with you!

* Jekyll allows me to blog using Git as my _"database"_.
* Jekyll allows me to create my own navigation, exactly as I want it to.
* Jekyll gives me 100% control over every single HTML tag rendered on the site.
* Jekyll allows me to process logic during the _"build"_ of my website, allowing me to have logic conditionally rendering my HTML, giving me multiple layouts on different parts of the site.
* Jekyll is simply amazing!

I started on Sunday with Jekyll, today it's Thursday. In 5 days I've created a completely
[new theme for Jekyll](https://github.com/polterguy/aista-jekyll) from scratch, implemented very
high quality SEO traits for the site, gone through the entire hierarchy of the site and cleaned up most
of the documentation, implemented blogging on the site, and basically increased the quality of Magic's
documentation parts probably by probably at least one order of magnitude. And my only cost was my time.
Hence, I want to share some love with Jekyll and GitHub, and therefor I write this post. Try it out if you've got
something you need to publish. If you're slightly geeky in nature, I am certain you won't regret it.
And if you want to use a highly optimised nice theme for your Jekyll and GitHub pages, we've decided
to share the theme you're looking at now for free under the terms of Creative Commons Attribution-ShareAlike
such that you can get the exact same look and feel for your site as we're using here.

* [Getting started with Jekyll](https://jekyllrb.com/)
* [Getting started with GitHub Pages](https://pages.github.com/)
* [Setting up a custom domain for your GitHub Page](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
* [Use our free Jekyll Theme](https://github.com/polterguy/aista-jekyll)
