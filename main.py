#!/usr/bin/env python
# encoding: utf-8

import logging
import telegram
import random
import json
from giphypop import translate

with open('quotes.json') as data_file:
    quotes = json.load(data_file)
    rick = quotes["Rick"]
    morty = quotes["Morty"]
	beth = quotes["Beth"]
	jerry = quotes["Jerry"]
	summer = quotes["Summer"]
	extra = quotes["Extra"]

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    bot = telegram.Bot(token='HERE GOES THE TOKEN!')

    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=5):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id

            if '/start' in text:
                custom_keyboard = [["/quote", "/gif"]]
                reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
                bot.sendMessage(chat_id=chat_id,
                                text="I'm Mr. Meeseeks! Look at me!!",
                                reply_markup=reply_markup)
                LAST_UPDATE_ID = update_id + 1

            elif '/quote' in text:
                answer = quote()
                bot.sendMessage(chat_id=chat_id,
                                text=answer)
                LAST_UPDATE_ID = update_id + 1

            elif '/gif' in text:
                bot.sendMessage(chat_id=chat_id,
                                text="Ooohhh can do. ")
                img = translate('rick and morty')
                bot.sendDocument(chat_id=chat_id,
                                 document=img.fixed_height.url)
                print "Enviar Gif " + img.fixed_height.url
                LAST_UPDATE_ID = update_id + 1


def quote():
    character = random.randint(0,5)
    if character == 0:
        return "Rick: " + random.choice(rick)
    elif character == 1:
        return "Morty: "  + random.choice(morty)
	elif character == 2:
        return "Beth: "  + random.choice(beth)
	elif character == 3:
        return "Jerry: "  + random.choice(jerry)
	elif character == 4:
        return "Summer: "  + random.choice(summer)
	else
		return random.choice(extra)

if __name__ == '__main__':
    main()
