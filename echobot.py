import random
import telebot

token = 'token'

bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных комманд
/add - добавить задачу в список (шаблон - дата, через пробел Задача)
/show - вывести все добавленные задачи
/show + date (/show 31.12.2025 или /show сегодня) вывести задачи на дату
/random - добавить случайную задачу на дату Сегодня"""

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

commands_todo = ["/help", "/add", "/random", ["/show"]]

tasks = {}

def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем задачу в список
        tasks[date].append(task)
    else:
        # Даты нет в словаре
        # Создаем запись с ключем date
        tasks[date] = [task]

@bot.message_handler(commands=["help"])
def help(massage):
    bot.send_message(massage.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(massage):
    command = massage.text.split(maxsplit=2)
    date = command[1].lower() # lower - в нижнем регистре
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(massage.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(massage):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(massage.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(massage): # massage.text = /show date
    command = massage.text.split(maxsplit=1)
    text = ""
    result_text =""
    if len(command) == 1:
        for key, value in sorted(tasks.items()):
            date = key
            text = date + "\n"
            for task in tasks[date]:
                result_text += text + "[] " + task + "\n"
            text = result_text
        #text = '\n'.join(f"{k}:{v}" for k,v in sorted(tasks.items()))
    else:
        date = command[1].lower()
        if date in tasks:
            text = date + "\n"  # Перевод в верхний регистр
            for task in tasks[date]:
                text = text + "[] " + task + "\n"
        else:
            text = 'Задач на указанную дату нет'
    bot.send_message(massage.chat.id, text)

@bot.message_handler(content_types=["text"])
def echo(massage):
    if massage.text in commands_todo:
        return
    else:
        text = 'Я не знаю эту комманду - попробуй /help'
    bot.send_message(massage.chat.id, text)

bot.polling(none_stop=True)