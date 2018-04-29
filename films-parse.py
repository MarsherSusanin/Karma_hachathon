import sys
import urllib.request
import urllib.parse
import time
import re

def is_rus(text):
    match = re.match('[а-яА-ЯёЁ]',text);#"""^[а-яА-ЯёЁ][а-яё0-9 !?:;"'.,]+$""", text)
    return bool(match)

nameMovieAll = input("Введите название фильма:");
#nameMovieAll = nameMovieAll.decode('the-existing-encoding').encode("utf-8");
s_url_en = "https://www.imdb.com/find?ref_nv_sr_fn&q="+nameMovieAll+"&s=all";
s_url_rus = "https://www.imdb.com/find?ref_=nv_sr_fn&q="+nameMovieAll+"&s=all";

# Возможность использования русских названий фильмов
#if is_rus(nameMovieAll):
#    s = s_url_rus
#else:
#    s = s_url_en;
    
s = s_url_en;
response = urllib.request.urlopen(s);

html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы
st0 = [];
st1 = [];
ps1 = html.find("findResult odd",1,len(html))+17;
ps2 = html.find("findMoreMatches",1,len(html))-26;#-27;
data = html[ps1:ps2];

st11 = "https://www.imdb.com";
while len(data) >0:
    ps1 = data.find("<td",0,len(data));
    ps2 = data.find("td>")+3;
    st0.append(data[ps1:ps2]);
    data = data[ps2:len(data)];

for i in range(1,len(st0),2):
    data = st0[i];
    ps1 = data.find("href",0,len(data))+6;
    ps2 = data.find(" ",ps1,len(data))-1;
    st1.append(st11 + data[ps1:ps2]);

l = int(len(st0)/2);
print ("Количество фильмов: "+str(l));


for i in range(1,len(st0)-1,2):
    print (st0[i]);
for i in range(l):
    print (st1[i]);

nMovie = input("Введите номер фильма:");
urlMovie = st1[int(nMovie)-1];
response = urllib.request.urlopen(urlMovie);
html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы

ps1 = html.find('<div class="title_wrapper">',1,len(html));
ps2 = html.find(">See full cast & crew</a>",1,len(html))-26;
data = html[ps1:ps2];

stMovieResult=[];
stMovieResultDesc=['Название на русском: ','Год выхода: ','Название на английском: ','Продолжительность: ','Жанр: ','Дата выхода в кинотеатрах: ','Ссылка на постер: ','Краткое описание: ','Режиссер: ','Сценарий: ','Актерский состав: '];
# Название на руссском
s1 = 'class="">';
s2 = '&nbsp;';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]); 
data = data[ps2:len(data)];
# Год выхода
s1 = '\n>';
s2 = '</a>';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]);
data = data[ps2:len(data)];
# Название на английском
s1 = 'originalTitle">';
s2 = '<span';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]);
data = data[ps2:len(data)];
# Продолжительность
s1 = 'PT126M">\n                        ';
s2 = '\n                    </time';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]);
data = data[ps2:len(data)];

# Считываем жанры
stGenre = [];
s1 = 'genre">';
s2 = '</span>';
ps1 = data.find(s1,1,len(data))+len(s1);
while ps1 >= len(s1):
    ps2 = data.find(s2,1,len(data));
    stGenre.append(data[ps1:ps2]);
    data = data[ps2:len(data)];
    ps1 = data.find(s1,1,len(data))+len(s1);

s = ', '.join(stGenre);
stMovieResult.append(s[2:len(s)]);

# Дата выхода фильма на экраны
s1 = 'release dates" >';
s2 = '\n<meta';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]);
data = data[ps2:len(data)];
# Ссылка на постер
s1 = '\nsrc="';
s2 = '"';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]);
data = data[ps2:len(data)];
# Описание фильма
s1 = 'itemprop="description">\n                    ';
s2 = '\n';#\n\n            </div>';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]);
data = data[ps2:len(data)];
# Режиссер
s1 = 'itemprop="name">';
s2 = '</span>';
ps1 = data.find(s1,1,len(data))+len(s1);
ps2 = data.find(s2,ps1,len(data));
stMovieResult.append(data[ps1:ps2]);
data = data[ps2:len(data)];

# Сценаристы
s1 = 'name">';
s2 = 'class="ghost">';
ps1 = data.find(s1,1,len(data))-10;
ps2 = data.find(s2,1,len(data));
data1 = data[ps1:ps2];
k = ps2;
stWriters = [];
s1 = 'name">';
s2 = '</span>';
ps1 = data1.find(s1,1,len(data1))+len(s1);
while ps1 >= len(s1):
    ps2 = data1.find(s2,ps1,len(data1));
    stWriters.append(data1[ps1:ps2]);
    data1 = data1[ps2:len(data1)];
    ps1 = data1.find(s1,1,len(data1))+len(s1);

s = ', '.join(stWriters);
stMovieResult.append(s[0:len(s)]);
data = data[k:len(data)];

# Актеры
s1 = 'name">';
s2 = 'class="ghost">';
ps1 = data.find(s1,1,len(data))-10;
ps2 = data.find(s2,1,len(data));
data1 = data[ps1:ps2];
k = ps2;
stStars = [];
s1 = 'name">';
s2 = '</span>';
ps1 = data1.find(s1,1,len(data1))+len(s1);
while ps1 >= len(s1):
    ps2 = data1.find(s2,ps1,len(data1));
    stStars.append(data1[ps1:ps2]);
    data1 = data1[ps2:len(data1)];
    ps1 = data1.find(s1,1,len(data1))+len(s1);

s = ', '.join(stStars);
stMovieResult.append(s[0:len(s)]);
data = data[k:len(data)];

for i in range(len(stMovieResult)):
    print (stMovieResultDesc[i]+stMovieResult[i]);

# Запись описание фильма в текстовой файл
f=open("hakaton.txt","w", encoding="utf-8");
for i in range(len(stMovieResult)):
    f.write(stMovieResultDesc[i]+stMovieResult[i]+'\n');
f.close();