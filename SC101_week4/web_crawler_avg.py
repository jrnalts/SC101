"""
File: web_crawler_avg.py
Name:
--------------------------
This file demonstrates how to get
averages on www.imdb.com/chart/top
Do you know the average score of 250 movies?
Let's use Python code to find out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	res = requests.get('https://www.imdb.com/chart/top/')
	tags = BeautifulSoup(res.text).find_all('td', {'class', 'ratingColumn imdbRating'})
	total = 0
	for tag in tags:
		rate = tag.text
		total += float(rate)
	print(total/250)


if __name__ == '__main__':
	main()
