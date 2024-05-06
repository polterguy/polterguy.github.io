---
title: Magic CAPTCHA - Outperforming Google reCAPTCHA by 2,567 times
---

Magic CAPTCHA is an alternative to Google reCAPTCHA and is used by Magic internally. It is based upon Proof of Work (PoW), and is tiny in comparison to reCAPTCHA. In fact, Google's reCAPTCHA is 2,567 times larger on bandwidth consumption than Magic CAPTCHA.

* Magic CAPTCHA - 662 bytes
* Google reCAPTCHA 1.7MB

This is a big deal since the more JavaScript you put on your page, the slower your site will load - And to further the insult reCAPTCHA is blocking JavaScript, so it basically _"destroys"_ your website's experience as you include it on your page. Magic CAPTCHA typically loads in 0.050 seconds, implying 50 milliseconds - While reCAPTCHA needs several seconds to load, typically 2 to 5 seconds even on a high bandwidth connection. You can read more about the basic idea of PoW-based CAPTCHA in the articles below.

* [Using Bitcoin and Blockchain ideas to create a better CAPTCHA library](https://ainiro.io/blog/using-bitcoin-and-blockchain-ideas-to-secure-our-ai-chatbot)
* [Goodbye Google reCAPTCHA, hello website speed](https://ainiro.io/blog/goodbye-google-recaptcha-hello-website-speed)

![Example of CAPTCHA](https://ainiro.io/assets/images/blog/captcha.png)

## How to use it in your own code

Magic CAPTCHA is integrated into Magic Cloud, but you can also use it in your own components and software if you wish. The process is fairly straight forward.

* Include magic-captcha.js on your page.
* Create a Magic CAPTCHA token as you invoke your endpoint, and pass in this token to your endpoint.
* Verify the token on the server, and throw an exception if it doesn't verify.

If you're using Hyperlambda and you're creating a Hyperlambda module in a cloudlet, the process of verifying your CAPTCHA token is straight forward. Add the following Hyperlambda at the top of your file.

```
execute:magic.auth.captcha-verify
   token:x:@.arguments/*/token
```

If the token isn't valid the above slot invocation will throw an exception. To increase the workload which defaults to 3 trailing zeros, you can add a **[workload]** argument of 4 to the above code. However, with a workload of 4 it takes on average 0.5 seconds on my M3 CPU to generate a valid token, so increasing it beyond this is probably not feasible. If you change the workload requirement on the server, you have to use at least the same workload on your client when generating the token.

On the client again you've got to create code resembling the following when you need a token.

```javascript
mcaptcha.token(function (token) {
  // Pass token into the server here.
}.bind(this), 3);
```

The last argument to the `token` function is the workload, implying the number of trailing zeros before a valid token has been generated. The path to your magic-captcha.js file is typically something as follows.

```
YOUR-CLOUDLET.us.ainiro.io/magic/system/misc/magic-captcha.js
```

Once your client has a valid token, you have n seconds to invoke your server before the token is no longer considered valid. This is because the UTC time for generating the token is a part of its value, and the server will only allow for tokens that are fresher than n seconds to be considered. You can configure this value by overriding it on your server with an **[age]** argument to your invocation to the **[magic.auth.captcha-verify]** slot, but the default value is 10000, implying 10 seconds (10,000 milliseconds).

## Use it in 3rd party software

You can also use Magic CAPTCHA in your own software, such as a PHP application or a Python application. Your cloudlet has an HTTP GET endpoint that verifies any token, and returns a 400 status code unless the token is valid. The path to this endpoint is as follows, and it takes a single QUERY parameter named _"token"_ being the token's value.

```
YOUR-CLOUDLET.us.ainiro.io/magic/system/misc/magic-captcha-verify
```

## How it works

PoW on the Blockchain implies having a seed value starting out at e.g. 0 that you append to some string value, for then to generate a hash until you've got n trailing zeros at the end of your hash. If you don't get a resulting hash value with n trailing zeros, you increment the seed value by 1, and try again - Until you've got a hash value with enough trailing zeros to be considered valid. This implies a client wanting a valid token needs to generate n amount of hash values, depending upon how many trailing zeros you need for a valid token.

* 1 ZERO requires on average 16 hash values
* 2 ZEROs requires on average 256 hash values
* 3 ZEROs requires on average 4,096 hash values
* 4 ZEROs requires on average 65,536 hash values
* 5 ZEROs requires on average 1,048,576 hash values

For most endpoints where Magic CAPTCHA is feasible, a workload of 3 or possibly 4 is a good value. 5 implies generating a token might take minutes, even on an M3 CPU. 2 is too small, and barely uses the CPU at all before a valid token has been generated.

## Benefits

First of all, Magic CAPTCHA is literally 0.04% of the size of reCAPTCHA, implying it has zero negative consequences for your page load speed - Where Google's reCAPTCHA typically eats up 25% of your total page load speed according to Google's own measurement tools. This implies that for pages that needs to load fast, reCAPTCHA is **fundamentally broken**. Magic CAPTCHA is _not_ broken, and has _zero_ consequences for your page load speed.

In addition Google's reCAPTCHA will constantly invoke Google with information about events occurring on your page. This eats up more bandwidth, which becomes a really big deal on phones and tablets with slow internet connections.

On top of that, simply loading _anything_ from a Google domain forces you to show cookie disclaimers to be in compliance with GDPR and other privacy related laws. Magic CAPTCHA will never transmit cookies or private data to the server, unless you somehow force it to do this. This implies you can get completely rid of all your cookie disclaimers, assuming you don't use other Google related code in your frontend.

> All in all Google reCAPTCHA is for the above reasons **fundamentally broken**!

Magic CAPTCHA also allows for _"friendly bots"_ to invoke your endpoints without additional authentication or authorisation schemes. Sometimes you want to create publicly available endpoints that prevents malicious bots from invoking thousands of times, while still allowing _"friendly bots"_ to invoke the same endpoints. Magic CAPTCHA allows for this, since the cost/benefit becomes a calculation the bot can do to calculate that the cost of generating a token is actually worth it - Resulting in that a bot might want to invoke your endpoint once or twice, but will probably avoid invoking it 10,000 times, unless it is very persistent and willing to waste a lot of energy (read money) to invoke your endpoint.

## Concerns

Magic CAPTCHA does not technically eliminate bots. In fact, any bot _can_ easily invoke your endpoint, but the idea is to scare bots away from doing that repeatedly due to the cost of having to create thousands of SHA256 values for each invocation, which spends a lot of CPU, and therefore becomes expensive over time.

This implies that technically Magic CAPTCHA isn't actually a CAPTCHA according to its strict definition, and malicious bots might go through it and invoke your endpoint. The idea with Magic CAPTCHA is that the expenses of doing such a thing becomes so great over time, that few will choose to do it simply for this reason. And even thouse that invokes your endpoint, will probably not want to invoke it thousands of timnes consecutively.

In addition when generating a token the client's CPU will run on maximum performance for 0.05 to 5 seconds, depending upon the CPU's power and your workload requirements. This spends extra power on the client, which might be a concern for phones and other devices that are running on battery, and/or endpoints the client needs to invoke many times, over and over again.

For the above reasons Magic CAPTCHA isn't a drop-in replacement of Google's reCAPTCHA, and only really work in some few scenarios. However, when it does work, it runs in circles around Google reCAPTCHA on all the parameters that matters.

Notice, Magic still contains Google reCAPTCHA logic allowing you to resort to reCAPTCHA when Magic CAPTCHA isn't enough for these reasons, since Magic CAPTCHA can't replace Google's reCAPTCHA on everything. However, when it can replace reCAPTCHA it is literally _"a bajillion"_ times better.
