# OTT-recommender
A flask based REST Api is created which recommends OTT platforms to user according to various parameters.
It also takes in consideration of priority of a particular parameter.
The various steps involved were:
- Collection of datasets: Various datasets were collected for each ott platform. The main website used for this was kaggle.
-  The main python file is created using Exploratory data analysis: After segregation of certain data new CSV's were created to store the data
-  
# Live-sentiment analysis
Live tweets are fetched from twitter using Tweepy which is an open source Python package that provides a convenient way to access the Twitter API with Python.
After providing necessary tokens to authenticate our requests tweets are fetched from twitter.
Pagination is used a lot in Twitter API developmen for example in iterating through timelines, user lists, direct messages, etc. In order to perform pagination and to make the process easier we are using Tweepy's Cursor object.
We are fetching 100 tweets at a time.
We the iterate through the tweets and apply
Vader
It uses a list of lexical features (e.g. word) which are labeled as positive or negative according to their semantic orientation to calculate the text sentiment. Vader sentiment returns the probability of a given input sentence to be positive, negative, and neutral.

Then an App is created using flask framework which runs with Gunicorn Python WSGI HTTP server which handles Post requests.
The app provides an interface between the main python file and the Web UI.





