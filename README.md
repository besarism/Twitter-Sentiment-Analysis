

Twitter Sentiment Analysis 

Main goal of this mini-software is to identify emotional tone in the series of words that make each tweet.
You will be asked to input the location, range of location, what tweets and the amount of tweets you are searching for and you will be served with a nice scatter plot of the sentiment of the each tweet.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to install some packages to run the software including:

* Twython
* Textblob
* Geopy
* Matplotlib
* Numpy

To install those packages you can use pip, for example:

```
pip install Twython
```


## Running the tests

You can clone this repository by adding this command to the path you want to save this software:
```
git clone https://github.com/besarism/Twitter-Sentiment-Analysis.git
```
And then you locate where main.py file is and run the file:

```
python main.py
```
And then you will see a window like this

<p align="center">
<img src="https://raw.githubusercontent.com/besarism/Twitter-Sentiment-Analysis/master/images/window1.png" />
</p>

And you will be able to filter your search by your keyword, location, range of the location (miles) also you will can decide if the tweets that are going to be analyzed to be less than a day old

<p align="center">
<img src="https://raw.githubusercontent.com/besarism/Twitter-Sentiment-Analysis/master/images/window2.png" />
</p>

After you hit analyze data button, the software in background will get all the tweets matching your search criteria using Twython, will analyze their sentiment using Textblob package and finally will serve you with a really beautiful scatter plot using Matplotlib.

<p align="center">
<img src="https://raw.githubusercontent.com/besarism/Twitter-Sentiment-Analysis/master/images/window3.png" />
</p>



## Authors

* **Besar Ismaili** - *Initial work* - [@besarism](https://github.com/besarism)

See also the list of [contributors](https://github.com/besarism/Twitter-Sentiment-Analysis/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



