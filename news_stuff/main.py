from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

"""
	This module uses vader to predict positive/negative valance of 
	a news article database pulled from kaggle. I am going to look
	at this relationship over time for a set of news sources.
"""


"""
	Pulls the columns from the desired news sources
	from the pandas dataframe
"""
def pull_news_sources(input_df, news_sources):
	pass

"""
	List the most commonly used sources
"""






if __name__ == "__main__":
	file = "uci-news-aggregator.csv"
	dataframe = pd.read_csv(file)
	# get the following news sources from the dataframe
	news_sources = ["nytimes.com", "wsj.com", "theguardian.com"]

