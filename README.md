# OTT- Recommender
A Flask based REST Api is created which responds with a recommendation of an OTT platform(s) to the user according based on the choices that the user makes.
The result of which also takes in consideration of which feature to be given higher priority.
The various steps involved were:
-  Collection of datasets: Various datasets were collected for each OTT platform. The major reference for the data was Kaggle
-  We initialise a Watson Notebook for the performing operations pertaining to data cleaning and eventual analysis of OTT platforms.
-  After data cleaning, we analyzed the data and performed Exploratory data analysis to get an idea of different features.
-  We needed few common measures of comparison like Language, Age Rating, IMDb and genre, so we resorted to converting them upto a common scale to be compared accordingly
-  These features were finally used to formulate our Recommender algorithm.
# Sentiment Analysis
1. **OTT Review** <br>
After successfully scraping different opinions and reviews of people on the respective OTTs being analyzed in this project, we performed sentiment analysis on the data we had. We resorted to many preprocessing techniques at the core of which was **VADER** Model. Final sentiment data was sent to the React UI dashboard to be shown to the user as interpretable data.
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
 
The Apps are created using **Flask framework (by Python)** which runs with **Gunicorn Python WSGI HTTP server which handles POST requests**
The app provides an interface layer between the main python file and the React UI.





