---
layout: post
author: thomas
title: 7 Questions and Answers about Low-Code
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/low-code-survey.jpg"
---

## 1. What is Low-Code?

The term low-code was coined by Forrester in 2014, but the idea have arguably existed for decades, and can to some extent be seen in 25+ year old software systems such as Access, Excel, and Visual FoxPro. Although often used interchangeable, the terms low-code and no-code have some differences. Where no-code is typically often associated with “citizen development”, enabling non-software developers to create software systems, by dragging and dropping visual elements on the screen - The term low-code is more often used to describe automating repetitive software development tasks, having the computer automatically create the code, instead of requiring a software developer spending his or her precious time to manually assemble the same code. Hence, low-code is not really an accurate word, since a low-code software system typically has the same amount of code as a traditionally assembled software system. The difference is that a low-code system was to a large extent automatically assembled, while the traditional software system needed much more manual labour. Hence, one of the primary purposes of low-code obviously becomes to reduce costs, by reducing the need for manual labour, often resulting in higher quality code, more stable end results, with fewer security holes. Below is a screenshot taken from Magic Cloud, my company's flagship product, and how it automatically generates a CRUD web API wrapping your database to provide you with an example.

![Crudifier in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

## 2. Is Low-Code a new thing?

The answer to that question is “complicated”. While we have seen an explosion of low-code tools and frameworks the last 5 to 10 years, the idea of reducing technical debt by relying upon pre-fabricated components and libraries goes more than 50 years back in time. It could be argued that every time you use a library, component, or framework, you are in fact utilising “low-code constructs”, since the amount of code you have to create yourself significantly reduces, and you can in such a regard “outsource technical debt”. Other examples are command line interfaces such as the Angular CLI allowing you to generate skeleton components you can modify yourself after the Angular CLI has done its job, or Entity Framework’s ability to generate C# classes based upon an existing database. However, the last 5 years we have seen an explosion in the abilities of new low-code frameworks to refine and improve upon such ideas, to an extent we could barely imagine just a decade ago, similarly to the AI explosion we saw some 10 years ago. Both AI and low-code constructs have existed with us probably for more than 50 years, but only recent innovations and improvements in computer speed, coupled with new ideas, new programming languages, and better algorithms, have facilitated for these constructs to be taken to “the next level.”

## 3. What can you do with Low-Code?

In theory you can do anything you wish with low-code. This is especially true if your low-code framework of choice generates actual code for you, in a Turing complete programming language, since this allows you to modify the automated result your low-code framework produces after it has done its job. In practice though, low-code is often mostly used for repetitive tasks, such as for instance generating HTTP CRUD endpoints wrapping your database, and/or other types of highly standardised tasks, where the amount of code needed to solve the job might be huge, but its “copy and paste factor” also equally large. Low-code typically is better suited for tasks where the amount of standardisation is large, yet still you have access to huge amounts of meta data. To generate CRUD HTTP endpoints wrapping a database for instance is extremely easy for an automated process, since your low-code tool can easily retrieve meta data about tables, columns, and foreign keys in your database. While generating a beautiful frontend, matching your company’s existing profile might be more difficult. Hence, you typically would want to use low-code more in repetitive tasks, where you have access to meta data, and the amount of standardisation is large.

## 4. Is Low-Code lockin?

The answer to the above question varies greatly depending upon which low-code framework you chose. If your low-code platform is closed source, generates only binary applications, being impossible for developers to modify and extend upon, then you have a huge amount of lockin. If your platform is open source, creates code that can be modified by a software developer and easily extended upon, you literally have zero lockin. To understand how much amount of lockin your organisation has in these regards, ask yourself the following question; “What would happen if my low-code framework vendor goes out of business?” The answer to that question should be your metric in regards to how much lockin you’re currently suffering by. Other questions to ask down the same path is; “What would happen if my low-code vendor increases their licensing costs by 10?” - Yet again, if your answer is that you would be in trouble, then your low-code vendor has a great amount of lockin on you. Like everything else in life, the amount of lockin you can tolerate become an individual choice, but there exists open source low-code frameworks, resulting in you having zero lockin. Like all other hyper growth areas of software development having experienced a “gold rush”, there exists scrupulous software vendors out there with shady business models, explicitly designed into forcing you to become dependent upon their services in order to continue your own business. If you are 100% dependent upon your low-code platform vendor to have success yourself, you’re probably not in a healthy relationship with a healthy platform vendor, and you would probably be better off changing low-code framework.

## 5. Can I replace my expensive software developers with Low-Code?

First of all, if you’ve got a lot of expensive software developers, then I want to congratulate you. Being the CEO of a low-code framework vendor myself, I know first hand how difficult it is to find great software developers. And my advice to you is to do everything you can to keep your great software developers, and ensure they want to continue working for you. Low-code is not about getting rid of human resources and replace these with the machine, as it is about making your existing (human) developers more productive. Your savings in low-code should be focused on increasing productivity without increasing costs, and not about reducing costs while keeping productivity. A skilled software developer is incredibly difficult to replace, and only once he or she is gone you will understand what you have lost. So my advice to you would be as follows; **No, no and no**! You cannot replace your expensive software developers with low-code frameworks. In fact, I would go further and encourage you to teach your existing expensive software developers low-code frameworks, such that they become much more productive, at which point you can justify paying them even more than whatever you’re paying them today. Highly motivated and skilled software developers are close to impossible to replace, and you should be grateful for them wanting to work with your company.

## 6. Why should I care about Low-Code?

Low-code if applied correctly allows you to increase your company’s productivity, sometimes by one order of magnitude - Implying if you don’t care about low-code, chances are your competitor will care about it, at which point your competitor will be 10 times as productive as you, for the same amount of resources you’re spending - Resulting in your competitor constantly underbidding you, delivering more than you, and having a better value proposition for his clients, resulting in you slowly over time going out of business. Let me ask you a question to illustrate the absurdity of the above question; “Why would you want to fly across the Atlantic Ocean when you can swim?” - Really, it’s that simple. Low-code is not a fad, it’s here to stay. To prove it realise that more than 50% of all software development companies have already applied low-code constructs into their software development cycle, and roughly half of these companies are happy with the results it has created for them so far - And the ratio of happy to unhappy increases every year, since the space and frameworks are growing more and more mature every year. If you tried low-code last year, and it failed, my advice to you is try it again. Low-code is in hyper growth these days, and frameworks are released almost on a daily basis, and existing frameworks that might have been immature 2 years ago, might very well be something completely different today. And simply because one framework failed you doesn’t imply another framework will fail you. Low-code adoption is in hyper growth these days, and also large and mature companies are currently adopting low-code frameworks these days. Not adopting low-code today would be the equivalent of not adopting cars 100 years ago, because of arguments such as “I still trust my horse more.” Of course like all immature industries, it’s a gold rush, and not everything that’s shiny is gold - But the general direction low-code is heading in, is a direction we’ve seen dozens of times before throughout our history, and it is the inevitable future. Whether or not you should adopt low-code today though is a different question, and this depends upon your business requirements. However, I would argue that this decision isn’t really yours to make, but rather ask your developers, at least a small team of senior developers, and give these the required time to research different low-code frameworks, and maybe have them start out with the frameworks providing the least amount of lockin would be my advice - Implying the open source low-code frameworks out there, resulting in the least amount of risk for your company as a whole. According to a study performed by DZone a year ago, 6% of respondents answered “all the time”, 16% answered “often”, and 34% of respondents answered “sometimes” on the question “How often do you use low-code?” - This either implies that 56% of developers are delusional, or they know something you don’t know. If there’s a 10% chance of that they know something you don’t know, could you afford to bet your company’s future on that 56% of these respondents were delusional?

![How often do you use Low-Code](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/low-code-survey.jpg)

## 7. How should I start with Low-Code?

My advice would be to find a highly motivated software developer in your organisation, already having shown an interest in the subject, and have that individual create one or two micro services you can incorporate into other projects. Preferably something small, that’s completely encapsulated as a micro service, without too much complex business logic. For instance a component primarily intended to perform CRUD operations towards one of your databases. This reduces risk for you, since it becomes a small chunk of your larger project, allowing you to easily change your mind further down the road. When the micro service is finished, you evaluate the process, and if the results are positive, you slowly move smaller parts of your software development pipeline that can be moved into the low-code space. If you’re smart, you chose a low-code framework with small amounts of lockin, preferably something that’s open source, since this further reduces your risk, allowing you to host the entire platform on your own infrastructure if required. This methodology is what we refer to as “hurrying slowly”. When your developer starts understanding the platform you have chosen, you should have your developer teach another person in your organisation, allowing your low-code initiatives to “grow organically from within”, by leveraging the first developer’s enthusiasm about the low-code platform, and facilitating for this enthusiasm to spread out organically in your organisation. This eliminates fear of low-code internally within your organisation, which most of the time is unjustified, preventing your existing developers from wanting to learn low-code - While also at the same time this method significantly reduces risk for your organisation as a whole. Yet again DZone’s readers comes with advice to us through the low-code study DZone performed a year ago, where the respondents were asked the question “Which use cases are low-code useful in?” You can see what the respondents answered “Very useful” to in the chart below. The parts where more than 40% of the respondents answered “very useful” for was; Enterprise CRUD, interactive web forms, request handling, business process management, and simple databases. This implies that if you have any of these 4 use cases, and you apply low-code to your problem, more than 40% of DZone’s respondents believes that low-code will be “very useful”. Hence the way to start with low-code is probably with one of the following use cases, at least according to DZone’s readers; CRUD, web forms, request handling, business process management, or simple databases. Implying if you choose one of those previously mentioned use cases, you isolate your project by creating one or two micro services, you diverge small amounts of initial resources to the task, and you choose a low-code framework without lockin - The chances of you succeeding with low-code becomes much higher, resulting in a positive feedback loop through your low-code team, spreading out into the rest of your organisation, allowing you to painless perform the transition into 10x productivity, without disrupting your organisation’s productivity in any ways.

![Use cases for Low-Code](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/use-case.jpg)

## Shameless plug

I am the CEO of Aista, and our flagship product is [Magic Cloud](/tutorials/getting-started/). Magic is
an open source low-code framework focused on CRUD and database web APIs. If you're curious about low-code,
you are of course free to try out our product in your organisation.