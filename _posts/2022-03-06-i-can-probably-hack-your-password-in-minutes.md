---
layout: post
author: thomas
title: I can probably hack your password in MINUTES!
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/password-entropy.jpg"
description: Your password is probably easily hacked in seconds by an experienced hacker, here's why, and what you can do to avoid it.
---

The average password is easily hacked in minutes by an experienced software developer. This is because of a fundamental flaw in how we were taught to create our passwords. An example of a bad password is for instance; _"qWxc4&Gh"_. On the surface such passwords seems to be impossible to hack, but such a password can actually easily be hacked in 39 minutes by an experienced hacker by simply _"guessing"_, using a technique referred to as brute force, where a computer tries all combinations of characters one after the other. The reason is because of something we refer to as _"entropy"_ in computer programming and cryptography. There are simply not enough possible combinations in short passwords such as the above to be _"random enough"_ to prevent a computer from guessing it by trying all combinations of characters one after the other. Below is a list taken from [Hive Systems](https://www.hivesystems.io/) illustrating the problem.

![Password entropy](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/password-entropy.jpg)

In addition to that such passwords are easily guessed, they're also extremely difficult to remember, resulting in users having to write down their passwords somewhere to be able to remember them. The only real alternative to writing down your passwords, seems to be to use the same password on multiple sites, over and over again. Since few websites and software systems (correctly) implement password hashing using BlowFish and per record based salts, this results in that if a malicious hacker manages to hack one website you've registered with, he can typically reuse your password from that one website on _all_ websites you've registered. This of course results in that if you choose to register with a password at _"The Free Ponies and Barbies for your Daughter"_ website, a hacker capable of hacking _"the free pony site"_ might end up having your password for your online internet bank. If you're a software developer reading this and you're telling me _"but I'm hashing my passwords"_ then I've got three words for you ...

> Rainbow Dictionary Attack ...

... search for it and weep!

## The solution

If you create a password consisting of 8 characters you end up with an entropy of 72 to the power of 8. This is because of that your base number is 72. This is a ridiculously high number for humans, but for a computer it is actually quite easily traversed using brute force. If you instead choose to create your passwords as sentences, you end up with a base number of 470,000 if you're exclusively using English words. This is because of that the English language contains 470,000 different words. Hence a sentence with 8 words becomes 470,000 to the power of 8, which of course becomes such a ridiculously high number that if you used every single computer on earth to try to guess such a password, you'd still need a trillion, trillion, trillion, trillion years (or something). Then add to the above entropy by realising there exists hundreds of actively used languages on the planet, and thousands of dialects, further adding to the entropy of your passwords. Below is an example of a password that is literally 100% perfectly impossible to guess using brute force.

> This is actually a very secure password dude!

The above password contains 8 words, implying 470,000 to the power of 8 different combinations required to guess it - While at the same time the password is also easily remembered. The only drawback with the above password is that it requires slightly more time to write, which can be a little bit inconvenient, especially if you're logging in with your phone. However, once you've logged in the first time, typically your phone will offer to remember your password, implying you'll only need to type it _once_. So even though the above password seems to be unsafe for a human being, it's probably a trillion, trillion, trillion times more secure than the 8 character password we started out with initially.

Facts are that the way we were taught to construct our passwords is quite counter intuitively a very, very, very bad password strategy. It's much smarter to use entire sentences, and add some dialect, and/or words from your native tongue. This makes your passwords easily remembered and very difficult to guess. For added benefit you can create passwords that are easily visualised, creating imagery in your head, such as the following which is easily remembered due to the image it creates, but still not an easily guessed sentence.

> I like the smell of sunshine on a Sunday

The poetic imagery of something such as the above makes the above password extremely easy to remember, since it creates _"images"_, allowing you to more easily create associations, strengthening your ability to remember it. While at the same time rendering your passwords 100% impossible to guess using any known techniques as of today. This is why we don't require any special characters, combination of upper case and lower case characters, and/or or numbers as you setup Magic and it asks you for a root password - Simply because we want to encourage users to using sentences as passwords to increase entropy and strengthen security of their Magic servers. And yes, before you ask, we (obviously) use BlowFish and per record based salts as we store your passwords into Magic's database ...

For the record, I have never attempted to maliciously break into any computer systems on the planet, neither to steal your password, nor for any other (malicious) reasons. So even though I _can_ hack your password, rest assured I personally never would ... ;)
