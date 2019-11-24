#pip install chatterbot
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot=ChatBot('test')
bot.set_trainer(ListTrainer)
conv=open('chats.txt','r').readlines()
bot.train(conv)
while True:
    request=input("You: ")
    response=bot.get_response(request)
    print("Bot: ",response)
             
