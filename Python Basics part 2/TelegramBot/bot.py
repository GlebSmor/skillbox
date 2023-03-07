import telebot
import requests
import json
from config import TOKEN
from telebot import types
from telebot.types import Message

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message):
    with open('users.json', 'r') as file:
        data_from_json = json.load(file)

    user_id = message.from_user.id
    username = message.from_user.username

    if str(user_id) not in data_from_json:
        data_from_json[user_id] = {'username': username}
        data_from_json[user_id]['history'] = []
        data_from_json[user_id]['cocktail'] = ''

    with open('users.json', 'w') as file:
        json.dump(data_from_json, file, indent=4)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search = types.KeyboardButton('🔍Search')
    history = types.KeyboardButton('🕓History')
    markup.add(search, history)
    bot.send_message(chat_id=message.chat.id, text=f'Hello {message.from_user.first_name}!\n'
                                                   f'This is cocktail recipes bot.\n'
                                                   f'Here you can find recipes for your favorite cocktails\n\n\n'
                                                   f'Bot based on https://www.thecocktaildb.com',
                     reply_markup=markup)


def pick_cocktail_handle(message: Message):
    mess = ''
    count = 0
    with open('users.json', 'r') as file:
        data_from_json = json.load(file)
        name, qty = data_from_json[str(message.from_user.id)]['cocktail'].split('-')
        qty = int(qty)

    if message.text.isdigit() and 1 <= int(message.text) <= qty:
        response = json.loads(requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + name).text)
        cocktails = [response['drinks'][x] for x in range(0, len(response['drinks']))]
        cocktail = cocktails[int(message.text) - 1]
        mess += f'Name: {cocktail["strDrink"]}\n'
        mess += '\n\nIngredients\n\n'

        for ingredient in cocktail:
            if cocktail[ingredient] and 'strIngredient' in ingredient:
                count += 1
                if cocktail["strMeasure" + str(count)]:
                    mess += f'    {cocktail[ingredient]}: {cocktail["strMeasure" + str(count)]}\n'
                else:
                    mess += f'    {cocktail[ingredient]}\n'

        instruction = cocktail['strInstructions'].split('.')

        mess += '\n\nInstruction\n\n'
        for string in range(0, len(instruction) - 1):
            instruction[string] = instruction[string].strip() + '.'
        mess += '\n'.join(instruction)

        with open('users.json', 'r') as file:
            data_from_json = json.load(file)
        history = data_from_json[str(message.from_user.id)]['history']

        if len(history) == 5:
            history.pop(0)
        history.append(mess)
        with open('users.json', 'w') as file:
            json.dump(data_from_json, file, indent=4)

    else:
        mess = 'Input error'
        bot.register_next_step_handler(message, callback=pick_cocktail_handle)

    bot.send_message(chat_id=message.chat.id, text=mess)


def search_drink_handle(message: Message):
    mess = ''
    name = message.text

    response = json.loads(requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + name).text)
    try:
        cocktails = [response['drinks'][x] for x in range(0, len(response['drinks']))]
        count = 0
        for cocktail in cocktails:
            mess += f'{count + 1} - {cocktail["strDrink"]}\n'
            count += 1
        with open('users.json', 'r') as file:
            data_from_json = json.load(file)
            data_from_json[str(message.from_user.id)]['cocktail'] = name + '-' + str(count)
        with open('users.json', 'w') as file:
            json.dump(data_from_json, file, indent=4, ensure_ascii=False)

        bot.send_message(chat_id=message.chat.id, text=f'Pick cocktail number (1-{count}):')
        bot.send_message(chat_id=message.chat.id, text=mess)
        bot.register_next_step_handler(message, callback=pick_cocktail_handle)
    except TypeError:
        mess = 'No drinks found'
        bot.reply_to(message, text=mess)


@bot.message_handler(content_types=['text'])
def search_drink(message: Message):
    if message.text == '🔍Search':
        bot.send_message(chat_id=message.chat.id, text='Enter the cocktail name:')
        bot.register_next_step_handler(message, callback=search_drink_handle)
    elif message.text == '🕓History':
        with open('users.json', 'r') as file:
            data_from_json = json.load(file)
        history = data_from_json[str(message.from_user.id)]['history']
        for elem in history:
            bot.send_message(chat_id=message.chat.id, text=elem)


bot.polling()