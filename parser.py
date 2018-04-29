from bs4 import BeautifulSoup
import requests, re, urllib.parse, urllib.request

def get_html(url):
    response=urllib.request.urlopen(url)
    return response.read()

def parse (html):
    soup = BeautifulSoup(html,'html.parser')
    tittle=soup.find('p', class_="Title")
    print (tittle.prettify())


def main ():
    parse(get_html('https://www.filmpro.ru/materials/selections/63250'))
    

if __name__=='__main__':
    main()
