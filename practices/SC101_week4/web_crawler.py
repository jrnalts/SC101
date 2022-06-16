import requests 
from bs4 import BeautifulSoup


def main():
    res = requests.get('https://www.imdb.com/chart/top/')
    tags = BeautifulSoup(res.text).find_all('td', {'class', 'titleColumn'})
    d = {}
    for tag in tags:
        year = tag.span.text
        if year in d:
            d[year] += 1
        else:
            d[year] = 1
    for year, count in sorted(d.items(), key=lambda e: e[1]):
        print(f'{year}: {count}')




if __name__ == '__main__':
    main()
