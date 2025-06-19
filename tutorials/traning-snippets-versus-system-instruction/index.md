---
title: Training Snippets versus System Instruction
---

There are two basic ways to provide _"context information"_ for your AI chatbot that doesn't require programming; System Instruction and Training Snippets (RAG). Since the relationship between these two can sometimes be confusing, I will try to explain the difference in this article. However, let's first ask ourselves exactly what context information is.

## Context Information

Context information is information that is automatically transmitted to OpenAI as the user is asking your chatbot a question. Without context information, the chatbot will perform just like a vanilla ChatGPT request, without having any knowledge about your company or organisation. If you add context information, the AI chatbot will be able to use this context as the basis for answering users' questions. It's similar to uploading a PDF to ChatGPT and asking it questions about the PDF, except everything happens automatically behind the scenes, and is invisible to the end user.

By providing context information, you can control the LLM's behaviour, in addition to teaching it new things it didn't know from before. In addition you can provide _"instructions"_ to the chatbot, such as giving it a name, telling it to answer in a specific language, or for that matter instruct it to answer in the style of Snoop Dogg.

In a way it could be argued that providing context information to the LLM is what makes your AI chatbot unique, capable of answering questions related to your data.

## System Instruction

The system instruction is _always_ transmitted to the LLM as an invisible message number 1. If you're acquinted with OpenAI's APIs, it's the _"system"_ message of an HTTP invocation towards their chat API.

Since the system instruction is _always_ transmitted to OpenAI, this makes it a very good place for instructions that are general and should always be sent to the LLM. This makes it highly useful for providing _"instructions"_ such as a tone of voice, in addition to basic information that the AI chatbot should always know. You can edit the system instruction by clicking _"Configure"_ on your type from the machine learning component. Below is an example for an imaginary AI chatbot created for SalesForce, intended to act as a sales executive.

![Screenshot of editing the system instruction](/assets/images/system-instruction-editing.png)

The system instruction should not be too long, but only contain the most important information and instructions required to modify its behaviour according to your requirements. However, there's no real difference between the system instruction and a training snippet conceptually, since they both end up as context information.

This allows you to provide the most important parts of your expected behaviour to the system instruction, and can for instance contain information such as _"The name of your company"_, _"How to call your company"_, or _"How to act if the user is showing frustration"_, etc. Think of the system instruction as the foundation for your AI chatbot, as in the contextual information it should _always_ have access to, regardless of what questions the user is asking.

## Training Snippets

Training snippets again are matched according to what questions the user is asking, and you can have thousands of individual training snippets, covering all sorts of different information. When the user is asking a question, the AI chatbot will first generate embeddings for your questions, and then lookup training snippets such that it attaches the most _"similar"_ training snippets as additional context data, before it transmits the request to the LLM.

When a question is being asked, your cloudlet will find the top n matching training snippets, until it's filled up its context window, and transmit these to the LLM. This allows us to transmit only context information from your training snippets that is relevant to answer the user's question. If you want to synthesise this behaviour to see which training snippets are a part of a specific question, you can copy and paste your question into the Search bar of the _"Training data"_ tab, and check the _"VSS"_ checkbox. Below is a screenshot to serve as an example.

![Searching through your training snippets using VSS](/assets/images/vss-search-through-rag-data.png)

In the above image you can see a number in square brackets for each training snippet in the first column. This is the _"similarity value"_ of each individual snippet, and basically the lower this number is, the more relevant the particular snippet is to the question being asked. A similarity of 0 means the question is the _exact_ same content as the snippet. While a similarity of 1 means it's the exact _opposite_ and completely irrelevant. This allows us to match for instance a question being _"What's the price"_ towards training snippets containing price information.

Notice, this _"similarity"_ value is also related to the threshold of your configuration - Since only snippets that are _within_ the threshold you've got in your LLM tab's value are considered. Notice, this number is inversed, so a snippet of 0.56 similarity, will be considered if you've got a threshold of 0.3, since 0.3 + 0.56 is less than one. A snippet with a similarity of 0.61 again will _not_ be condiered. This allows you to exclude irrelevant training snippets if they're below some threshold value in similarity.

The _"Tokens"_ column again is important to understand, since it's the number of OpenAI tokens one specific training snippet is consuming. If you look at your AI chatbot's configuration, and choose the _"LLM"_ tab, you will see one important field that's related to training snippets. This is its _"Max Context tokens"_ value. In the screenshot below you can see this number being 4,000.

![Max Context Window value for your machine learning model](/assets/images/max-context-window.png)

This value is an instruction to the cloudlet of how many tokens to consume in total through RAG training snippets for each request. In the above image it's set to 4,000, while our training snippets from the image above is in the range of 126 to 865.

When a question is being asked, the cloudlet will retrieve the most relevant training snippets, and start adding context information from the top of the list returned, until it has filled up its context window with a maximum of 4,000 tokens, or it can no longer find snippets with a similarity that's within the _"Threshold"_ value of your type.

For our _"What's the price"_ example above, it will probably have room for all training snippets on page 1, and possibly add some 15 to 20 training snippets to the request in total. The cloudlet will _never_ add more than 4,000 tokens in total though from your training snippets, and it will never add snippets that's not within the _"Threshold"_ value for your type.

This allows you to modify the _"Max Context tokens"_ value of your type to reduce or increase how much context you want to provide. In general more context is better, but also more expensive, since it will consume additional input tokens when invoking OpenAI. In general, 4,000 is the _"sweet spot"_ for context tokens, and 0.3 for threshold - Unless you have special requirements.

## Rolling context

_"Rolling context"_ is a concept we've invented ourselves, and _significantly_ increases the quality of the chatbot's response. To understand the concept you first have to realise that AINIRO's AI chatbots are _"conversational AI chatbots"_. This implies it will remember previous questions, _and_ previous contexts, until it's filled up the available context window the specific model you're using is capable of dealing with (as a general rule of thumb).

This is what allows users to for instance ask questions like _"Who's your CEO"_, for then to get an answer and continue with follow up questions such as _"Can you show me an image of him"_. The word _"him"_ being the subject of the conversation here, and since the LLM will be given previous questions and answers from the same conversation, the LLM will automatically associate _"him"_ with the CEO from the previous answer, and display in image of the CEO if it's got that in its context.

Since every question triggers a new _context_ due to VSS search through your training snippets, this allows us to attach multiple contexts for each question, by preserving the _previously_ used contexts for consecutive questions. Only when the total available context window for the LLM is exhausted, the cloudlet will start _"pruning"_ messages from the top of the conversation to avoid overflowing the LLM with too many input tokens. This implies that for gpt-4o for instance, we've got 128,000 tokens to use at most. With a 4,000 max context value for individual requests, this implies that for each question an additional 4,000 tokens are associated as tokens, until we reach the max value of the LLM.

Notice, the _"Max response tokens"_ value is deducted from the LLM's context window to give room for the answer from the LLM. So for this example, it will have a maximum value of 124,000 for context information.

Also notice, that gpt-4.1 has a context window of 1 million tokens, and we will cap this at 128,000 by default, since providing 1 million context tokens for an average support AI chatbot is _beyond overkill_, and might become very expensive over time.

However, due to our _"rolling context"_ concept, the AI chatbot will basically _"become smarter for every question asked"_ until it's filled up its available context window.

## System Instruction of Training Snippets?

So, what should you choose as your primary source for adding information to your AI chatbot? Actually, there's no real difference between the system instruction and training snippets, and they can both take both instructions and information.

Our general rule of thumb is that the most important information, such as contact us information, name of company, etc, we add to the type's system instruction. While more dynamic data, such as information about specific products or services, we add as training snippets. This is because the system instruction is _always_ there, implying whatever you write into its system instruction will _always_ be available for the LLM to use as information to answer questions. While training snippets needs to match the question asked.

We suggest you keep your system instruction small in size though, max 2 pages of text in a PDF document roughly, unless you've got special requirements. While you add additional information as individual training snippets.

And there's nothing preventing you from adding _"instructions"_ to individual training snippets, such as for instance _"If the user wants to contact a human being, then ask the user for his or her email address, before ...blah, blah, blah ..."_

## Wrapping up

In this article we discussed the relationship between the system message of your machine learning type and its training snippets. We showed how we're using VSS and embeddings to match questions towards your training data, to transmit context information to the LLM - In addition to the relationship between the _"Max context window"_ size, _"Threshold"_ value, and how this is used to extract relevant information from your training snippets as you're prompting the LLM.

If you find this difficult to understand, [AINIRO](https://ainiro.io) is providing this as a service to our clients, and we'd love to help you out creating an amazing AI chatbot for your company. If you're interested in having us help you out, you can [contact us here](https://ainiro.io/contact-us).

