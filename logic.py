from graphic_explan.dictonary import dictonary
from math import *
from mathematics.price import PriceCalculator
from mathematics.UFG import UFG
from mathematics.calculators import cutting_mode, angle_decimal


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



def data_generator(user_id, cicle, argument):
    """Функция получает от пользователя необходимые данные для дальнейшей работы с ними"""
    """И отправляет результат пользователю"""
    if cicle in list(dictonary["part_price"]):
        user[user_id].number_dict['number']+=1
        number = user[user_id].number_dict['number']
        if number < len(dictonary["part_price"][cicle])+1:                        
            if number == 0:
                user[user_id].workpiece[list(user[user_id].workpiece)[number]] = cicle
            elif number > 0:
                user[user_id].workpiece[list(user[user_id].workpiece)[number]] = argument           
            if number <= len(dictonary["part_price"][cicle])-1:
                return dictonary["part_price"][cicle][number][0], dictonary["part_price"][cicle][number][1]
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
                    den = cutting_mode(user[user_id].variable["#1"], 
                                 user[user_id].variable["#2"], 
                                 user[user_id].variable["#3"], 
                                 user[user_id].variable["#4"])
                    return f'{den}', None
                elif cicle == "degrees_decimal":
                    den = angle_decimal(user[user_id].variable["#1"], 
                                  user[user_id].variable["#2"],
                                  user[user_id].variable["#3"], 
                                  user[user_id].variable["#4"])
                    return f'{den}', None
                elif cicle == "UFG":
                    den = UFG(float(user[user_id].variable["#1"]), 
                              float(user[user_id].variable["#2"]))
                    return f"{den}", None
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
    
