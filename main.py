import tkinter as tk                                     # tkinter - ui package
from geopy.geocoders import Nominatim                    #
import certifi                                           # ssl, certifi - to avoid -
import ssl                                               # - some errors that disable using geopy
import geopy.geocoders                                   # geopy - package used to get the location
ctx = ssl.create_default_context(cafile=certifi.where()) #
geopy.geocoders.options.default_ssl_context = ctx        #
from textblob import TextBlob							 # textblob - package used for sentiment analysis
from twython import Twython, TwythonError				 # twython - Python wrapper for the Twitter API
import matplotlib										 # matplotlib - Matplotlib is a Python 2D plotting library
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm
import datetime											 # datetime - helps us to get current day date
import time												 # time - helps us to format created_date of the particular tweet


APP_KEY = 'ENTER'
APP_SECRET = 'ENTER'
OAUTH_TOKEN = 'ENTER'
OAUTH_TOKEN_SECRET = 'ENTER'

twitter = Twython (
	APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
)

# functions and vars
now = datetime.datetime.now()
filter_date = False
date_today = now.strftime("%Y-%m-%d")

def check_action1():
	global filter_date
	filter_date = not filter_date
	print(filter_date)

def check_action2():
	# do something
	print("check action 2")

cordinates = ""
address = ""
def get_location():
	global cordinates
	global address
	address = address_entry.get()
	geolocator = Nominatim()
	if address == "":
		# default value
		address = "Tollbugata 8A, 0152 Oslo" # ELA AS offices
	print(address)
	location = geolocator.geocode(address)
	address_label.config(text=f"Address: {location.address}")
	load_data_button.config(state=tk.NORMAL)
	print(location.latitude, location.longitude)
	cordinates = f"{location.latitude},{location.longitude}"

def get_polarity(text):
	blob = TextBlob(text)
	print(text)
	sentiment = blob.sentiment
	polarity = sentiment.polarity
	return polarity


search_text = ""
def load_data():
	# do something
	global cordinates
	global search_text
	search_text = "ELA AS" if text_entry.get() == "" else text_entry.get()
	no_of_tweets = "100" if number_entry.get() == "" else number_entry.get()
	range = "50" if range_entry.get() == "" else range_entry.get()
	geocode = f"{cordinates},{range}mi"
	search_result = twitter.search(q=search_text, count=no_of_tweets, geocode=geocode)
	tweets = search_result['statuses']
	polarity_list = []
	number_of_tweets = []
	for i,tweet in enumerate(tweets):
		print(i)
		print(tweet['created_at'])
		print("==============================================")
		if filter_date:
			tweet_created_date = time.strftime('%Y-%m-%d', time.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
			if tweet_created_date == date_today:
				text = tweet['text']
				polarity = get_polarity(text)
				polarity_list.append(polarity)
				number_of_tweets.append(i + 1)
			else:
				print("This tweets is rejected because is more than a day old")
		else:
			text = tweet['text']
			polarity = get_polarity(text)
			polarity_list.append(polarity)
			number_of_tweets.append(i + 1)


	print(len(number_of_tweets), len(tweets))

	axes = plt.gca()
	axes.set_ylim([-2, 2])
	print(number_of_tweets)
	print(polarity_list)



	cs = plt.scatter(number_of_tweets, polarity_list, c=polarity_list, cmap=cm.jet, vmin=-2., vmax=2., alpha=0.8)
	plt.colorbar(cs)


	plt.title(f"Sentiment of {search_text} in {address}")
	plt.xlabel("# of Tweets analyzed")
	plt.ylabel("Sentiment")
	plt.show()

# here we setup the UI

window = tk.Tk()
window.title("ELA Sentiment Analysis")
window.geometry("700x400")

# Application title label
title_label = tk.Label(text="ELA AS - Twitter data analysis")
title_label.place(x=350, y=20, anchor="center")

# Other UI elements

# 			get location
input_address_label = tk.Label(text="Input the address to get the location")
input_address_label.place(x=350, y=80, anchor="center")

address_label = tk.Label(text="Address: ")
address_label.place(x=350, y=135, anchor="center")

address_entry = tk.Entry(justify='center')
address_entry.place(x=350, y=105, anchor="center")

# range_entry = tk.Entry(justify='center')
# range_entry.place(x=480, y=105, width=50, anchor="center")

address_button = tk.Button(text="Locate", command=get_location)
address_button.place(x=350, y=165, anchor="center")


# 			search for tweets

input_text_label = tk.Label(text="Input the text and the # of tweets you want to search: ")
input_text_label.place(x=350, y=220, anchor="center")

text_entry = tk.Entry(justify='center')
text_entry.place(x=350, y=250, anchor="center")

number_entry = tk.Entry(justify='center')
number_entry.place(x=480, y=250, width=50, anchor="center")

input_range_label = tk.Label(text="Range of the address (miles): ")
input_range_label.place(x=350, y=280, anchor="center")

range_entry = tk.Entry(justify='center')
range_entry.place(x=480, y=280, width=50, anchor="center")

load_data_button = tk.Button(text="Analyze data",state=tk.DISABLED, command=load_data)
load_data_button.place(x=350, y=310, anchor="center")

date_checkbutton = tk.Checkbutton(text="Only tweets of today", command=check_action1)
date_checkbutton.place(x=350, y=350, anchor="center")


window.mainloop()
