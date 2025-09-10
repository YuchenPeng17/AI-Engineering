# AI-Engineering

> Build AI Powered Products
> 

### **Source:**

- [platform.openai.com](https://platform.openai.com/)
- [platform.openai.com/docs/api-reference](https://platform.openai.com/docs/api-reference/introduction)
- [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)

---

Project 1. Build a Character AI Chatbot

This project builds a Character AI Chatbot powered by the OpenAI API.

### Focus Areas

- Configure the OpenAI API and manage the API key securely
- Interact with AI models and interpret their outputs
- Understand the concept of tokens and their impact
- Use system prompts to shape the AI’s personality and behavior

**What is a Token?**

- In OpenAI’s language models, a token is a unit of text — often a word, part of a word, or even a single character — that the model processes
- Text isn’t read like humans do; instead, a tokeniser splits it into tokens and maps them to numerical IDs the model understands
- The model learns patterns and relationships between tokens to predict the next one in a sequence, which is how it generates coherent responses
- As a rule of thumb, 1 token ≈ 4 characters of English text, or about ¾ of a word (so ~100 tokens ≈ 75 words)

---

## Project 2. Build a Calorie Tracker

This project demonstrates a Calorie Tracker app that leverages AI vision to identify food from images and estimate nutritional information.

### Focus Areas

- Using AI vision model APIs
- Applying prompt engineering (context, instruction, input, and output)
- Understanding zero-shot, few-shot, and chain-of-thought prompting
- Converting images into base64-encoded strings for OpenAI API calls

### Prompt Engineering Fundamentals

**What is Prompt Engineering?**

- The practice of designing and optimising prompts to guide generative AI models toward desired outputs
- Art of effective communication with AI

**Prompt Components**

- Context: Background information that frames the task
    - *“Assume you are an expert financial analyst.”*
- Instruction: A clear statement of the goal
    - *“Classify the following text as positive, neutral, or negative.”*
- Input Data: The specific data the model should process
    - *“Apple stock increased by 2% in today’s trading session.”*
- Output Indicator: Defines the expected format of the response
    - *“Sentiment: ”*

**Prompting Strategies**

- Zero-shot: Ask the model to do a task without giving any examples
- Few-shot: Provide a few examples of input-output pairs before the actual query
- Chain-of-thought: Ask the model to to reason step by step before giving the answer