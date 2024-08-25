
"""class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.number_dict = {'number': 0}
        self.conditions = {'kelb': []}
        self.text_nc = {"text": "% \nO0001 \n"}
        self.working_dict = {'list': []}


def func_generato():
    '''Заполняю текстовый документ нужными параметрами'''
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


@bot.message_handler(func=lambda message: message.text == "Круглый карман")
def echo_all(message):
    user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word
    func_generato()
    return


@bot.message_handler(func=lambda message: message.text == "Прямоугольный карман")
def echo_all(message):
    user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_2
    func_generato()


@bot.message_handler(func=lambda message: message.text == "Радиусный карман")
def echo_all(message):
    user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_3
    func_generato()
    return


@bot.message_handler(func=lambda message: message.text == "Расчет режимов резания")
def echo_all(message):
    user_id = message.from_user.id
    user[user_id] = User(user_id)
    bot.send_message(message.from_user.id, 'Отправьте любую БУКВУ')
    user[user_id].conditions['kelb'] = word_4
    func_generato()
    return

"""