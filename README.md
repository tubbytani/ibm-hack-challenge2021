# OTT-recommender
A flask based REST Api is created which recommends OTT platforms to user according to various parameters.
It also takes in consideration of priority of a particular parameter.
The various steps involved were:
- Collection of datasets: Various datasets were collected for each ott platform. The main website used for this was kaggle.
-  : After segregation of certain data new CSV's were created to store the data
-  
# Live-sentiment analysis
Live tweets are fetched from twitter using Tweepy which is an open source Python package that provides a convenient way to access the Twitter API with Python.
These tweets are then categorised into positve, negative and neutral using Natural Language processing (NLP).
