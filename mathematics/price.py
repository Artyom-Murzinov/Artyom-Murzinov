from bs4 import BeautifulSoup
import requests
import re
from math import *
import json
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("token")
headers = {"Authorization": f"OAuth {token}"}
params = {"path": "dictionary_data/metal_densities.json"}



class PriceCalculator:
    """Класс считает вес и цену заготовки"""
    def __init__(self, profile, alloy, size, length, wall_thickness):
        self.alloy_density = list()                     #Плотность сплава
        self.alloy = alloy                              #Сплав
        self.profile = profile                          #Профиль
        self.size = float(size)                         #Размер
        self.length = float(length)                     #Длина
        self.wall_thickness = float(wall_thickness)     #Толщина стенки

    def __str__(self):
        return  PriceCalculator.workpiece_cost(self)
    
    
    def alloy_search(self, alloy_grade, alloy):
        """Рекурсивная функция осуществяет поиск марку стали и записывает в виде списка марку и плотность"""
        if isinstance (alloy_grade, dict):            
            for key, value in alloy_grade.items(): 
                PriceCalculator.alloy_search(self, alloy_grade[key], alloy)
                if key.lower() == alloy.lower():
                    self.alloy_density = key, value
            return self.alloy_density
        return None

    def alloy_price_search(self):
        """Достаю из интернета стоимость сплава и высчитываю среднюю стоимость, плотность сплава"""
        price = 0
        number = 0
        patterns = r'[0-9][^a-z="<>/]*'
        yandex_url = "https://cloud-api.yandex.net/v1/disk/resources/download"
        emetal_url = f"https://e-metall.ru/{self.profile}/?item_steel_mark={self.alloy}"

        # тут из яндекс диска получаю файл json и отправялю в рекурсию 
        yandex_disk = requests.get(yandex_url, headers=headers, params=params)
        href = yandex_disk.json()['href']
        yandex_response = requests.get(href)
        yandex_response.encoding = 'utf-8'
        self.alloy_grade = yandex_response.json()
        PriceCalculator.alloy_search(self, self.alloy_grade, self.alloy)


        metal_response = requests.get(emetal_url)
        bs = BeautifulSoup(metal_response.content, "html5lib" )    
        for tag in bs.find_all('td'):
            if 'Цена, руб с НДС' in str(tag):
                try:
                    if "шт" not in str(tag):
                        if "т" in str(tag) or "кг" in str(tag):                  
                            price += float(re.findall(patterns, str(tag))[0][:-3].replace(' ', '')) 
                            number += 1               
                except:
                    pass
        try:
            self.new_price = round(price/number/1000, 2)
        except:
            self.new_price = 0
        

    def workpiece_cost(self):
        """Делаю расчет веса заготовки, средняя стоимость заготовки, средняя стоимость сплава за 1 кг"""
        PriceCalculator.alloy_price_search(self)
        try:
            if self.profile.lower() == 'круг':
                body_weight = (pi * self.size**2/4 * self.length * self.alloy_density[1][0]) / 1000000
            elif self.profile.lower() == 'квадрат':
                body_weight = (self.size**2 * self.length * self.alloy_density[1][0]) / 1000000
            elif self.profile.lower() == 'шестигранник':
                body_weight = (((self.size/2)**2/sqrt(3))*6 * self.length * self.alloy_density[1][0]) / 1000000
            elif self.profile.lower() == 'труба':
                body_weight = (((pi * self.size**2 / 4) - (pi * (self.size - self.wall_thickness * 2)**2 / 4))* self.length * self.alloy_density[1][0])/1000000
            elif self.profile.lower() == 'лист':
                body_weight = (self.size * self.wall_thickness * self.length * self.alloy_density[1][0]) / 1000000
            return f'Средняя цена за кг={self.new_price}руб, Масса заготовки={round(body_weight, 4)}кг, Стоимость заготовки={round(body_weight * self.new_price, 2)}руб'
        except:
            return f'Такого нет, в скором появится, извините!😊'


#alloy='40х'
#profile = "круг"
#size = 25      #Размер 
#wall_thickness = None
#length = 300 #Длина заготовки

#density = PriceCalculator(profile, alloy, size, length, wall_thickness)
#print(density)
