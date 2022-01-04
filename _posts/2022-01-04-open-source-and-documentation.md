---
layout: post
author: thomas
---

As an Open Source advocate, being the _by far_ most active contributor to GitHub in Cyprus, I am obviously
passionated and opinionated about Open Source - And during my 20+ years of contributing code to open source projects, and having
maintained open source projects myself, I can tell you that the defining difference between a successful project
and one that fails is _documentation_. If you write the best open source library in the world, but don't provide
documentation, your code might as well exist within a black hole. Nobody _can_ use a project that's
not documented, regardless of how well written it is.

If you look carefully at the URL of this website, and/or the HTTP headers returned from this site, you will
notice that it's hosted by GitHub. GitHub has an initiative called [GitHub Pages](https://pages.github.com/).
GitHub Pages allows you to host any static content you wish for free. In addition, they provide [Jekyll](https://jekyllrb.com/)
integration, allowing you to automagically transform your static Markdown files into HTML, and serve it with
blistering speed from GitHub's servers. This provides you with a remarkably solid infrastructure to document
your Open Source thing, whatever _"your thing"_ might actually be.

To help facilitate for more, better, and higher quality Open Source in the world, we at Aista have decided to give away
the Jekyll theme you're looking at here for _free_. The theme was explicitly created to document our
own Open Source project [Magic Cloud](https://github.com/polterguy/magic), and is created with the philosophy
of _content first_. Implying the content is the most important thing on this site, in addition to allowing
users to navigate our content as easy as possible, to find whatever it is they are currently looking for in
order to use your Open Source project.

The theme is based around the assumption of that there's one _"Most Wanted Response"_ you would like to
guide users into, which is easily configured using the _"mwr"_ configuration setting in your _"\_config.yml"_
file. This could be to star your project on GitHub, download the latest code, or whatever really. You can
see our MWR at the top/right corner of this page. It's the button that says _"Start"_, and it guides
users to the _"Getting Started with Magic and Hyperlambda"_ tutorial.

## Using a high quality Jekyll Theme

If you want to use our theme, it's very easy - You can find its code [here](https://github.com/polterguy/aista-jekyll).
The theme requires some configuration by adding a _"\_config.yml"_ file, a _"blog.html"_ file, and creating a
folder caller _"\_posts"_ where you put your Markdown blog posts, _if_ you want to use blogging with your site.
You can check out the structure of this GitHub page [here](https://github.com/polterguy/polterguy.github.io) to
get a feeling for how you need to structure your site if you want to use the Aista Jekyll Theme.

With this theme you've got complete control over your content, navigation, and even how your blog ends up
looking like - But more importantly, you're documenting your site on a high quality SEO foundation, easily
allowing your users to find your Open Source library's documentation, with high quality fonts, making
your documentation easy to read and navigate. And you're _not paying as much as a nickle to host it_.
This allows you to use nothing but your own energy and faith in your ability to study, improve, and work,
for then to use these abilities to create something nice for the world, and document it such that others can
access it. As an additional bonus, when hosting your site with GitHub, there are no banners, no advertisement,
and nothing coming in between you, your readers, and your open source code and documentation.

**Notice** - Our Aista Jekyll Theme is also explicitly created to make YouTube videos _"pop out"_, something
you can see below.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/lYcwpR72EN0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

The HTML/Markdown required to inject a YouTube video such as I do above, is as follows.

```html
<div class="video">
<iframe
  width="560"
  height="315"
  style="position:absolute; top:0; left:0; width:100%; height:100%;"
  src="https://www.youtube.com/embed/lYcwpR72EN0"
  frameborder="0"
  allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```

And, the theme also has high quality support for code snippets, such as you can see above with our HTML code example.
Images will also _"pop out"_ in a similar fashion.

## Why create open source anyway?

The above might be your only remaining question at this point. However, if you need that question answered,
I suspect you might want to chose a different career path than software development. Because in the end,
no software developer became a great software developer because he found intelligent answers to the above
question. Still most great developers are actively contributing to several open source projects.

However, when that is said, almost every single job I have personally ever had, I was given at least partially
because I was able to show case my open source code. And my current company, whom I happen to be CEO of,
having secured VC funding for, to hire a handful of software developers for a period of 3 years before we
need to start making money for ourselves - _Was exclusively based upon my open source code_.

But in the end, you contribute to open source projects because you _want_ to contribute to open source
projects. There are no intelligent answers beyond that really. A duck is what a duck is, and contributing
should by itself be its own reward. If you wish to add a link to PayPal or some _"buy me a coffee"_ thing
on your site, you're of course welcome to do that, and with a highly popular open source project, you can
expect _some_ donations to roll in over time - But really, your motivation for contributing and creating
your own open source code should really be as simple as follows ...

> Because I can, and I want to ...

Anyways, feel free to use our [Aista Jekyll Theme](https://github.com/polterguy/aista-jekyll) as you see
fit, for whatever purpose you might have. The thing is Creative Commons Attribution ShareAlike licensed,
implying it's free for all to use, as long as you keep the backlink of course.
