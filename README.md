# Heart Disease Predector
This project is about creating a Heart Disease Predector using Supervised Learning.

## Introduction  
Having a healthy body is the key for you to achieve all the things/goals that you have been dreamed of. While our heart is the engine of our body, but not so much people really pay attention to it until a heart failure catch them off guard.  

This is why I think early detection of heart disease is very important. So people can be treated earlier and possibly saving their life. This is why I want to build a system to help doctors better classify or reinforce their decisions. And hopefully that could also possibly saves medical expenses, productivity lost, and more importantly saving a friend or family member of someone.  

For complete write-up of this project, please go to my post on [medium](https://medium.com/@kahousio/will-you-have-heart-disease-a-heart-disease-predictor-using-machine-learning-38df796f562d).

## Project Design
The problem that I am trying to solve is to predict/classify whether a person has heart disease or not based on some of the personal info and medical test results.  

That is my primary goal of my project, and the second goal of my project is to build a heart disease predictor - a demo app using Flask.
For model evaluation, I will use recall score as my primary metric. Because I want to take into account those cases where I predict someone is healthy but they actually have heart disease. I also pay attention to precision score when I am evaluating a model, because I don't want to tell someone that he/she has heart disease but they actually don't. This will get people upset/depressed and we don't want that.  

## Getting Started
* `notebooks` - My code for exploratory data analysis and my modelings are in this folder. 
* `web_app` - This folder contains the HTML, CSS, pickle file, and api for my web app.  
* `presentation` - This is the deck that I used to present in [Metis](https://www.thisismetis.com/). For references, please refer to the reference page in my deck.

