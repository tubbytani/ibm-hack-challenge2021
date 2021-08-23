# OTT- Recommender
A flask based REST Api is created which recommends OTT platforms to user according to various parameters.
It also takes in consideration of priority of a particular parameter.
The various steps involved were:
- Collection of datasets: Various datasets were collected for each ott platform. The main website used for this was kaggle.
-  The main python file is created using Exploratory data analysis: After segregation of certain data new CSV's were created to store the data
-  
# Sentiment Analysis
1. **OTT Review** <br>
After successfully scraping different opinions and reviews of people on the respective OTTs being analyzed in this project, we performed sentiment analysis on the data we had. We resorted to many preprocessing techniques at the core of which was **VADER** Model. 
2. **LIVE @Twitter** <br> 
Live tweets are fetched from twitter using **Tweepy** which is an open source Python package that provides a convenient way to access the Twitter API with Python.
After providing necessary credentials to authenticate our requests tweets are fetched from twitter. <br>
Pagination is used a lot in Twitter API development for example in iterating through timelines, user lists, direct messages, etc. In order to perform pagination and to make the process easier we are using **Tweepy's Cursor object**. <br>
## Flow
- Request to Fetch 100 real-time tweets based on specially OTT-specific keywords
- Cleaning the tweets, removing duplicates and applying Preprocessing
- The final Tweets are iterated through our software stack, involving **VADER**
### VADER
VADER ( Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity of emotion. It uses a list of lexical features (e.g. word) which are labeled as positive or negative according to their semantic orientation to calculate the text sentiment. Vader sentiment returns the probability of a given input sentence to be positive, negative, and neutral. We chose this algorithm because it is well optimized for social media data and can yield fine results when used with unstructured data from Twitter.
 
Then an App is created using **Flask framework (by Python)** which runs with Gunicorn Python WSGI HTTP server which handles POST requests.
The app provides an interface layer between the main python file and the React UI.





