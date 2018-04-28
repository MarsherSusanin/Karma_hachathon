import bs4, requests, re

site=requests.get("https://www.google.com/search?q=фильмы&stick=H4sIAAAAAAAAAONgfcSYxi3w8sc9YanYSWtOXmMM5-L0Tc1NSi0q9k8T8uLics7PyUlNLsnMzxPS4RKVEtRPhgvop2Xm5BZrMEgJc2EKS_FZ8VxsubDjwu6LPRf2XOzmAQBhpmC-awAAAA&npsic=0&sa=X&ved=0ahUKEwizv_Wg5tzaAhUhG5oKHSCXAioQ1i8IIjAK")

#html_result=bs4.BeautifulSoup(site.text,'html.parser')

pattern= re.search(r'[aria-label=]["^"]',site)

#tittle=html_result.select('aria-label=')

#NameMovie = tittle[0].getText()

print(pattern)