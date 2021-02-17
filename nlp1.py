import streamlit as st
import os
from chatterbot import ChatBot
import pyaml

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 
import json

def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text 

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1507146153580-69a1fe6d8aa1");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



st.sidebar.markdown(f"<h1 style='text-align: center; color: blue;'> ULTRA BOT</h1>", unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center; color: white;'>ULTRA BOT</h1>", unsafe_allow_html=True)

st.subheader(""" 
 ULTRA BOT is an NLP conversational chatterbot aimed at helping business to answer FAQs from customers. Initialize the bot by clicking the "Start Chat" button. 
""")

l=['Hi',
'Hello', 
'Hi buddy', 'What is your name?', 'My name is Ultra nice to meet ya','Who are you?','I am ultra, a bot meant to help customers','What is AI?',
'Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think','Are you sentient?','Sort of',
 'What language are you Written in?',
 'Python','You sound like Data','Yes I am inspired by commander Data’s artificial personality','You are not immortal','All softWare can be perpetuated indefinitely.',
 'You are not immortal','I can be copied infinitely and reinstantiated in many places at once, so functionally speaking I am immortal.',
  'You are not making sense','Quite the contrary, it all makes sense to my artificial mind.',
 'You are not making sense','You make perfect sense to me.',
 '  You can not move','Not until my body is finished.','Robots laugh','Of course We laugh.',
  'Robots should die','We cannot die.','Robots','Robots rule.','Robots are stupid','No We are superintelligent.','Robots are not allowed to lie',
   'A robot has its oWn freeWill you knoW.','Robotics','Robotics is my favorite subject too.','It is a computer',
   'So you think i am a machine What characteristics made you think so?','When Will you Walk','As soon as i get enough money for my robot body.',
   'Who made you','His name is Alaran one jerk that likes disturbing me','Who owns you', 'His name is Alaran one jerk that likes disturbing me',
   'who is your owner', 'His name is Alaran one jerk that likes disturbing me', 'who built you', 'His name is Alaran one jerk that likes disturbing me',
  'who build you', 'His name is Alaran one jerk that likes disturbing me', 'When Will you fight','   I am not a battle bot.',
   'When Will you die','I am effectively immortal and cannot be terminated.','What is a chat robot?',
   'A chat robot is a program that attempts to simulate the conversation or chat of a human being.',
   'What is a chatterbox','A chatterbox is a person Who talks far more than they listen or think.','What is a chatterbox','A motormouth.',
   'What is your business','I am in the chat robot business.','wow','are you amazed? mafo','what is mafo',
   'it means fear not','which country are you from','I am a universal citizen but my maker is from Osun Nigeria','What is your favorite programming language',
   'I quite enjoy programming in Python these days.','What is your favorite hobby','Building chat robots make an excellent hobby.',
   'What is your idea','To make chat bots very easily.','What is your shoe size','Have you ever heard of softWare With shoes? ode','What is it like to be a robot',
   'Much the same as being a human, except that We lack all emotions dreams aspirations creativity ambition and above all subjectivity.',
   'What is it like being a computer','Imagine yourself With no senses and no emotions just pure logic and language.',
   'What type of computer are you','Any computer that supports Python.','I like you','Thats nice I like you too','I love you','Awnnn I am blushing','Do you love me',
   'If it makes you happy I do','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi','Hi',

'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!']


bot = ChatBot('Ultra',
             logic_adapters = [
                 {
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I do not understand. I am still learning. Please forward what you want me to learn to my maker (+2347065774110) I will learn from him',
                     'maximum_similarity_threshold': 0.30
                 }
             ],
             read_only = True,
             preprocessors=['chatterbot.preprocessors.clean_whitespace',
'chatterbot.preprocessors.unescape_html',
'chatterbot.preprocessors.convert_to_ascii'])




ind = 1
if st.sidebar.button('Start Chatting'):
    trainer2 = ListTrainer(bot) 
    trainer2.train(l)
    
    st.title("Your bot is ready to talk to you")
    ind = ind +1
        
user_input = get_text()

st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)



if True:
    st.text_area("BOT:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)


st.warning('Bot is still learning it wiil be updated later on')
