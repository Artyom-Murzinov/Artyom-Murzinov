
def func_generato():
    '''Заполняю текстовый документ нужными параметрами'''
    # FIXME create state ? logic
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        user_id = message.from_user.id
        if message.text.lower() == 'end':
            bot.send_message(message.from_user.id, 'Прерываю цикл!')
            return
        number, erorrs = func_error(message.text, user[user_id].number_dict["number"])
        user[user_id].number_dict["number"] = number
        if erorrs != None:
            bot.send_message(message.from_user.id, erorrs)
        if number <= len(user[user_id].conditions['kelb']) -1:
            bot.send_message(message.from_user.id, user[user_id].conditions['kelb'][number])
    ##############################################################################
        if user[user_id].conditions['kelb'] == word or user[user_id].conditions['kelb'] == word_2 or user[user_id].conditions['kelb'] == word_3:
            '''Условие для записи G-кода'''
            if number > 0:
                user[user_id].text_nc["text"] += f"#{number} = {message.text}\n"
            if number >= len(user[user_id].conditions["kelb"]):
                gen_text = generating_file(user[user_id].conditions['kelb'], user_id)
                bot.send_message(message.from_user.id, gen_text)
                return
        elif user[user_id].conditions['kelb'] == word_4:
            '''Условие деля записи режимов резания'''
            if number > 0:
                user[user_id].working_dict["list"].append(message.text)
            if number >= len(user[user_id].conditions["kelb"]):
                turnovers, supply = mathematics(user[user_id].working_dict["list"])
                if supply != None:
                    bot.send_message(message.from_user.id, f'число оборотов = {turnovers} \nПодача = {supply}')
                else:
                    bot.send_message(message.from_user.id, turnovers)
                return
    return


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

