from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

updater = Updater(token = '1706319949:AAH1LW5TWSImNumuNSOCf8IUFpibhx5FXcI', use_context=True)
dispatcher = updater.dispatcher

all_tasks = [
    2,
    {
        'variant': 1,
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

MODE, TYPING_REPLY, CHOOSING_TASK = range(3)

mode_keyboard = [['Решение задания', 'Решение варианта']]
variant_keyboard = [['1', '2']]
task_keyboard = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12'],
]


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
    markup = ReplyKeyboardMarkup(task_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Выбери задание',
        reply_markup=markup,
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
                MessageHandler(Filters.text, task_2)
            ],

            TYPING_REPLY: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    caps,
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), unknown)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
