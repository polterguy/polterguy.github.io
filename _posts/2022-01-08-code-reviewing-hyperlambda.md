---
layout: post
author: thomas
canonical_url: https://aista.com/blog/code-reviewing-hyperlambda/
---

One of our partners has just finished the initial implementation of a medium complex FinTech project using
Magic and Hyperlambda, and they wanted me to code review the product before putting the finishing touches on it.
The system has 15 tables, it's got 169 files, 165 of which are Hyperlambda, and the project is of medium complexity.
There are two interesting points to this story, which is as follows.

1. It took me 15 minutes to do a complete code review on the entire thing
2. I could only find a handful of issues, in fact 7 to be exact

The reasons why this is spectacular is because first of all, if I was to code review C# code or PHP code
for a system of the same complexity, I would probably need at least a whole working day, maybe even half a week.
Due to the degree of simplicity in Hyperlambda, I could read through its entire codebase in 15 minutes.
The system's backend was implemented by one developer, whom had never created any Hyperlambda code before, still I could
only find 7 issues with it. Every time I code review C# code of the same complexity, I can easily pinpoint
dozens and sometimes hundreds of issues.

Anyways, this illustrates a couple of crucial unique selling points with Hyperlambda, being of course that
the thing is pathetically easily understood, ridiculously easy to read, and preposterously simple to maintain.
Imagining reading through a C# project, or a Java project, that is created on top of a database with 15
different tables, doing multiple integrations with 3rd party systems, with the same degree of complexity as
this system has in 15 minutes, and understanding the system in its entirety in 15 minutes, is of course
simply madness. With Hyperlambda, I spent no more than 15 minutes, and after those 15 minutes, I had created
a deep and thorough understanding of 90% of the codebase, what it does, and how it does what it does.

BTW, if you're interested in code reviewing your Hyperlambda code, and or tutoring in any ways, this
is a services we are providing for our partners - And you can send us an email at [info@aista.com](mailto:info@aista.com)
if you want to start the discussion in these regards. Our philosophy is that the foundation of our success
is our clients' success and happiness. When you sleep at night, we sleep at night ... ;)
