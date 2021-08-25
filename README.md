# OTT- Recommender
A Flask based REST Api is created which responds with a recommendation of an OTT platform(s) to the user based on the choices that the user makes.
The result also takes in consideration of the features which are given higher priority by the user.
The various steps involved were:
-  Collection of datasets: Various datasets were collected for each OTT platform. The major reference for the data was Kaggle
-  We initialise a [Watson Studio Notebook](https://eu-gb.dataplatform.cloud.ibm.com/analytics/notebooks/v2/d7f89838-67bc-421b-bf72-ff9c33a5d4eb/view?access_token=05d7c8d20083ba2d73e4cd1d3cff4ef57e7b104bfb679014ecacbe1a0a761992)  for the performing operations pertaining to data cleaning and eventual analysis of OTT platforms.
-  After data cleaning, we analyzed the data and performed EDA (Exploratory Data Analysis) to get an idea of different features.
-  We needed few common measures of comparison like Language, Age Rating, IMDb and genre, so we resorted to converting them upto a common scale to be compared accordingly
-  These features were finally used to formulate our Recommender algorithm.
-  The output of recommender is then sent to the UI with the help of Flask framework deployed on IBM cloud.
# Sentiment Analysis
1. **OTT Review** <br>
After successfully scraping different opinions and reviews of people on the respective OTTs being analyzed in this project, we performed sentiment analysis on the data we had. We resorted to many preprocessing techniques at the core of which was **VADER** Model. Furthermore, we calculated the frequency of Keywords for building a WordCloud. Final metadata was sent to the React UI dashboard to be shown to the user as interpretable data. <br>
[Check out the Watson Notebook!](https://eu-gb.dataplatform.cloud.ibm.com/analytics/notebooks/v2/a7496980-1878-4e14-aea4-ff1261c03905/view?access_token=775c4c63558a50c5db29d8acda6e4b12a49b683f1c1dde67fcad1c56f793c7d9)
2. **LIVE @Twitter** <br> 
Live tweets are fetched from twitter using **Tweepy** which is an open source Python package that provides a convenient way to access the Twitter API with Python.
After providing necessary credentials to authenticate our requests tweets are fetched from twitter. <br>
Pagination is used a lot in Twitter API development for example in iterating through timelines, user lists, direct messages, etc. In order to perform pagination and to make the process easier we are using **Tweepy's Cursor object**. 
## Flow of Twitter
- Request to Fetch 100 real-time tweets based on specially OTT-specific keywords
- Cleaning the tweets, removing duplicates and applying Preprocessing
- The final Tweets are iterated through our software stack, involving **VADER**
## About VADER
VADER ( Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity of emotion. It uses a list of lexical features (e.g. word) which are labeled as positive or negative according to their semantic orientation to calculate the text sentiment. Vader sentiment returns the probability of a given input sentence to be positive, negative, and neutral. We chose this algorithm because it is well optimized for social media data and can yield fine results when used with unstructured data from Twitter.

## APP Creation
The Apps are created using **Flask framework (by Python)** which runs with **Gunicorn Python WSGI HTTP server which handles POST requests**
The app provides an interface layer between the main python file and the React UI.
Various parts of the app:
- manifest.yaml: The file is an application deployment descriptor. This means that it contains information needed to deploy the application on cloud doundry
- requirements.txt: This file is used for specifying what python packages which are required to run the project.
- nltk.txt: This file consists of a list of corpora to be installed to run the project.
- Main app file
- Main sentiment/recommender python file




