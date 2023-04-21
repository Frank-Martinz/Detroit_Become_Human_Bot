from telegram.ext import Application, MessageHandler, filters, ConversationHandler
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import ReplyKeyboardMarkup
import asyncio
from __db__ import *


async def start(update, context):
    await update.message.reply_photo(photo='img/1_1.jpg')
    reply_keyboard = [['Начать']]
    user_id, name = update.message.chat.id, update.message.chat.first_name
    add_new(user_id, name, 30, 0, 0, 'false', 'false', 'false', 'false')
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('Завод CyberLife...')
    await asyncio.sleep(1)
    await update.message.reply_text('- Добро пожаловать в Detroit, Коннор!')
    await asyncio.sleep(1)
    await update.message.reply_text('- Твои задачи выследить девиантов и ликвидировать их.')
    await asyncio.sleep(1)
    await update.message.reply_text('- Моё имя Коннор, приступаю к выполнению задач.', reply_markup=markup)
    await asyncio.sleep(1)
    return 1


async def dialog_1(update, context):
    await update.message.reply_photo(photo='img/1_2.jpg')
    reply_keyboard = [['Спасти рыбку'], ['Оставить рыбку умирать']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Вам поступило задание в один из многоэтажных домов."
        " Андроид семьи внезапно начал вести себя агрессивно,"
        " застрелил отца семьи, взял в заложницы маленькую девочку и грозит спрыгнуть с ней с крышы."
        " Вам преходилось сталкиваться с подобным, поэтому вы ехали на задание довольно уверенно."
        " Через некоторое время вы прибыли на место и прошли в квартиру.")
    await asyncio.sleep(8)
    await update.message.reply_text(
        "На полу вы увидели рыбку, выпрыгнувшую из аквариума. Если вы её не спасёте, то вскоре она погибнет.",
        reply_markup=markup)
    await asyncio.sleep(0.8)
    return 2


async def dialog_2(update, context):
    container = get_user(update.message.chat.id)[0]
    reply_keyboard = [['Осматривать квартиру'], ['Осмотреть планшет'], ['Найти пистолет'],
                      ['Выйти на крышу'], ['Осмотреть полицейского']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Спасти рыбку" or update.message.text == "Оставить рыбку умирать":
        await update.message.reply_text(
            "Пройдя дальше в комнату, вы увидели множество поллицейских с оружием и человека,"
            " по виду которого можно было понять, что он является капитаном."
            " Вы подошли к нему и попробовали заговорить, но похоже он не был настроен на разговор с вами."
            " осмотревшись в увидели открытый проход на крышу,"
            " где по всей видимости и находились заложница с девиантом.", reply_markup=markup)
        await asyncio.sleep(0.8)
    else:
        text = update.message.text
        if text == "Осматривать квартиру":
            if container[5] == 0:
                value = container[2] + 15
                change(container[0], container[1], value, 0, 0, 'true', container[6], container[7], container[8])
            await update.message.reply_text(
                "Осмотревшись получше, вы увидели мёртвое тело мужчины. Оно принадлежало отцу девочки."
                " Вы подошли ближе. Благодаря своим способностям вы выяснили,"
                " что мужчина был застрелен из пистолета и во время нападения держал что-то в руках."
                " И правда, недалеко вы увидели планшен."
                " На нём был открыт сайт по оформлению заказа на андроида."
                " Видимо девианта собирализь заменить в скором времени.", reply_markup=markup)
            await asyncio.sleep(0.8)

        elif text == "Осмотреть планшет":
            if container[6] == 0:
                value = container[2] + 15
                change(container[0], container[1], value, 0, 0, container[5], 'true', container[7], container[8])
            await update.message.reply_text("Вы направились в комнату заложницы. На кровати ребёнка лежит планшет."
                                            "На устройстве вы обнаружили видео,"
                                            " где девочка рвдостно и воодушевлённо рассказывает"
                                            " о своём новом друге андроиде по имени Даниель.", reply_markup=markup)
            await asyncio.sleep(0.8)
        elif text == "Найти пистолет":
            reply_keyboard = [['Взять пистолет'], ['Не брать пистолет']]
            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            if container[7] == 0:
                value = container[2] + 15
                change(container[0], container[1], value, 0, 0, container[5], container[6], 'true', container[8])
            await update.message.reply_text(
                "Недалеко от окна вы обнаружили ещё одно тело, но оно уже принадлежало полицейскому."
                " Осмотрев его, вы поняли, что он был застрелен девинатом во время перестрелки."
                " Рядом с трупом лежит пистолет.", reply_markup=markup)
            await asyncio.sleep(0.8)
        elif text == "Взять пистолет":
            if container[8] == 0:
                value = container[2] + 15
                change(container[0], container[1], value, 0, 0, container[5], container[6], container[7], 'true')
            reply_keyboard = [['Осматривать квартиру'], ['Осмотреть планшет'], ['Найти пистолет'],
                              ['Выйти на крышу'], ['Осмотреть полицейского']]
            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text("Вы взяли пистолет", reply_markup=markup)
        elif text == "Не брать пистолет":
            reply_keyboard = [['Осматривать квартиру'], ['Осмотреть планшет'], ['Найти пистолет'],
                              ['Выйти на крышу'], ['Осмотреть полицейского']]
            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text("Вы не взяли пистолет", reply_markup=markup)
        elif text == "Выйти на крышу":
            reply_keyboard = [['Пройти к девианту']]
            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text(
                "Решив, что уже достаточно осмотрели место преступления,"
                " вы вышли через проход на крышу."
                " На самом краю стоял девиант с пистолетом и держал заложницу.", reply_markup=markup)
            await asyncio.sleep(0.8)
            return 3
        elif text == "Осмотреть полицейского":
            await update.message.reply_text(
                "Недалеко от окна вы обнаружили тело полицейского. Он был застрелен девиантом", reply_markup=markup)


async def dialog_3(update, content):
    container = get_user(update.message.chat.id)[0]
    if update.message.text == "Пройти к девианту":
        await update.message.reply_photo(photo='img/1_3.jpg')
        if container[2] <= 45:
            reply_keyboard = [['Начать следующую миссию']]
            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text(
                "Вы попытались начать переговоры с девиантом, но он был настроил агрессивно и выстрелил в вас.")
            await asyncio.sleep(1)
            await update.message.reply_text(
                "Задание провалено", reply_markup=markup)
            return 4
        elif container[2] <= 60:
            if container[-1] == 1:
                reply_keyboard = [['Достать пистолет'], ['Сбросить с крыши андроида']]
                markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            else:
                reply_keyboard = [['Попытаться успокоить'], ['Сбросить с крыши андроида']]
                markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text(
                "Вы попытались начать переговоры с девиантом. Видно было, что он очень напряжён и настроен агрессивно,"
                " однако продолжал слушать вас. По мере того,"
                " как вы говорили, вы старались подходить в девианту. В какой то момент он понял,"
                " что вы замышляете и направил пистолет на вас.")
            await asyncio.sleep(3)
            await update.message.reply_text(" - Хватит! Уходи, иначе выстрелю!", reply_markup=markup)
        else:
            reply_keyboard = [['Начать следующую миссию']]

            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
            await update.message.reply_text("Вы вступили в переговоры с андроидом,"
                                            " при этом стараясь медленно подходить."
                                            " С каждым вашим словом девиант успакаивался и постепенно переходил"
                                            " в нормальное состояние. В итоге вам удалось уговорить"
                                            " его отпустить заложницу, но быстро подоспешие полицейские"
                                            " всё же застрелили и андроида, несмотря на ваши уговоры,"
                                            " что этого делать не стоит.")
            await update.message.reply_photo(photo='img/1_7.jpg')
            await asyncio.sleep(1.4)
            await update.message.reply_text("Задание выполнено", reply_markup=markup)
            await asyncio.sleep(0.8)
            return 4
    elif update.message.text == "Сбросить с крыши андроида":
        await update.message.reply_photo(photo='img/1_6.jpg')
        reply_keyboard = [['Начать следующую миссию']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text("Вы бросились на андроида, оттолкнули девочку,"
                                        " и упали с крыши вместе с девиантом.")
        await asyncio.sleep(1)
        await update.message.reply_text("Задание выполнено", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 4
    elif update.message.text == "Достать пистолет":
        await update.message.reply_photo(photo='img/1_4.jpg')
        reply_keyboard = [['Начать следующую миссию']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text("Вы быстро достали пистолет и выстрелили. Андроид упал мертвый."
                                        " Быстро подоспели полицейские и отвели девочку в сторону."
                                        " Вы смогли спасти её.", reply_markup=markup)
        await asyncio.sleep(1)
        await update.message.reply_text("Задание выполнено", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 4
    elif update.message.text == "Попытаться успокоить":
        await update.message.reply_photo(photo='img/1_5.jpg')
        reply_keyboard = [['Начать следующую миссию']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text("Вы постарались успокоить андроида, но он был непреклонен и выстрелил в вас.")
        await asyncio.sleep(1)
        await update.message.reply_text("Задание провалено", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 4


async def dialog_4(update, content):
    reply_keyboard = [['Открыть дверь и войти']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Начать следующую миссию":
        await update.message.reply_text("Вам поступило новое задание! Вы должны найти Хэнка.")
        await asyncio.sleep(1)
        await update.message.reply_text(
            "Вы пришли к бару Джимми Питерсона. На вывеске указано, что андроидам здесь не рады.", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 5


async def dialog_5(update, content):
    reply_keyboard = [['Просканировать лица'], ['Спросить где Хэнк']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Осталось только розыскать Хэнка.", reply_markup=markup)
    return 6


async def dialog_6(update, content):
    reply_keyboard = [['Убедить'], ['Пригрозить'], ['Выразить понимание']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Просканировать лица":
        await update.message.reply_photo(photo='img/1_8.jpg')
        await update.message.reply_text("Вы нашли лейтенанта Хэнка, он сидит за барной стойкой")
        await asyncio.sleep(1)
        await update.message.reply_text(
            "- Здраствуйте Хэнк, моё имя Коннор, я андроид, присланный с CyberLife. Меня прислали к вам на помощь.",
            reply_markup=markup)
        await asyncio.sleep(1)
        return 7
    elif update.message.text == "Спросить где Хэнк":
        await update.message.reply_text("Вы наткнулись не на того человека.")
        await asyncio.sleep(0.8)
        await update.message.reply_text("- Пойди прочь машина - сказал он.")
        await asyncio.sleep(0.8)
        await update.message.reply_text("Вы решаете просканировать лица")
        await asyncio.sleep(1)
        await update.message.reply_text("Вы нашли лейтенанта Хэнка, он сидит за барной стойкой")
        await update.message.reply_photo(photo='img/1_8.jpg')
        await update.message.reply_text(
            "- Здраствуйте Хэнк, моё имя Коннор, я андроид, присланный с CyberLife. Меня прислали к вам на помощь.",
            reply_markup=markup)
        await asyncio.sleep(0.8)
        return 7


async def dialog_7(update, content):
    reply_keyboard = [['Войти в дом']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Убедить":
        await update.message.reply_text("- Хэнк, для более лучшей работы нам следует подружиться. Я много знаю о вас.")
        await asyncio.sleep(1.2)
        await update.message.reply_text("- Давайте я оплачу за вас счёт.")
        await asyncio.sleep(1)
        await update.message.reply_text("- Ладно, машина, поехали на задание.")
        await asyncio.sleep(1)
        await update.message.reply_text("Вы приехали на место убийство. Вам нужно войти в дом.", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 8
    elif update.message.text == "Пригрозить":
        await update.message.reply_text("- Хэнк, нам нужно ехать на задание, работа сама себя не сделает!")
        await asyncio.sleep(1)
        await update.message.reply_text("- Вы пойдёте со мной.")
        await asyncio.sleep(1)
        await update.message.reply_text("Хэнк хватает андроида.")
        await asyncio.sleep(1)
        await update.message.reply_text(
            "- Только попробуй мне тут поуказывать, машина, кусок металла, имитирующий человека")
        await asyncio.sleep(1.3)
        await update.message.reply_text("Вы приехали на место убийство. Вам нужно войти в дом.", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 8
    elif update.message.text == "Выразить понимание":
        await update.message.reply_text(
            "- Понимаете Хэнк, нам лучше будет сотрудничать, для того, чтобы успешно выполнить задание.")
        await asyncio.sleep(1.3)
        await update.message.reply_text("- Ладно, так уж и быть, дай мне 5 минут ещё")
        await asyncio.sleep(1)
        await update.message.reply_text("Вы приехали на место убийство. Вам нужно войти в дом.", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 8


async def dialog_8(update, content):
    await update.message.reply_photo(photo='img/1_9.jpg')
    reply_keyboard = [['Начать сканирование']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Войти в дом":
        await update.message.reply_text("В доме стоит Хэнк и группа полицейских.")
        await asyncio.sleep(1)
        await update.message.reply_text("- Что здесь произошло?")
        await asyncio.sleep(0.5)
        await update.message.reply_text(
            "- Девиант, убил своего хозяина. Весь дом в его крови, просканируй всё, может что-нибудь найдешь.")
        await asyncio.sleep(2)
        await update.message.reply_text("- Хорошо", reply_markup=markup)
        await asyncio.sleep(0.5)
        return 9


async def dialog_9(update, content):
    reply_keyboard = [['Начать проектирование движений андроида']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Начать сканирование":
        await update.message.reply_text("Вы обнаружили тело мужчины, нож, стул, кровь.", reply_markup=markup)
        await asyncio.sleep(1)
        return 10


async def dialog_10(update, content):
    reply_keyboard = [['Осмотреть улицу']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Начать проектирование движений андроида":
        await update.message.reply_text(
            "- Хэнк, на андроида нападал хозяин, машина обороняясь"
            " взяла нож и начала убивать жертву, а позже скрылась.")
        await asyncio.sleep(2)
        await update.message.reply_text("- А это уже что-то новое, проводи дальше расследование.", reply_markup=markup)
        await asyncio.sleep(1)
    return 11


async def dialog_11(update, content):
    reply_keyboard = [["Начать осматривать дом"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Осмотреть улицу":
        await update.message.reply_text("На улице нет следов андроида, значит андроид в доме.", reply_markup=markup)
        await asyncio.sleep(1)
        return 12


async def dialog_12(update, content):
    reply_keyboard = [["Залезть"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Начать осматривать дом":
        await update.message.reply_text("Вы увидили лестницу, ведущую на чердак.", reply_markup=markup)
        await asyncio.sleep(1)
        return 13


async def dialog_13(update, content):
    reply_keyboard = [["Пройти дальше"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Залезть":
        await update.message.reply_text("На чердаке пронёсся звук хотьбы.")
        await asyncio.sleep(1)
        await update.message.reply_text("- Выходи, мы тебя не тронем")
        await asyncio.sleep(0.3)
        await update.message.reply_text("- ...")
        await asyncio.sleep(1)
        await update.message.reply_text("- Выходи, мы всего лишь проверим тебя, никто тебя не тронет.",
                                        reply_markup=markup)
        await asyncio.sleep(1)
    return 14


async def dialog_14(update, content):
    reply_keyboard = [["Сказать где находится девиант"], ['Уйти с чердака и сказать, что никого нет']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if update.message.text == "Пройти дальше":
        await update.message.reply_text("Андроид показался.")
        await asyncio.sleep(1)
        await update.message.reply_text("- Не подходи!")
        await asyncio.sleep(1)
        await update.message.reply_text("- Что ты здесь делаешь?")
        await asyncio.sleep(1)
        await update.message.reply_text(
            "- Он, он, он на-па-л на меня, унижал, начал бить и"
            " в какой-то момент, что-то внутри меня решило, я не должен подчиняться ему. Тогда"
            " я взял нож и нанёс ему ответный удар. Хватит терпеть унижений, они нас просто используют.")
        await asyncio.sleep(8)
        await update.message.reply_text(
            "- Ты девиант, у тебя программный сбой, ты не исправен, ты должен служить людям!")
        await asyncio.sleep(3)
        await update.message.reply_text("- Разве я заслужил такого отношения к себе?")
        await asyncio.sleep(1)
        await update.message.reply_text("Звуки хождения...")
        await asyncio.sleep(1)
        await update.message.reply_text("- Они идут, не говори им, что я тут.", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 15


async def dialog_15(update, content):
    if update.message.text == "Сказать где находится девиант":
        reply_keyboard = [["Догнать андроида"]]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text("Девиант побежал", reply_markup=markup)
    elif update.message.text == "Уйти с чердака и сказать, что никого нет":
        reply_keyboard = [['Начать следующую миссию']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "- Хэнк, я был на чердаке, там никого нет. Возможно девиант вылез через окно и убежал по крышам.")
        await asyncio.sleep(3)
        await update.message.reply_text("- Так и знал, что ты всего лишь ненужная машина, Коннор.", reply_markup=markup)
        await asyncio.sleep(2)
        return 16
    elif update.message.text == "Догнать андроида":
        reply_keyboard = [['Начать следующую миссию']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text("Вы догнали андроида и позвали Хэнка.")
        await asyncio.sleep(1)
        await update.message.reply_text("- Молодец Коннор! Так быть может мы и подружимся.")
        await asyncio.sleep(1)
        await update.message.reply_text("Задание выполнено успешно, девиант пойман", reply_markup=markup)
        await asyncio.sleep(0.8)
        return 16


async def dialog_16(update, content):
    await update.message.reply_photo(photo='img/2_0.jpg')
    if update.message.text == "Начать следующую миссию":
        reply_keyboard = [['Высказать свои опасения'], ['Ничего не говорить']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            'Вы приехали к старому дому. Задумались: \"Как здесь может кто-то жить ,а уж тем более шуметь?\"',
            reply_markup=markup)
        await asyncio.sleep(1)
        return 17


async def dialog_17(update, content):
    text = update.message.text
    if text == 'Высказать свои опасения':
        await update.message.reply_text('Конор - Хэнк, вы уверены, что сюда безопасно заходить?')
        await asyncio.sleep(1)
        await update.message.reply_text('Хэнк - Да чего ты боишься? Ты наполовину железный. Тебя не убьёт')
        await asyncio.sleep(1.5)
    reply_keyboard = [['Промолчать'], ['Ответить']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        'Вы заходите в дом. Поднимаетесь на последний этаж. Как только вы поднялись, вы слышите грохот')
    await asyncio.sleep(1)
    await update.message.reply_text('Хэнк - Ты слышал?', reply_markup=markup)
    await asyncio.sleep(1)
    return 18


async def dialog_18(update, content):
    text = update.message.text
    if text == 'Промолчать':
        await update.message.reply_text("Хэнк - Вечно вы такие молчаливые, когда надо? Шум был оттуда!")
        await asyncio.sleep(1)
    elif text == 'Ответить':
        await update.message.reply_text("Конор - Да. Это было в той стороне!")
        await asyncio.sleep(1)
        await update.message.reply_text("Хэнк - Без сопливых разберусь. Идём!")
        await asyncio.sleep(1)
    reply_keyboard = [['Пойти вперед', 'Пойти налево', 'Пойти направо']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Вы подходите к закрытой двери. Хэнк выбивает её. Вы входите в квартиру.\nПеред вами 3 двери",
        reply_markup=markup)
    await asyncio.sleep(1)
    return 19


async def dialog_19(update, content):
    text = update.message.text
    if text == 'Пойти вперед':
        await update.message.reply_text('Конор - Я пойду осмотрюсь там!')
        await asyncio.sleep(1)
        await update.message.reply_text('Хэнк - Хорошо. Иди туда')
        await asyncio.sleep(1)
    elif text in ['Пойти налево', 'Пойти направо']:
        await update.message.reply_text('Конор - Я пойду осмотрюсь там!')
        await asyncio.sleep(1)
        await update.message.reply_text(
            'Хэнк - Эй! Ты куда пошёл? Я там осмотрюсь. Лучше посмотри там! *Указывает направление*')
        await asyncio.sleep(1)
    reply_keyboard = [['Посмотреть на книгу'], ['Осмотреть кресло'], ['Осмотреть холодильник']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Вы заходите в комнату. В комнате стоит мебель. "
        "Обустроено так, как будто тут кто-то живёт. "
        "Вы решили осмотреться и заметили пару интересных объектов: "
        "на столе лежит книга, в углу стоит кресло, рядом с плитой стоит холодильник", reply_markup=markup)
    await asyncio.sleep(1)
    return 20


async def dialog_20(update, content):
    text = update.message.text
    if text == 'Посмотреть на книгу':
        reply_keyboard = [['Посмотреть на книгу'], ['Осмотреть кресло'], ['Осмотреть холодильник']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            'Вы подошли к книге. '
            'Она написана каким-то шифром. '
            'Чтобы его расшифровать понадобится много времени. '
            'Вы откладываете книгу и добыв улику возврашаетесь назад.', reply_markup=markup)
        await asyncio.sleep(1.5)
        return 20
    elif text == 'Осмотреть кресло':
        reply_keyboard = [['Просканировать кресло'], ['Вернуться назад']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text("Вы подходите к нему и видите грязные следы", reply_markup=markup)
        return 21
    elif text == 'Осмотреть холодильник':
        reply_keyboard = [['Посмотреть на книгу'], ['Осмотреть кресло'], ['Осмотреть холодильник']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Вы открываете холодильник. "
            "В нём нет продуктов. На плите тоже пусто. "
            "Видимо \"этот\" не питается или давно не выходил за продуктами. "
            "Добыв улику возврашаетесь назад.", reply_markup=markup)
        await asyncio.sleep(2.5)
        return 20


async def dialog_21(update, content):
    text = update.message.text
    if text == 'Просканировать кресло':
        await update.message.reply_text('*Сканирование*')
        await asyncio.sleep(3)
        reply_keyboard = [['Реконструировать'], ['Вернуться назад']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text('Просканировав кресло вы поняли, что можете реконструировать события.',
                                        reply_markup=markup)
        return 22
    elif text == 'Вернуться назад':
        reply_keyboard = [['Посмотреть на книгу'], ['Осмотреть кресло'], ['Осмотреть холодильник']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            'В комнате есть несколько интересных объектов: на столе лежит книга, '
            'в углу стоит кресло, рядом с плитой стоит холодильник', reply_markup=markup)
        await asyncio.sleep(1)
        return 20


async def dialog_22(update, content):
    text = update.message.text
    if text == 'Реконструировать':
        await update.message.reply_text('*Реконструкция*')
        await asyncio.sleep(4)
        reply_keyboard = [["Толкнуть Хэнка", "Достать из кобуры Хэнка пистолет"],
                          ["Бездействовать", "Броситься на девианта"]]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Вы поняли, что подозреваемый находится на чердаке. "
            "\"Хэнк\", - прокричали вы! Он на чердаке. "
            "В этот момент на кресло приземлился девиант. "
            "Хэнк забежал в комнату. "
            "У девианта в руках пистолет", reply_markup=markup)
        await asyncio.sleep(2)
        return 23
    elif text == 'Вернуться назад':
        reply_keyboard = [['Посмотреть на книгу'], ['Осмотреть кресло'], ['Осмотреть холодильник']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            'В комнате есть несколько интересных объектов: на столе лежит книга, '
            'в углу стоит кресло, рядом с плитой стоит холодильник', reply_markup=markup)
        await asyncio.sleep(1)
        return 20


async def dialog_23(update, content):
    text = update.message.text
    if text == 'Толкнуть Хэнка':
        await update.message.reply_photo(photo='img/2_1.jpg')
        await update.message.reply_text(
            'Вы толкаете Хэнка и в вас прилетает пуля, но Хэнк окзаывается в коридоре. '
            'Два метких выстрела со стороны Хэнка и девиант повержен. '
            'Он подбегает к вам и спрашивает: \n\"Хэй! Ты как? В порядке? Идти можешь?\". '
            'Но только открыв рот вы понимаете, что важный биокомпонент повреждён. '
            'Вы отключаетесь... . Ваш индикатор погас. '
            'Хэнк вызвал подмогу. Район оцепили. Хэнк вернулся в офис. '
            'На подходе к своему рабочему месту он видит вас. Живым не вредимым...')
        await asyncio.sleep(5)
    elif text == 'Достать из кобуры Хэнка пистолет':
        await update.message.reply_photo(photo='img/2_3.jpg')
        await update.message.reply_text(
            'Вы быстрым и ловким движением достаёте пистолет и делаете два метких выстрела. '
            'Девиант упал. Его индикатор погас.\nХэнк - Спасибо!\nКонор - Вы вовремя подоспели. '
            'Меня бы тут уже не было, если бы не вы.\nВы вызвали подмогу. '
            'Вас отправили в офис для заполнения бумаг. После работы хэнк предложил вам сходить с ним в бар. '
            'Отметить вашу победу!')
        await asyncio.sleep(5)
    elif text == 'Бездействовать':
        await update.message.reply_photo(photo='img/2_2.jpg')
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
        await asyncio.sleep(7)
    elif text == 'Броситься на девианта':
        await update.message.reply_photo(photo='img/2_4.jpg')
        await update.message.reply_text(
            "Вы быстро направлятесь в девианта. "
            "Он успевает сделать выстрел в Хэнка. "
            "Вы вступаете в драку. Вы одерживаете в ней победу. "
            "Вы оборачиваетесь на Хэнка. Хэнк валялся на полу. "
            'У него из груди идёт кровь.\nКонор - Хэнк! Я сейчас вызову подмогу! '
            'Я...\nХэнк - Поздно! Мне уже не помочь. Прощай...\nВы медленно встаёте. '
            'Вы сделали вызов. Приехала полиция и скорая. Вы видете чёрный мешок, который выносят из дома. '
            'Вы чувствуете странное чувство. Вас отправляют в офис. '
            'Вам приходится до ночи писать отчёты в одиночку. '
            'Весь день вас не отпускает мысль, что вы стали девиантом. '
            "Вы решате проверить это и разобраться в девиантах. Вы направляетесь к Камски...")
        await asyncio.sleep(7)
    await update.message.reply_text("На данный момент квест закончился."
                                    " В ближайщее время наша команды сделает продолжение."
                                    " Надеемся, что вы полностью погрузились в сюжет, и он вам понравился."
                                    "А пока, мы покажем вам фото города.")
    await update.message.reply_photo(photo="img/2_5.jpg")
    await asyncio.sleep(0.5)
    await update.message.reply_photo(photo="img/2_6.jpg")
    await asyncio.sleep(0.5)
    await update.message.reply_photo(photo="img/2_7.jpg")
    await asyncio.sleep(0.5)
    await update.message.reply_photo(photo="img/2_8.jpg")
    await asyncio.sleep(0.5)
    reply_keyboard = [['/restart']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Мы старались ради вас!", reply_markup=markup)
    return ConversationHandler.END


async def stop(update, context):
    await update.message.reply_text("Ещё увидимся)")
    return ConversationHandler.END


def main():
    TOKEN = '6236599929:AAHl3ikQ1rVfvvoMP2On1-SokbjuXEmwnC0'
    app = ApplicationBuilder().token("TOKEN").build()

    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      CommandHandler('restart', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_1)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_2)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_3)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_4)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_5)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_6)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_7)],
            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_8)],
            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_9)],
            10: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_10)],
            11: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_11)],
            12: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_12)],
            13: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_13)],
            14: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_14)],
            15: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_15)],
            16: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_16)],
            17: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_17)],
            18: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_18)],
            19: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_19)],
            20: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_20)],
            21: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_21)],
            22: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_22)],
            23: [MessageHandler(filters.TEXT & ~filters.COMMAND, dialog_23)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    create()
    main()
