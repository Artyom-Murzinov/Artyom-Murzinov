def mathematics(number_list):
    try:
        n = (1000 * float(number_list[0])) / (3.14 * float(number_list[1]))
        f = float(number_list[2]) * float(number_list[3]) * n
        return int(n), int(f)
    except:
        return 'отправьте end, и выберите цикл', None


def generating_file(action, user_id):
    if action == word:
        action1 = "KK"
    elif action == word_2:
        action1 = "PK"
    elif action == word_3:
        action1 = "RK"
    if action1 == 'KK' or action1 == 'PK' or action1 == 'RK':
        new_code = open("O0001.nc", "w")
        with open(f"{action1.lower()}.txt", "r", encoding="utf-8") as pk:
            info = pk.read()
        new_code.write(user[user_id].text_nc['text'])
        with open("O0001.nc", "a") as new_code:
            new_code.write(info)
        user[user_id].text_nc["text"] += info
        return user[user_id].text_nc["text"]


def func_error(argumet, numb):
    '''Ловлю ошибку если на FLOAT'''
    try:
        float(argumet)
        numb += 1
        return numb, None
    except:
        return numb, 'Введите число'

