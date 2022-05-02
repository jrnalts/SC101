"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        m_num, f_num = total_by_gender(tags)
        print(f'Male Number: {m_num}')
        print(f'Female Number: {f_num}')


def total_by_gender(tags):
    """
    Input:
        tags(str): content from popular baby names by web crawler.
    Output:
        m(int), f(int): summary of top 200 names by gender in decades.
    """
    m = f = 0  # Set Default of male/female number
    for tag in tags:
        for i, num in enumerate(tag.text.strip().split()):
            num = num.replace(',', '')
            if i >= 1000 and not num.isdigit():  # Only accept number / group with each 5 elements in top 200
                break
            else:
                if i % 5 == 2:
                    m += int(num)
                elif i % 5 == 4:
                    f += int(num)
    return m, f


if __name__ == '__main__':
    main()
