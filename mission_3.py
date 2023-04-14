from telegram.ext import Application, MessageHandler, filters, ConversationHandler
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import ReplyKeyboardMarkup


async def start(update, context):
    reply_keyboard = [['Начать']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('(События после того, как узнали, что у вас новое задание)', reply_markup=markup)
    return 1


async def dialog_1(update, context):
    reply_keyboard = [['*Высказать свои опасения*', '*Ничего не говорить*']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        'Вы приехали к старому дому. Задумались: \"Как здесь может кто-то жить ,а уж тем более шуметь?\"',
        reply_markup=markup)
    return 2


async def dialog_2(update, context):
    text = update.message.text
    if text == '*Высказать свои опасения*':
        await update.message.reply_text(
            'Конор - Хэнк, вы уверены, что сюда безопасно заходить?\n '
            'Хэнк - Да чего ты боишься? Ты наполовину железный. Тебя не убьёт')
    reply_keyboard = [['*Промолчать*', '*Ответить*']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        'Вы заходите в дом. Поднимаетесь на последний этаж. Как только вы поднялись, вы слышите грохот\n'
        'Хэнк - Ты слышал?',
        reply_markup=markup)
    return 3


async def dialog_3(update, context):
    text = update.message.text
    if text == '*Промолчать*':
        await update.message.reply_text("Хэнк - Вечно вы такие молчаливые, когда надо? Шум был оттуда!")
    elif text == '*Ответить*':
        await update.message.reply_text("Конор - Да. Это было в той стороне!\nХэнк - Без сопливых разберусь. Идём!")
    reply_keyboard = [['*Пойти вперед*', '*Пойти налево*', '*Пойти направо*']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Вы подходите к закрытой двери. Хэнк выбивает её. Вы входите в квартиру.\nПеред вами 3 двери",
        reply_markup=markup)
    return 4


async def dialog_4(update, context):
    text = update.message.text
    if text == '*Пойти вперед*':
        await update.message.reply_text('Конор - Я пойду осмотрюсь там!\nХэнк - Хорошо. Иди туда')
    elif text in ['*Пойти налево*', '*Пойти направо*']:
        await update.message.reply_text(
            'Конор - Я пойду осмотрюсь там!\nХэнк - Эй! Ты куда пошёл? Я там осмотрюсь. Лучше посмотри там! '
            '*Указывает направление*')
    reply_keyboard = [['*Посмотреть на книгу*', '*Осмотреть кресло*', '*Осмотреть холодильник*']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Вы заходите в комнату. В комнате стоит мебель. "
        "Обустроено так, как будто тут кто-то живёт. "
        "Вы решили осмотреться и заметили пару интересных объектов: "
        "на столе лежит книга, в углу стоит кресло, рядом с плитой стоит холодильник", reply_markup=markup)
    return 5


async def dialog_5(update, context):
    text = update.message.text
    if text == '*Посмотреть на книгу*':
        reply_keyboard = [['*Посмотреть на книгу*', '*Осмотреть кресло*', '*Осмотреть холодильник*']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            'Вы подошли к книге. '
            'Она написана каким-то шифром. '
            'Чтобы его расшифровать понадобится много времени. '
            'Вы откладываете книгу и добыв улику возврашаетесь назад.', reply_markup=markup)
        return 5
    elif text == '*Осмотреть кресло*':
        reply_keyboard = [['*Просканировать кресло*', '*Вернуться назад*']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text("Вы подходите к нему и видите грязные следы", reply_markup=markup)
        return 6
    elif text == '*Осмотреть холодильник*':
        reply_keyboard = [['*Посмотреть на книгу*', '*Осмотреть кресло*', '*Осмотреть холодильник*']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Вы открываете холодильник. "
            "В нём нет продуктов. На плите тоже пусто. "
            "Видимо \"этот\" не питается или давно не выходил за продуктами. "
            "Добыв улику возврашаетесь назад.", reply_markup=markup)
        return 5


async def dialog_6(update, context):
    text = update.message.text
    if text == '*Просканировать кресло*':
        reply_keyboard = [['*Реконструировать*', '*Вернуться назад*']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text('Просканировав кресло вы поняли, что можете реконструировать события.',
                                  reply_markup=markup)
        return 7
    elif text == '*Вернуться назад*':
        reply_keyboard = [['*Посмотреть на книгу*', '*Осмотреть кресло*', '*Осмотреть холодильник*']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            'В комнате есть несколько интересных объектов: на столе лежит книга, '
            'в углу стоит кресло, рядом с плитой стоит холодильник', reply_markup=markup)
        return 5


async def dialog_7(update, context):
    text = update.message.text
    if text == '*Реконструировать*':
        reply_keyboard = [["*Толкнуть Хэнка*", "*Достать из кобуры Хэнка пистолет*"],
                          ["*Бездействовать*", "*Броситься на девианта*"]]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Вы поняли, что подозреваемый находится на чердаке. "
            "\"Хэнк\", - прокричали вы! Он на чердаке. "
            "В этот момент на кресло приземлился девиант. "
            "Хэнк забежал в комнату. "
            "У девианта в руках пистолет", reply_markup=markup)
        return 8
    elif text == '*Вернуться назад*':
        reply_keyboard = [['*Посмотреть на книгу*', '*Осмотреть кресло*', '*Осмотреть холодильник*']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            'В комнате есть несколько интересных объектов: на столе лежит книга, '
            'в углу стоит кресло, рядом с плитой стоит холодильник', reply_markup=markup)
        return 5


async def dialog_8(update, context):
    text = update.message.text
    if text == '*Толкнуть Хэнка*':
        await update.message.reply_text(
            'Вы толкаете Хэнка и в вас прилетает пуля, но Хэнк окзаывается в коридоре. '
            'Два метких выстрела со стороны Хэнка и девиант повержен. '
            'Он подбегает к вам и спрашивает: \n\"Хэй! Ты как? В порядке? Идти можешь?\". '
            'Но только открыв рот вы понимаете, что важный биокомпонент повреждён. '
            'Вы отключаетесь... . Ваш индикатор погас. '
            'Хэнк вызвал подмогу. Район оцепили. Хэнк вернулся в офис. '
            'На подходе к своему рабочему месту он видит вас. Живым не вредимым...')
    elif text == '*Достать из кобуры Хэнка пистолет*':
        await update.message.reply_text(
            'Вы быстрым и ловким движением достаёте пистолет и делаете два метких выстрела. '
            'Девиант упал. Его индикатор погас.\nХэнк - Спасибо!\nКонор - Вы вовремя подоспели. '
            'Меня бы тут уже не было, если бы не вы.\nВы вызвали подмогу. '
            'Вас отправили в офис для заполнения бумаг. После работы хэнк предложил вам сходить с ним в бар. '
            'Отметить вашу победу!')
    elif text == '*Бездействовать*':
        await update.message.reply_text(
            'Хэнк быстро достал пистолет и успел сделать выстрел. '
            'Попал чётко в девианта. У девианта погас индикатор. '
            'Неожиданно вы слышите падение. Хэнк валялся на полу. '
            'У него из груди идёт кровь.\nКонор - Хэнк! Я сейчас вызову подмогу! '
            'Я...\nХэнк - Поздно! Мне уже не помочь. Прощай...\nВы медленно встаёте. '
            'Вы сделали вызов. Приехала полиция и скорая. Вы видете чёрный мешок, который выносят из дома. '
            'Вы чувствуете странное чувство. Вас отправляют в офис. '
            'Вам приходится до ночи писать отчёты в одиночку. '
            'Весь день вас не отпускает мысль, что вы стали девиантом. '
            'Вы решате проверить это и разобраться в девиантах. Вы направляетесь к Камски...')
    elif text == '*Броситься на девианта*':
        await update.message.reply_text(
            "Вы быстро направлятесь в девианта. "
            "Он успевает сделать выстрел в Хэнка. "
            "Вы вступаете в драку. Вы одерживаете в неё победу. "
            "Вы оборачиваетесь на ХэнкаХэнк валялся на полу. "
            'У него из груди идёт кровь.\nКонор - Хэнк! Я сейчас вызову подмогу! '
            'Я...\nХэнк - Поздно! Мне уже не помочь. Прощай...\nВы медленно встаёте. '
            'Вы сделали вызов. Приехала полиция и скорая. Вы видете чёрный мешок, который выносят из дома. '
            'Вы чувствуете странное чувство. Вас отправляют в офис. '
            'Вам приходится до ночи писать отчёты в одиночку. '
            'Весь день вас не отпускает мысль, что вы стали девиантом. '
            "Вы решате проверить это и разобраться в девиантах. Вы направляетесь к Камски...")


async def stop(update, context):
    await update.message.reply_text("Ещё увидимся)")
    return ConversationHandler.END


def main():
    TOKEN = '5628424797:AAGdXSWR4FLlbF287IbfFdFVxYl1Q9gYmTM'
    app = ApplicationBuilder().token("TOKEN").build()

    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_1)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_2)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_3)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_4)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_5)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_6)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_7)],
            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_8)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()