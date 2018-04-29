from bs4 import BeautifulSoup
import requests, re, urllib.parse, urllib.request

def get_html(url):
    response=urllib.request.urlopen(url)
    return response.read()

def parse (html):
    soup = BeautifulSoup(html,'html.parser') #Превращаем сайт в html текст
    title=soup.find_all('div', class_='itemevent__head__name') # Ищем все контейнеры div с классом имени фильма

    names=title.find('a')[0:]
    print(title)


    #print (title)
    #print (alltitles)


def main ():
    parse(get_html('https://kino.mail.ru/cinema/selection/2675_15_festivalnih_filmov_kotorie_neskuchno_smotret/'))


if __name__=='__main__':
    main()
