import telebot
import random
from DBInterface import generate_tasks
from simplite import Pylite
from secret import API_KEY
from threading import Thread

token = API_KEY
bot = telebot.TeleBot(token)
users = {}
# Greeting message
@bot.message_handler(commands=["start"])
def greet(message):
    bot.send_message(message.chat.id, "Привет! Я фигня.")

# Continiously updating for new incoming messages
def update_messages():
    bot.polling(none_stop=True)

# Text messages processing
@bot.message_handler(content_types=["text"])
def answer(message):
    DB = Pylite("userDB.db")
    id = message.chat.id
    if users.get(id) is None:
        print("NEW!")
        tasks = generate_tasks(id, DB)
        users[id] = [tasks, 0]
    if users[id][1] < 5:
        task = random.choice(users[id][0])
        users[id][0].remove(task)
        users[id][1] += 1
        # TODO: make correct DP answer or some in that shit
        # bot.send_message(id, "Вот Вам штука: {}".format(task[0][1]))
        # bot.send_message(id, "Вот Вам штука: {}".format(task[0][2]))
        # bot.send_message(id, "Вот Вам штука: {}".format(task[0][3]))
        # bot.send_message(id, "Вот Вам штука: {}".format(task[0][0]))
    else:
        users[id] = None
    DB.close_connection()

polling = Thread(target=update_messages)
polling.start()