import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 
import json

def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text 

page_bg_img = '''
<style>
body {
background-image: url("https://github.com/ultranet1/CHAT_BOT/blob/main/ch1.jpg");
background-size: cover;
}
</style>
'''

ai= 'https://github.com/ultranet1/CHAT_BOT/blob/main/ai.yml'




st.sidebar.markdown(f"<h1 style='text-align: center; color: blue;'> ULTRA BOT</h1>", unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center; color: white;'>ULTRA BOT</h1>", unsafe_allow_html=True)

st.subheader(""" 
 ULTRA BOT is an NLP conversational chatterbot aimed at helping business to answer FAQs from customers. Initialize the bot by clicking the "Start Chat" button. 
""")

ind = 1
if st.sidebar.button('Start Chatting'):
    trainer2=ListTrainer(bot) 
    trainer2.train(ai)
    st.title("Your bot is ready to talk to you")
    ind = ind +1
        
user_input = get_text()

st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)





bot = ChatBot('Ultra',
             logic_adapters = [
                 {
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I do not understand. I am still learning. Please contact github.io/ultranet1 for further assistance.',
                     'maximum_similarity_threshold': 0.90
                 }
             ],
             read_only = True,
             preprocessors=['chatterbot.preprocessors.clean_whitespace',
'chatterbot.preprocessors.unescape_html',
'chatterbot.preprocessors.convert_to_ascii'])





if True:
    st.text_area("BOT:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)


st.warning('Bot is still learning, it wiil be updated later on')
