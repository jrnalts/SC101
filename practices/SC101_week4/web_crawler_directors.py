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
	res = requests.get('https://www.imdb.com/chart/top/')
	tags = BeautifulSoup(res.text).find_all('td', {'class', 'titleColumn'})
	d = {}
	for tag in tags:
		director = tag.a['title'].split(',')[0]
		if director in d:
			d[director] += 1
		else:
			d[director] = 1
	for director, count in sorted(d.items(), key=lambda e: e[1]):
		print(f'{director}: {count}')


if __name__ == '__main__':
	main()
