# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

updater = Updater(token = '1706319949:AAH1LW5TWSImNumuNSOCf8IUFpibhx5FXcI')
dispatcher = updater.dispatcher

all_tasks = [
    2,
    {
        'variant': 1,
        'number': 0,
        1: 'Павел Иванович купил американский автомобиль, на спидометре которого скорость измеряется в милях в час. Американская миля равна 1609 м. Какова скорость автомобиля в километрах в час, если спидометр показывает 50 миль в час? Ответ округлите до целого числа.',
        2: 'На рисунке точками показана месячная аудитория поискового сайта Ya.ru во все месяцы с декабря 2008 года по октябрь 2009 года. По горизонтали указываются месяцы, по вертикали — количество человек, посетивших сайт хотя бы раз за данный месяц. Для наглядности точки на рисунке соединены линией. Определите по рисунку наименьшую месячную аудиторию сайта Ya.ru в период с декабря 2008 года по апрель 2009 года. https://math-ege.sdamgia.ru/get_file?id=39969&png=1',
        3: 'На клетчатой бумаге с размером клетки  дробь, числитель — 1, знаменатель — корень из { Пи }см \times дробь, числитель — 1, знаменатель — корень из { Пи }см изображён круг. Найдите площадь закрашенного сектора. Ответ дайте в квадратных сантиметрах. https://math-ege.sdamgia.ru/get_file?id=66323&png=1',
        4: 'Вероятность того, что новый электрический чайник прослужит больше года, равна 0,97. Вероятность того, что он прослужит больше двух лет, равна 0,89. Найдите вероятность того, что он прослужит меньше двух лет, но больше года.',
        5: 'Решите уравнение https://ege.sdamgia.ru/formula/30/30ab0de144ee27a54c056fd09ac67208p.png',
        6: 'Боковые стороны равнобедренного треугольника равны 5, основание равно 6. Найдите радиус вписанной окружности. https://math-ege.sdamgia.ru/get_file?id=66673&png=1',
        7: 'На рисунке изображен график производной функции f(x), определенной на интервале (−4; 8). Найдите точку экстремума функции f(x) на отрезке [−2; 6].https://math-ege.sdamgia.ru/get_file?id=65531',
        8: 'Найдите угол CAD₂ многогранника, изображенного на рисунке. Все двугранные углы многогранника прямые. Ответ дайте в градусах.https://math-ege.sdamgia.ru/get_file?id=29862',
        9: 'Найдите значение выражения https://ege.sdamgia.ru/formula/svg/c8/c88bffe34e5bc267ed0361e52dc397f9.svg',
        10: 'Плоский замкнутый контур площадью S = 0,5 м² находится в магнитном поле, индукция которого равномерно возрастает.'
            ' При этом согласно закону электромагнитной индукции Фарадея в контуре появляется ЭДС индукции, значение которой, выраженное в вольтах, определяется формулой εᵢ = aScosα, где α – острый угол между направлением магнитного поля и перпендикуляром к контуру, a=4 • 10⁻⁴ Тл/с – постоянная,'
            ' S – площадь замкнутого контура, находящегося в магнитном поле (в м²). При каком минимальном угле α  (в градусах) ЭДС индукции не будет превышать 10⁻⁴  В?',
        11: 'Смешали 4 литра 15–процентного водного раствора некоторого вещества с 6 литрами 25–процентного водного раствора этого же вещества. Сколько процентов составляет концентрация получившегося раствора?',
        12: 'Найдите наименьшее значение функции y=(x + 3)²(x + 5) − 1 на отрезке  [−4; −1].',
    },
    {
        'variant': 2,
        'number': 0,
        1: 'Футболка стоила 800 рублей. Затем цена была снижена на 15%. Сколько рублей сдачи с 1000 рублей должен получить покупатель при покупке этой футболки после снижения цены?',
        2: 'На диаграмме показан средний балл участников 10 стран в тестировании учащихся 4-го класса, по математике в 2007 году (по 1000-балльной шкале). По данным диаграммы найдите число стран, в которых средний балл ниже, чем в Нидерландах.https://math-ege.sdamgia.ru/get_file?id=37601',
        3: 'Найдите площадь четырехугольника, изображенного на клетчатой бумаге с размером клетки 1 см \times 1 см (см. рис.). Ответ дайте в квадратных сантиметрах.https://math-ege.sdamgia.ru/get_file?id=66087',
        4: 'На конференцию приехали 3 ученых из Норвегии, 3 из России и 4 из Испании. Каждый из них делает на конференции один доклад. Порядок докладов определяется жеребьёвкой. Найдите вероятность того, что восьмым окажется доклад ученого из России.',
        5: 'Найдите корень уравнения: https://ege.sdamgia.ru/formula/svg/60/6033a33e3eac7c223e265c94e20d0617.svg',
        6: 'В тупоугольном треугольнике ABC AC = BC = √17, AH – высота, CH = 4. Найдите tg(ACB).',
        7: 'На рисунке изображен график производной функции f(x), определенной на интервале (−4; 8). Найдите точку экстремума функции f(x) на отрезке [−2; 6].https://math-ege.sdamgia.ru/get_file?id=65531',
        8: 'Найдите угол CAD₂ многогранника, изображенного на рисунке. Все двугранные углы многогранника прямые. Ответ дайте в градусах.https://math-ege.sdamgia.ru/get_file?id=29862',
        9: 'Найдите значение выражения https://ege.sdamgia.ru/formula/svg/c8/c88bffe34e5bc267ed0361e52dc397f9.svg',
        10: 'Плоский замкнутый контур площадью S = 0,5 м² находится в магнитном поле, индукция которого равномерно возрастает.'
            ' При этом согласно закону электромагнитной индукции Фарадея в контуре появляется ЭДС индукции, значение которой, выраженное в вольтах, определяется формулой εᵢ = aScosα, где α – острый угол между направлением магнитного поля и перпендикуляром к контуру, a=4 • 10⁻⁴ Тл/с – постоянная,'
            ' S – площадь замкнутого контура, находящегося в магнитном поле (в м²). При каком минимальном угле α  (в градусах) ЭДС индукции не будет превышать 10⁻⁴  В?',
        11: 'Смешали 4 литра 15–процентного водного раствора некоторого вещества с 6 литрами 25–процентного водного раствора этого же вещества. Сколько процентов составляет концентрация получившегося раствора?',
        12: 'Найдите наименьшее значение функции y=(x + 3)²(x + 5) − 1 на отрезке  [−4; −1].',
    },
]

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

MODE, CHOOSING_TASK, SHOWING_TASK = range(3)

mode_keyboard = [['Решение задания', 'Решение варианта']]
variant_keyboard = [['1', '2']]
task_keyboard = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12'],
]

variant_number, task_number = 'Баболя', 'Бубуля'


def start(update: Update, _: CallbackContext) -> int:
    markup = ReplyKeyboardMarkup(mode_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Привет! Я бот для подготовки к ЕГЭ по профильной математике. Здесь можно просматривать задания из разных вариантов и тренироваться их выполнять. Напиши /cancel, чтобы остановить бота',
        reply_markup=markup
    )

    return MODE

def task_1(update: Update, _: CallbackContext) -> int:
    markup = ReplyKeyboardMarkup(variant_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Выбери вариант',
        reply_markup=markup,
    )

    return CHOOSING_TASK

def task_2(update: Update, _: CallbackContext):
    global variant_number
    variant_number = update.message.text
    markup = ReplyKeyboardMarkup(task_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Выбери задание',
        reply_markup=markup,
    )

    return SHOWING_TASK

def task_show(update: Update, _: CallbackContext):
    task_number = update.message.text
    print(all_tasks[int(variant_number)][int(task_number)])
    update.message.reply_text(
        all_tasks[int(variant_number)][int(task_number)],
        reply_markup=ReplyKeyboardRemove(),
    )


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ничего не понятно, выйди и зайди нормально')

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)


def main() -> None:

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states={

            MODE: [
                MessageHandler(Filters.regex('^Решение задания$'), task_1),
                MessageHandler(Filters.regex('^Решение варианта$'), task_1),
            ],

            CHOOSING_TASK: [
                MessageHandler(Filters.all, task_2)
            ],

            SHOWING_TASK: [
                MessageHandler(Filters.all, task_show)
            ]

        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), unknown)],
        allow_reentry=True
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
