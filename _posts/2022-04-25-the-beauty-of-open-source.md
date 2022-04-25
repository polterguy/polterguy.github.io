---
layout: post
author: thomas
title: The Beauty of Open Source
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/open-source.png"
description: 20 years ago when I initially discovered Open Source, few could see its beauty. Today the model is such an obvious game changer nobody really argues anymore.
---

We have chosen to base our entire business model upon open source. For a traditional business based upon secrecy and _"trade secrets"_, such a choice might look weird, since we're basically giving away our filet mignon for free you might say. However, for a small startup it allows us to _"compete"_ in a segment traditionally untouchable for a small company such as us. Let me illustrate that with a simple story about our codebase to illustrate the point.

One of the databases we support in Magic Cloud is MySQL. MySQL's database connector has a long standing bug related to async retrieval of data. If MySQL was closed source, there would be no way anybody would really know, except that all attempts to fetch data from a MySQL database would be blocking invocations, resulting in much less scalability and throughput for your backend as it fetches data from your MySQL instance. At some point some smart developer understood the problem, and more importantly [how to fix it](https://mysqlconnector.net/). At Aista we had no idea about these issues with MySQL's default data connector. However our codebase was open source, so we didn't need to know, since due to our codebase being open source [another smart developer](https://github.com/bgrainger) discovered the issue for us, and [fixed it](https://github.com/polterguy/magic.lambda.mysql/pull/3#issuecomment-1107898160) without us having to do anything but click the _"Accept pull request button"_. Thank you Bradley Grainger.

If any one of the above parts of our infrastructure was closed proprietary code, there would be no way we would be able to have the above scenario unfold. If MySQL was closed source, the developers behind [MySQL Connector](https://mysqlconnector.net/) would not be able to neither discover it nor fix it. If our codebase was closed source, Bradley wouldn't be able to discover our issues, etc, etc, etc. Every single part of our codebase would need to be open source from the bottom to the top for us to be able to harvest the quality improvements that Bradley applied for us, for free may I add. So by arguably _"giving away our filet mignon for free"_, we get to play in a more _even_ playing field, where we can more easily compete with _"the big guys"_, resulting in quality improvements of our product, typically only achievable for huge companies such as Google or Microsoft.

Thank you MySQL, thank you Bradley, than you MySQLConnector, and thank you Open Source - We love you all.
