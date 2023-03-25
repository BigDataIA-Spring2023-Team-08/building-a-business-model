# Building-a-business-model

> [🛝 PPT Link](https://docs.google.com/presentation/d/1CYUElHtByr4YBcTA7xzKUfK2-v7FuVPpQEiReKUxTGE/edit?usp=sharing)

## HungryPanda Application


![Image post-bro](https://user-images.githubusercontent.com/46862684/227663520-b29b2e7c-90c1-490f-b5eb-38d68166dcd0.svg)



## Description
Built a business model for a food blogging and Restaurant review application named **'HungryPanda'** using examples of the OpenAI models. Our business model uses 13 examples from this. Out of which we have productionized 4 examples! 

## Objective
1) Assist users to create food recipes based on available ingredients using **OpenAI's Recipe Creator** generative model.
2) Provide a user friendly experience by enabling translation using **OpenAI's English to Other Languages** Model.
3) Generate a personalized ad for restaurants using **OpenAI's Ad from Product Description** Model.

## OpenAI Models

**Recipe Creator**

***Settings***
Engine: text-davinci-003
Max tokens: 120
Temperature: 0.3
Top p: 1.0
Frequency penalty: 0.0
Presence penalty: 0.0

```
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a recipe based on these ingredients and instructions:\n\nFrito Pie\n\nIngredients:\nFritos\nChili\nShredded cheddar cheese\nSweet white or red onions, diced small\nSour cream\n\nInstructions:",
  temperature=0.3,
  max_tokens=120,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
```
**English to Other Languages**

***Settings***
Engine: text-davinci-003
Max tokens: 100
Temperature: 0.3
Top p: 1.0
Frequency penalty: 0.0
Presence penalty: 0.0

```
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Translate this into 1. French, 2. Spanish and 3. Japanese:\n\nWhat rooms do you have available?\n\n1.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
```

**Ad from Product Description**

***Settings***
Engine: text-davinci-003
Max tokens: 100
Temperature: 0.5
Top p: 1.0
Frequency penalty: 0.0
Presence penalty: 0.0

```
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a creative ad for the following product to run on Facebook aimed at parents:\n\nProduct: Learning Room is a virtual environment to help students from kindergarten to high school excel in school.",
  temperature=0.5,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
```
