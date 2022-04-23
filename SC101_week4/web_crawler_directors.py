"""
File: web_crawler_directors.py
Name:
--------------------------
This file demonstrates how to get
directors who appear on www.imdb.com/chart/top
most frequently! Do you know who is the top one?
Let's use Python code to dig out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html)
	#########################
	#                       #
	#         TODO:         #
	#                       #
	#########################


if __name__ == '__main__':
	main()
