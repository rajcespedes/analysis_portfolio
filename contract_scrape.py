from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get('https://www.spotrac.com/mlb/los-angeles-dodgers/overview/_/year/2024/sort/cap_total2').text

soup = BeautifulSoup(url, 'lxml')

list = {
    'name': [],
    'position': [],
    'age': [],
    'salary': []
}

compilation = []

retained = soup.find_all('table')

def set_df(data):
    retained_name = data.find_all('a', class_='link')

    for index, i in enumerate(retained_name):
        list['name'].append(i.text.strip())
    
    retained_position = data.find_all('td', class_='text-center details-sm')

    for index, i in enumerate(retained_position):    
        if ( index % 2 == 0):
            list['position'].append(i.text.strip())
        else:
            list['age'].append(i.text.strip())
    
    retained_salary = data.find_all('td', class_='text-center contract contract-cap_total2 highlight')

    for index, i in enumerate(retained_salary):
        list['salary'].append(i.text.strip())


def set_df_diff(data):

    accum = 0

    retained_name = data.find_all('a', class_='link')

    for index, i in enumerate(retained_name):
        list['name'].append(i.text.strip())

    for index, i in enumerate(data.find_all('td', class_='text-center details-sm')): 
        if(i.text.strip()): 
            accum += 1
            if(accum % 2 == 0):
                print(index, i.text.strip())
                list['age'].append(i.text.strip())
            else:
                list['position'].append(i.text.strip())
                
    retained_salary = data.find_all('td', class_='text-center contract contract-cap_total2 highlight')

    for index, i in enumerate(retained_salary):
        list['salary'].append(i.text.strip())


set_df(retained[0])

set_df(retained[3])

set_df_diff(retained[7])

print(f'''ammounts for, name {len(list['name'])}, position {len(list['position'])}, age {len(list['age'])} and salary {len(list['salary'])} ''')

print(list)

df = pd.DataFrame(list, columns=list.keys())

print(df)

df.to_csv('dodgers_salaries.csv')