from bs4 import BeautifulSoup
import requests
import pandas as pd

compilado = []

def scrape(input):
       for i in input:
        if (i.find('div', class_='title1')): 
            list = {
                'car': i.find('div', class_='title1').text,
                'details': i.find('div', class_='title2').text,
                'price': i.find('div', class_='price').text,
                'picture': i.find('img', class_='real')['src']
                }
            compilado.append(list)

for e in range(1,42):
    url = requests.get(f'https://www.supercarros.com/carros/cualquier-tipo/cualquier-provincia/ver-todos/?PagingPageSkip={e}').text
    
    soup = BeautifulSoup(url, 'lxml')

    promos = soup.find_all('li', class_='normal promo-ANADIVE')
    normal = soup.find_all('li', class_='normal')  
    special = soup.find_all('li', class_='special')
    
    scrape(normal)
    scrape(promos)
    scrape(special)
   
    df = pd.DataFrame(compilado,columns=compilado[0].keys())
    
    print(df)

df.to_csv('carros_scrapping.csv')