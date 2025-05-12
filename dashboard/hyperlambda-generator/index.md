---
title: Hyperlambda Generator
description: Magic contains a Hyperlambda AI-based generator, allowing you to create your backend APIs using natural language.
og_image: "/images/custom-chatgpt-chatbot.jpg"
header:
  image: /assets/images/wizard-magically-pulling-ai-chatbots-our-of-cauldron.webp
---

Magic contains its own Hyperlambda Generator. This isn't a single component, but goes through most parts of the platform that somehow allows you to create Hyperlambda code. It's built as a custom LLM we have fine tuned on top of OpenAI's GPT-4.1 model, with more than 20,000 training examples, so it's actually very strong on creating backend code, even though it's using a _"small base model"_.

![Screenshot of the Hyperlambda Generator creating an HTTP CRUD endpoint](/assets/images/hyperlambda-generator.png)

