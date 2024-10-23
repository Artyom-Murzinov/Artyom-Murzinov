import requests
from graphic_explan.dictonary import dictonary
from math import *
from price import *
 
user = {}
class User():
    def __init__(self, user_id):
        self.user_id = user_id
        self.number_dict = {"number": -1}
        self.conditions = {'cycle_calc': []}
        self.variable = dict()
        self.document = "% \nO0001 \n"
        self.workpiece = {"profile": None, "alloy": None, 
                     "size": None, "length": None, 
                     "wall_thickness": float()}


def exchange_rate():
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    return data['Valute']['USD']['Value'], data['Valute']['CNY']['Value']


def data_generator(user_id, cicle, argument):
    if cicle in list(dictonary["part_price"]):
        user[user_id].number_dict['number']+=1
        number = user[user_id].number_dict['number']
        if number < len(dictonary["part_price"][cicle])+1:                        
            if number == 0:
                user[user_id].workpiece[list(user[user_id].workpiece)[number]] = cicle
            elif number > 0:
                user[user_id].workpiece[list(user[user_id].workpiece)[number]] = argument           
            if number <= len(dictonary["part_price"][cicle])-1:
                return dictonary["part_price"][cicle][number], None
            elif number == len(dictonary["part_price"][cicle]):
                den = PriceCalculator(user[user_id].workpiece["profile"], 
                                user[user_id].workpiece["alloy"], 
                                user[user_id].workpiece["size"], 
                                user[user_id].workpiece["length"], 
                                user[user_id].workpiece["wall_thickness"])
                return f'{den}', None
        else:
            return "Цикл завершен, выберите следующий цикл! 👍", None
    else:        
        try:
            float(argument) 
            user[user_id].number_dict['number']+=1 
            number = user[user_id].number_dict['number']
            if number > 0:
                user[user_id].variable.update({f'#{number}': float(argument)})
            if len(dictonary[cicle]) -1 >= user[user_id].number_dict['number']:               
                if len(dictonary[cicle][number]) == 2:                
                    return dictonary[cicle][number][0], dictonary[cicle][number][1]
                else:
                    return dictonary[cicle][number], None
            elif len(dictonary[cicle]) == user[user_id].number_dict['number']:
                if cicle == "cutting_mode":
                    n = (1000 * float(user[user_id].variable["#1"]))/(3.14 * float(user[user_id].variable["#2"]))
                    f = float(user[user_id].variable["#3"]) * float(user[user_id].variable["#4"]) * n
                    return f'Число оборотов = {int(n)}об/мин, Подача = {int(f)}мм/мин 👍', None
                elif cicle == "degrees_decimal":
                    ugol = int(user[user_id].variable["#1"]) + int(user[user_id].variable["#2"])/60 + int(user[user_id].variable["#3"])/3600
                    osX = float(user[user_id].variable["#4"]) * cos(radians(ugol))
                    osY = float(user[user_id].variable["#4"]) * sin(radians(ugol))
                    return f'Угол равен = {round(ugol, 4)}, Ось X = {round(osX, 4)}, Ось Y = {round(osY, 4)} 👍', None
                elif cicle == "round_pocket" or cicle == "rectangular_pocket" or cicle == "radius_pocket" or cicle == "milling _plane" or cicle == "conical_thread":
                    for key, value in user[user_id].variable.items():
                        user[user_id].document += f'{key} = {value} \n'
                    if cicle == "round_pocket": action = "KK"   
                    elif cicle == "rectangular_pocket": action = "PK"
                    elif cicle == "radius_pocket": action = "RK"
                    elif cicle == "milling _plane": action = "FP"
                    elif cicle == "conical_thread": action = "KR"
                    with open(f"telegram_bot/file_document/{action}.txt", "r", encoding="utf-8") as pk:
                        info = pk.read()
                    new_code = open("O0001.nc", "w")
                    new_code.write(user[user_id].document)
                    with open("O0001.nc", "a") as new_code:
                        new_code.write(info)
                    user[user_id].document
                    return f'Перенесите этот файл на флешку 👆', 1   
            else:
    #            user[user_id].number_dict['number'] = 0
                return "Цикл завершен, выберите следующий цикл! 👍", None
        except:
            return 'Введите число! 🤯', None
    
