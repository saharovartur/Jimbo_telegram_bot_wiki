import telebot, wikipedia, re


bot = telebot.TeleBot("TOKEN")

wikipedia.set_lang("ru")


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        wikimas = wikitext.split(".")
        # Убираем все после последней точки
        wikimas = wikimas[:-1]
        wikitext2 = ""

        for x in wikimas:
            if not ("==" in x):
                if len((x.strip())) > 3:
                    wikitext2 = wikitext2 + x + "."
            else:
                break

        # Убираем разметку
        wikitext2 = re.sub("\([^()]*\)", "", wikitext2)
        wikitext2 = re.sub("\([^()]*\)", "", wikitext2)
        wikitext2 = re.sub("\{[^\{\}]*\}", "", wikitext2)

        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return "Прости, ничего не нашел об этом :("


@bot.message_handler(commands=["start"])
def start(m, res=False):
    """
    Функция, обрабатывающая команду /start
    """
    bot.send_message(
        m.chat.id,
        "Привет, меня зовут Джимбо! Отправь мне любое слово, и я найду его значение на Wikipedia!",
    )


@bot.message_handler(content_types=["text"])
def handle_text(message):
    """
    Получение сообщений от юзера
    """
    bot.send_message(message.chat.id, getwiki(message.text))


# Запускаем бота
bot.polling(none_stop=True, interval=0)

