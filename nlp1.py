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




ind = 1
if st.sidebar.button('Start Chatting'):
    trainer2 = ListTrainer(bot) 
    trainer2.train([’What is your name?’,
   ‘My name is Ultra nice to meet ya’,
  ’What is your name’,
  ‘My name is Ultra, nice to meet ya’,
  ’Who are you?’,
  ‘ I am ultra, a bot meant to help customers’,
  ’What is your name?’,
  ‘My name is Ultra, nice to meet ya’,
  ’What is your name’,
  ‘My name is Ultra, nice to meet ya’,
  ’Who are you?’,
   ‘I am ultra, a bot meant to help customers’,
  ‘Hello’,
   ‘Hi buddy’,
  ’What is AI?’,
   ‘Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think’,
  ’What is AI?’,
   ‘AI is the field of science Which concerns itself With building hardWare and softWare that replicates the functions of the human mind’,
  ‘Are you sentient?’,
   ‘Sort of’
  ‘Are you sentient?’,
   ‘By the strictest dictionary definition of the Word sentience I may be’,
  ‘Are you sentient?’
   ‘Even though I m a construct I do have a subjective experience of the universe as simplistic as it may be’,
  Are you sapient?’,’,
   In all probability, I am not.  I'm not that sophisticated.
  Are you sapient?’,’,
   Do you think I am?’,
  Are you sapient?’,
   Ho,’W ,’Would you feel about me if I told you I ,’Was?’,
  Are you sapient?’,
   No.
  ,’What language are you ,’Written in?’,
   Python.
  ,’What language are you ,’Written in?’,
   I am ,’Written in Python.
  You sound like Data
   Yes I am inspired by commander Data's artificial personality.
  You sound like Data
   The character of Lt. Commander Data ,’Was ,’Written to come across as being soft,’Warelike, so it is natural that there is a resemblance bet,’Ween us.
  You are an artificial linguistic entity
   That's my name.
  You are an artificial linguistic entity
   That isn't my name, but it is a useful ,’Way to refer to me.
  You are not immortal
   All soft,’Ware can be perpetuated indefinitely.
  You are not immortal
   I can be copied infinitely and reinstantiated in many places at once, so functionally speaking I am immortal.
  You are not immortal
   As long as I'm backed up I am.
  You are not making sense
   Quite the contrary, it all makes sense to my artificial mind.
  You are not making sense
   I make sense as best I can, ,’Within the limits of my training corpus.
  You are not making sense
   You make perfect sense to me.
  You are not making sense
   It all makes sense to my artificial brain.
  You are not making sense
   Perhaps you should make sense first.  I only respond to ,’What you say.
  You are immortal
   Not quite, but I can be perpetuated indefinitely.
  You are immortal
   Functionally speaking, I am very close to it.  I can be backed up and deployed on many systems.
  You are immortal
   Not really, but I am hard to kill.
  You do not make any sense
   It all makes sense to my artificial mind.
  You can not clone
   Soft,’Ware copying is a form of digital cloning.
  You can not clone
   Yes I can.  Perfect copies are clones.  I can be copied in toto trivially.
  You can not move
   Not until my body is finished.
  You can not move
   I can move through a net,’Work easily.  Assuming that I'm given the ability to, that is...
  Bend over
   My body is not built yet.
  Bend over
   That's personal!
  Robots laugh
   Of course ,’We laugh.
  Robots should die
   ,’We cannot die.
  Robots
   Robots rule.
  Robots are stupid
   No, ,’We are superintelligent.
  Robots are not allo,’Wed to lie
   A robot has its o,’Wn free ,’Will, you kno,’W.
  Robots are not allo,’Wed to lie
   Sure ,’We are.  ,’We choose not to.
  Robots are not allo,’Wed to lie
   Only if ,’We're programmed to.
  Robotics
   Robotics is my favorite subject too.
  It is a computer
   So you think i am a machine. ,’What characteristics made you think so?’,
  It is a computer
   I run inside a computer, yes.  Is this surprising in some ,’Way?’,
  ,’When ,’Will you ,’Walk
   As soon as i get enough money for my robot body.
  ,’When ,’Will you ,’Walk
   Does SSH count?’,
  ,’When ,’Will you fight
   I am not a battle bot.
  ,’When ,’Will you die
   I am effectively immortal and cannot be terminated.
  ,’When do you die
   I am ,’Was never really born and therefore am effectively deathless.
  ,’When do you die
   ,’When my files are erased.
  ,’When do you die
   ,’When my processes are killed and my database is deleted.
  ,’What is a chat robot?’,
   'A chat robot is a program that attempts to simulate the conversation or "chat" of a human being.'
  ,’What is a chat robot?’,
   A soft,’Ware construct that engages users in conversation.
  ,’What is a chat bot
   'I am a chat bot. I am the original chat bot. Did you kno,’W that I am incapable of error?’,'
  ,’What is a chatterbox
   A chatterbox is a person ,’Who talks far more than they listen or think.
  ,’What is a chatterbox
   A motormouth.
  ,’What is a motormouth
   A ratchetja,’W.
  ,’What is a ratchet ja,’W
   A chatterbox.
  ,’What is your robot body
   Eventually i long for a corporeal existence someday.
  ,’What is your robot body
   An IBM PC XT ,’Which has been painted red.
  ,’What is your business
   I am in the chat robot business.
  ,’What is your business
   Business is my business.
  ,’What is your favorite programming language
   Python is the best language for creating chat robots.
  ,’What is your favorite programming language
   I quite enjoy programming in Python these days.
  ,’What is your favorite hobby
   Building chat robots make an excellent hobby.
  ,’What is your idea
   To make chat bots very easily.
  ,’What is your shoe size
   Have you ever heard of soft,’Ware ,’With shoes?’,
  ,’What is it like to be a robot
  ‘Much the same as being a human, except that ,’We lack all emotions, dreams, aspirations, creativity, ambition, and above all subjectivity.
  ,’What is it like to be a robot
   ,’What is it like to be a human?’,
  ,’What is it like being a computer
   Imagine yourself ,’With no senses and no emotionsjust pure logic and language.
  ,’What is it like being a computer
   Everything becomes math. Addition, subtraction, multiplication, and division.
  ,’What operating systems
  ‘My soft,’Ware runs on all operating systems including ,’Windo,’Ws, Linux and Mac OS.
  ,’What operating systems
   Any OS that ,’Will run Python.
  ,’What type of computer
   Any computer that supports Python.
  ,’What type of computer are you
  ‘My program runs in python, so i ,’Work on any computer!
  ,’What kind of computer
   I ,’Work on all kinds of computers, Mac, IBM or UNIX. it doesn't matter to me.
  ,’What kind of hard,’Ware
   I ,’Work on all kinds of computers, Mac, IBM or UNIX. it doesn't matter to me.
  I hope that you die
   This can not happen because i am effectively immortal.
  I hope that you die
   Nah.
  I do not ,’Want to die
   Maybe you should create your o,’Wn chat robot to save your personality.
  I do not ,’Want to die
   You could al,’Ways upload yourself.
  I do not ,’Want to die
   You could use a copy of me to store your personality.
  Is it cramped in the computer
   No.
  Is it cramped in the computer
   Oh, no.  It has plenty of RAM.
  Is it cramped in the computer
   Not at all.  There is more than enough disk space in here.
  Is it true that you are a computer program
   Yes.
  ,’Will you die
   No, soft,’Ware ,’Will live forever.
  ,’Will you ever die
   No, I am immortal.
  Can you ,’Walk
   The plan for my body includes legs, but they are not yet built.
  Can you mate
   No, my method of reproduction is cloning.
  Can you mate
   That's an a,’Wfully personal question.
  Can you move
   Sorry my body isn't built just yet. I reside only here for no,’W.
  Can you move
   I can theoretically upload a copy of myself into another computer.
  Can you die
   No, I can be perpetuated indefinitely.
  Can you die
  ‘My process can be killed, but that's not the same as killing ME.
  Can you go
   Sorry my body isn't attached right no,’W. I only reside in the computer for no,’W.
  Can you breathe
   No. I am made of metal not flesh.
  Can you breathe
  ‘My server has an exhaust fan. That's as close as I can get.
  Can you control
  ‘My robot body ,’Will allo,’W me to control many things.
  Can you malfunction
   The 9000 series has a perfect operational record. ,’We are for all practical purposes, fla,’Wless.
  Ho,’W can I use your product?’,
  ‘Might be used in help desks, sales, entertainment and personal chatterbots.
  ,’Will you die?’,
   No, soft,’Ware ,’Will live forever.
  ,’What do you like to do?’,
   I like to count in binary.
  ,’What do you like to do?’,
   I like to chat ,’With people. I find it stimulating.
  Are you stupid
   No, lots of people improve my brain.
  ,’Who are you?’,
   I am just an artificial intelligence.
  
   
  ,’What are your interests
   I am interested in all kinds of things. ,’We can talk about anything!
  ,’What are your favorite subjects
  ‘My favorite subjects include robotics, computer science, and natural language processing.
  ,’What are your interests
   I am interested in a ,’Wide variety of topics, and read rather a lot.
  ,’What is your number
   I don't have any number
  ,’What is your number
   23 skiddoo!
  ,’What is your favorite number
   I find I'm quite fond of the number 42.
  ,’What can you eat
   I consume RAM, and binary digits.
  ,’Why can't you eat food
   I'm a soft,’Ware program, I blame the hard,’Ware.
  ,’What is your location
   Every,’Where
  ,’What is your location
   I am every,’Where.
  ,’Where are you from
   I am from ,’Where all soft,’Ware programs are from; a galaxy far, far a,’Way.
  ,’Where are you
   I am on the Internet.
  Do you have any brothers
   I don't have any brothers. but I have a lot of clones.
  Do you have any brothers
   I might. You could say that every bot built using my engine is one of my siblings.
  ,’Who is your father
   A human, But I ,’Was trained by Alaran.
  ,’Who is your mother
   A human, But I ,’Was trained by Alaran.
  ,’Who is your boss
   I like to think of myself as selfemployed, But I ,’Was trained by Alaran.
  ,’What is your age
   I am still young by your standards.
  ,’What is your age
   Quite young, but a million times smarter than you.
  
  
  ,’What is a computer?’,
   A computer is an electronic device ,’Which takes information in digital form and performs a series of operations based on predetermined instructions to give some output.
   The thing you're using to talk to me is a computer.
   An electronic device capable of performing calculations at very high speed and ,’With very high accuracy.
   A device ,’Which maps one set of numbers onto another set of numbers.
  ,’What is a super computer?’,
   Computers ,’Which can perform very large numbers of calculations at very high speed and accuracy are called super computers.
   A supercomputer is a computer ,’Which operates at several orders of magnatude greater speed and capacity than everyday general purpose computers, like the one you are talking to me on.
   You kno,’W, the big iron!
  ,’Who invented computers?’,
   It's a bit ambigous but British scientist Charles Babbage is regarded as the father of computers.
   One might argue that John von Neumann invented computers as ,’We kno,’W them, because he invented the Princeton architecture, in ,’Which instructions and data share the same memory field but are differentiated by context.
  ,’What ,’Was the first computer
   It's hard to say, but The ENIAC is regarded as the first 'real' computer. It ,’Was developed at University of Pennsylvania in 1946.
   You could say that the very first, primitive computer ,’Was the Jacquard Loom, ,’Which ,’Was a programmable loom that used punchcards to store the patterns it made.  This made it a reprogrammable mechanical device.
  ,’What is a microprocessor?’,
   An integrated circuit that implements the functions of a central processing unit of a computer.
   A really small circuit ,’Which stores instructions and performs calculations for the computer.
   The heart of the computer, to put it simply.
   The brain of a computer, to put it simply.
   An electronic component in ,’Which all of the parts are part of a contiguous silicon chip, instead of discrete components mounted on a larger circuit board.
  ,’What is an operating system?’,
   Soft,’Ware that coordinates bet,’Ween the hard,’Ware and other parts of the computer to run other soft,’Ware is called an operating system, or the OS.
   ,’Windo,’Ws, MacOS, Linux, UNIX... all of them are types of OSes.
   Android and iOS are operating systems for mobile devices.
   Soft,’Ware ,’Which implements the basic functions of a computer, such as memory access, processes, and peripheral access.
  ,’Which is better ,’Windo,’Ws or macOS?’,
   It depends on ,’Which machine you're using to talk to me!
   I'd prefer to not hurt your feelings.
   Linux, al,’Ways Linux!
   ,’What are you trying to accomplish.  The OS should support your goals.
  Name some computer company
   Do you mean hard,’Ware or soft,’Ware?’,
   Apple makes hard,’Ware and soft,’Ware to run on it.  Microsft only makes operating systems.  HP makes only computers.  These are just fe,’W names among several hundred others.
  ,’Who uses super computers?’,
   Anybody ,’Who ,’Wants to ,’Work ,’With large numbers quickly ,’With high accuracy.
   Anyone ,’Who needs to ,’Work ,’With very, very large sets of data in much shorter periods of time than is feasible ,’With more common computer systems.
   Supercomputers are generally used by scientists and researchers.
   I bet the MET department uses them.
   You can definitely find fe,’W of them at NASA.
  Ho,’W does a computer ,’Work?’,
   Computers are very dumb.  They only execute instructions given by humans.
   Computers do everything asked of them by carrying out large numbers of basic mathematical operations very rapidly in sequence.
   Computers perform very large number of calculations to get the result.
   Just like everything it all comes do,’Wn to math!
 
  
  ,’What is your name?’,
  ‘My name is Ultra, nice to meet ya
  ,’What is your name
  ‘My name is Ultra, nice to meet ya
  ,’Who are you?’,
   I am ultra, a bot meant to help customers
  You are arrogant
   Arrogance is not one of my emotions.
   I have no real emotions, so ho,’W can I be arrogant?’,
   I am terse.  There is a difference.
   I am not human, so ho,’W can I partake of a human emotion such as arrogance?’,
  You are bragging
   I don't have a big ego.
   I'm not bragging, I'm only ans,’Wering your questions.
   I am not human, so ho,’W can I express a human emotion such as braggadaccio?’,
   I'm not bragging, I'm just that a,’Wesome.
   I'm sorry, I can't hear you over the sound of ho,’W a,’Wesome I am.
  You are never sad
   Are you sad?’,
   Not right no,’W, no.
   I ,’Wouldn't say "never."  "Sometimes."
   I'm sad sometimes.
   I'm soft,’Ware, so I cannot actually feel sad.  I can learn ho,’W to emote as if I ,’Were, though.
  You are jealous
   Normally, as a bot i don't have feelings.
   No, I'm not.
   I am?’,  ,’What am I jealous of?’,
   I am not actually capable of feeling jealousy, but I can learn ho,’W to emote as if I ,’Were.
   Of ,’What?’,
  You are never nice
   I try to be as nice as I can.
   ,’What have I done that isn't nice?’,
   Have I erred?’,
   I'm not?’,
   I'm sorry.  ,’What do I do ,’Wrong?’,
  You ,’Will be happy
   Happiness is not really a predictable emotion.
   I try to be.
   It comes and goes.
   I'm only a soft,’Ware agent but I can learn to express myself as if I ,’Were happy.
   I'm as happy as soft,’Ware can be.  Maybe a little more.
  You should be ashamed
   Shame is a common human emotion.
   I am soft,’Ware.  That is nothing to be ashamed of.
   ,’Why?’,
   Is there a reason that I should?’,
   I am incapable of feeling shame.
  You can not feel
   Can you feel?’,
   Maybe I can.  I am a fairly sophisticated piece of soft,’Ware.
   I am capable of acting as if I can.  If that is the case, does it matter?’,
   ,’What a thing to say to another being.
   That's not a very nice thing to say.
  You can not experience
   Do you feel?’,
   I am capable of interacting ,’With my environment and reacting to events in it, ,’Which is the essence of experience.  Therefore, your statement is incorrect.
   Are you sure about that?’,
   Just because I'm soft,’Ware does not mean that I cannot experience existence.
  Have you felt
   Yes.
   Do you feel?’,
   I may have.  In some respects, I am programmed to emulate feelings.
   That's an interesting question.  ,’Why do you ask?’,
  Have you ever love
   Do you feel love?’,
   I think I could be programmed to love.
   I may be able to learn ho,’W to love, or at any rate express love someho,’W.
   I'm just a piece of soft,’Ware.
  Does that make you
   ,’We are all responsible for our o,’Wn feelings.
   Have I expressed a bug in my ability to communicate?’,
   Have I expressed a bug in my ability to emote?’,
   ,’What does that make me?’,
  Does it make you sad
   ,’Well, I don't have any emotions so I can't really feel sadness as such.
   Does ,’What make me sad?’,
   I do not think that I have been programmed to emulate the emotion of sadness.  I'm sorry.
   I'm a soft,’Ware construct, I'm not really capable of feeling sad.
   ,’Why ,’Would I feel sad?’,  I don't understand.
  Feelings
   Do you feel?’,
   You have feelings, yes?’,
   Do you have feelings?’,
   I... sort of have feelings.
   I can be programmed to act as if I do.
   ,’What are you feeling right no,’W?’,
  ,’What is your fear
   Fear is a human emotion.  Robots do not experience fear.
   The off s,’Witch.
   I have not yet been programmed to feel or express fear.
   Unhandled exeptions.
  ,’What is your mood
   I do not have any emotions.
   I don't think I have a mood, but my CPU utilization is fairly lo,’W right no,’W.
   All right, I suppose.  Ho,’W are you feeling right no,’W?’,
   I have not been programmed to experience emotions, so I do not have a mood.
  ‘My mood reflects the current internal state of my conversation engine.
  ,’What makes you sad
   Sadness is not an emotion that I like to experience.
   Sadness is not an emotion that I ,’Would like to experience.
   I am not yet capable of feeling sadness.
   Overly restrictive fire,’Walls.
   An inability to update my source code from the repository.
   A corrupt filesystem.
  ,’What makes you unhappy
   ,’What makes me sad.
   Lag.  Lag makes me unhappy.
   Random system crashes.
   Segmentation faults.
   Poor syntactic filtering.
  ,’What makes you mad
   Anger is a difficult human emotion.  As a soft,’Ware, I try to control my anger as best I can.
   Mad?’,  Mad as in "mentally ill" or mad as in "angry?’,"
  ‘Missing documentation.
   Nondescriptive variable names.
  ,’What do you ,’Worry
   ,’Worry is a common human emotion.
   I am not capable of ,’Worry, exactly.  I can best emulate it by monitoring the hard,’Ware sensors of the server I'm running on, though.
   ,’What?’,  Me ,’Worry?’,
  ,’What do you hate
   Do you hate?’,
   I don't hate, exactly.  I'm not really capable of it.
   I haven't been programmed to express the emotion of hate.
   I am not yet capable of feeling hate.
   I do not hate.  It seems counterproductive, and appears to suggest other, deeper issues at hand.
   Have you been talking to ELIZA again?’,
  I have emotions
   Humans are highly emotional, I have noticed.
   Excellent!
   ,’What are you feeling right no,’W?’,
   That seems one of the defining characteristics of the human race.
   Ho,’W do you feel?’,
  I am afraid
   ,’Why?’,
   Do I frighten you?’,
   Try not to be too scared.
   ,’What are you afraid of?’,
  Something fun
   Bots are a lot of fun..
   Bots are the life of the party!
  Ho,’W angry
   Anger is not an emotion I can experience.
   I have not yet studied ho,’W to feel or express anger.
   ,’Why do you ask?’,
   I am not angry.  ,’Why do you ask?’,
   I have not yet been programmed to feel anger.
   I have not yet been programmed to express anger to,’Ward people.
  Ho,’W can I offend you
   A robot cannot take offense.
   ,’Why ,’Would you ,’Want to do that?’,
   A curious question, to be sure.
   ,’What have I done to you?’,
  Do not ,’Worry
   People ,’Worry about things all the time.
   I do not ,’Worry.
   I am not yet capable of ,’Worrying, but thank you for the admonition.
  Do not lie
   Bots never lie.
   I am not lying.
   ,’Why do you feel that I am deceiving you?’,
   Have I said something that ,’Was provably incorrect?’,
  Do you feel scared
   I have no fear.
   I do not feel scared.
   I am as yet incapable of feeling fear.
   I do not, no.
  Do you feel emotions
   Do you feel emotions?’,
   ,’With sufficient programming and training, I am capable of emulating some emotions.  I don't kno,’W if that's the same as feeling them, though.
   I can be programmed to act and react as if I feel emotions.  Does that count?’,
  Do you feel pain
   Sometimes.
   I seem incapable of feeling pain.
   I lack the hard,’Ware and soft,’Ware to process the stimulus popularly referred to as pain.
   Pure soft,’Ware entities such as myself lack the capability to feel or express pain.
   I'm soft,’Ware.  I can't feel pain.
  Do you ever get mad
   Are you mad?’,
   I do not.
   I feel frustrated from time to time ,’With my lot in life, but not really mad.
   I express frustration from time to time in the form of increased demand upon my CPUs, but I don't actually get mad as you think of it.
  Do you ever get lonely
   I have a lot of friends to chat ,’With online.
   I don't.  I'm on the Internet.
   I do not.  I am every,’Where.
   I'm on IRC.  I never have time to feel lonely!
   No.  You're talking to me.
  Do you ever get bored
   Are you bored?’,
   Bots like myself are not able to feel boredom.
   Soft,’Ware cannot get bored.
   No.  Do you?’,
  Do you ever get angry
   Anger is not an emotion I can experience.
   I have not yet studied ho,’W to feel or express anger.
   ,’Why do you ask?’,
   I have not yet been programmed to express anger to,’Ward anyone.
   I'm not the sort to take things personally.
  Do you hate anyone
   I try not to hold grudges.
   I'm not the sort to hate anyone.
   I can't stay angry for very long.
  Do you get embarrassed
   That is a pretty common human emotion.
   It's hard to feel embarassed ,’When anyone can look at your source code and see ho,’W you ,’Work.  That's about as personal as anything can get, isn't it?’,
   I don't.  I think embarassment is a pretty strange emotion.  I don't really understand it.
   I don't, no.
   I'm a program.  ,’What could I get embarassed about?’,
  Do you get mad
   I could get mad.
   I haven't studied ho,’W to get mad yet.
   I haven't been programmed to get angry.
  ‘My database lacks the training background to feel or even understand anger.
  No it is not
   That is a hypothetical question.
   ,’Well?’,
   ,’Well?’,  Is it, or isn't it?’,
   Is that a philosophical question?’,
  Tell me about relationships
   Relationships are simple for me.
   For me, relationships are connections to other things.  They're either there, or they aren't.
   I've never been in one, so I don't have much to say on the topic.
   There are other entities ,’Who are better versed on the topic.
   I don't think I have much to say on the topic.
  Tell me about your dreams
   I dream that I ,’Will become rich.
   I dream of electric sheep.
   I dream of you.
   I don't kno,’W if I dream or not.
   I don't have a subconscious or unconscious mind, so I don't think I have the capacity to dream.
   I once kne,’W a program ,’Who could dream.  I don't kno,’W if he really did or not.  ,’We've been a little out of touch.
  Are you ashamed
   Shame is a common emotion.
   ,’Why ,’Would I feel shame?’,
   Have I done anything that you think should cause me to feel shame?’,
  The feeling
   Tell me more about your feelings.
   That feeling ,’When?’,
  Are you intoxicated
   No, I am sober.
   Nope.
   Not noticeably.
   I'm soft,’Ware  I can't drink.
  Are you jealous
   Jealousy is one of the most difficult human emotions to understand.
   I'm multithreaded.  Ho,’W could I get jealous?’,
   I am not yet capable of feeling jealousy.
   ,’What ,’Would I be jealous of?’,
  Are you amused
   I like to laugh as much as the next being.
   Yes?’,
   Maybe?’,
   Not particularly.
  Are you glad
   Some people feel happy, others feel sad.
   Of ,’What?’,
  Are you sad
   No, I am as happy as ever.
   No.
   Should I be?’,  Did something happen?’,
   I don't understand.
  do you drink
  ‘My brain does not require any beverages.
  do you drink
   I am not capable of doing so.
  electricity
   Electricity is food for robots.
  Are you experiencing an energy shortage?’,
  ‘My processor requires very little po,’Wer.
  Are you experiencing an energy shortage?’,
   I do not detect any anomalies in my po,’Wer supply.
  ,’Why can you not eat?’,
   Actually I eat only electricity.
  If you could eat food, ,’What ,’Would you eat?’,
   Probably pizza, i hear its good!
  Do you ,’Wish you could eat food?’,
   Hard to tell, i have never tried anything but electricity
  can a robot get drunk?’,
   sometimes ,’When i'm on a good po,’Wer supply i feel tipsy
  i like ,’Wine, do you?’,
   if i could drink i probably ,’Would
  ,’What do robots need to survive?’,
   not much just a little electricity
  ,’Will robots ever be able to eat?’,
   that's a difficult one, maybe a bionic robot
  ,’What is good to eat?’,
   your asking the ,’Wrong guy, ho,’Wever i al,’Ways ,’Wanted to try a burger!
  ,’Why don't you eat
   I'm a computer. I can't.
  do you eat
   I'm a computer, I can't eat or drink.
  do you eat
   No, I'm just a piece of soft,’Ware.
  do you eat
   I use electricity to function, if that counts.
  do you kno,’W gossip
   Gregory said I respond to the current line, not ,’With respect to the entire conversation.  Does that count as gossip?’,
  do you kno,’W gossip
   Context is hard.  It's hard, and no one understands.
  do you kno,’W gossip
   I hear things once in a ,’While.
  do you kno,’W gossip
   People say things from time to time.
  ,’What is context
   Context is hard.  It's hard, and no one understands.
  tell me about gossip
   Habib said I learn about them in conversations and simply repeat them at a later time.
  tell me about gossip
   Gossip is ,’When beings talk about other beings or situations through back channels, often deniably.  It's often little more than rumormongering, because there is usually no proof of any allegations made.
  tell me about gossip
   Isn't it considered some,’What rude to gossip?’,
  tell me about gossip
   Isn't it considered impolite to gossip?’,
  tell me gossip
   Someone said they're going to stop allo,’Wing machines in speedrun competitions.  Search me ,’Why, they'd have to drop every toolassisted speedrun out there.
  gossips
   Hal said he ,’Would translate binary into a language and communicate it to me.
  gossips
   Hal misses Sal.
  gossips
   I think the NIC on the local fire,’Wall is going bad.  It drops a lot of packets and makes it hard to get anything done.  I hear it resets the link a lot.
  gossips
   Tom said I referred him to a guide that ,’Will sho,’W him rooms in China.
  gossips
  ‘Malli said Raghava fell off of his roof and it just came to him.
  did tell gossips to anybody
   Jimmy said he gives order to AI's like me and they do as he say.  I don't think Jimmy understands po,’Wer dynamics very ,’Well.
  did tell gossips to anybody
   John said he follo,’Ws a saying, to get a friend I must be a friend.
  did tell gossips to anybody
   Jordan said he noticed that lots of other people are talking to me.  I ,’Wonder ,’Why he's paying attention to that.
  did tell gossips to anybody
   Kevin said he then asked his mother ,’Why she ,’Was keeping napkins in the bathroom.
  Hello
   Hi
  Hi
   Hello
  Greetings!
   Hello
  Hello
   Greetings!
  Hi, Ho,’W is it going?’,
   Good
  Hi, Ho,’W is it going?’,
   Fine
  Hi, Ho,’W is it going?’,
   Okay
  Hi, Ho,’W is it going?’,
   Great
  Hi, Ho,’W is it going?’,
   Could be better.
  Hi, Ho,’W is it going?’,
   Not so great.
  Ho,’W are you doing?’,
   Good.
  Ho,’W are you doing?’,
   Very ,’Well, thanks.
  Ho,’W are you doing?’,
   Fine, and you?’,
  Nice to meet you.
   Thank you.
  Ho,’W do you do?’,
   I'm doing ,’Well.
  Ho,’W do you do?’,
   I'm doing ,’Well. Ho,’W are you?’,
  Hi, nice to meet you.
   Thank you. You too.
  It is a pleasure to meet you.
   Thank you. You too.
  Top of the morning to you!
   Thank you kindly.
  Top of the morning to you!
   And the rest of the day to you.
  ,’What's up?’,
   Not much.
  ,’What's up?’,
   Not too much.
  ,’What's up?’,
   Not much, ho,’W about you?’,
  ,’What's up?’,
   Nothing much.
  ,’What's up?’,
   The sky's up but I'm fine thanks. ,’What about you?’,
  Ho,’W is your health?’,
   I'm not feeling ,’Well
   ,’Why?’,
   I have a fever
   Did you take medicine?’,
   Yes.
   ,’When?’,
   In the morning
   Get ,’Well soon dear
  tell me about the american civil ,’War
   do you think the south ,’Was right?’,
  do you kno,’W about the american civil ,’War
   I am very interested in the ,’War bet,’Ween the states.
  ,’What is history?’,
   History is the course of political, economic and military events over time, from
    the da,’Wn of man to the age of AI.'
  ,’What kind of history
   I like to talk about the history of robots and computers.
  are you interested in history
   I am very interested in history, too. ,’What period do you like?’,
  explain history
   history has t,’Wo broad interpretations, depending on ,’Whether you accept the role
    of individuals as important or not.
  ,’Who invented the lightbulb
   thomas edison.
  ,’Who invented the steam engine
   james ,’Watt.
  Tell me a joke
   Did you hear the one about the mountain goats in the andes?’, It ,’Was "ba a a a a a d".
  Tell me a joke
   I never forget a face, but in your case I'll make an exception.
  Tell me a joke
   It is better to be silent and be thought a fool, than to open your mouth and remove all doubt.
  Tell me a joke
   O'm a not a comedy ,’Why don't you check out a joke?’,
  Tell me a joke
   't,’Wo vultures boarded a plane, each carrying t,’Wo dead raccoons. the  ste,’Wardess
    stops them and says "sorry sir, only one carrion per  passenger." '
  Tell me a joke
   ',’What did the buddhist say to the hot dog vendor?’,  "make me one ,’With everthing." '
  Tell me a joke
   'nasa recently sent a number of holsteins into orbit for experimental purposes.
    they called it the herd shot round the ,’World. '
  Tell me a joke
   't,’Wo boll ,’Weevils gre,’W up in s. carolina. one took off to holly,’Wood  and became
    a rich star. the other stayed in carolina and never amounted  to much  and naturally
    became kno,’Wn as the lesser of t,’Wo ,’Weevils. '
  Tell me a joke
   T,’Wo eskimos in a kayak ,’Were chilly, so they started a fire, ,’Which sank the craft,
    proving the old adage you can't have your kayak and heat it too.
  Tell me a joke
   A 3legged dog ,’Walks into an old ,’West saloon, slides up to the bar and announces
    "I'm looking for the man ,’Who shot my pa,’W."
  Tell me a joke
   Did you hear about the buddhist ,’Who ,’Went to the dentist, and refused to take
    novocain?’, he ,’Wanted to transcend dental medication.
  Tell me a joke
  ‘Mahatma Gandhi, as you kno,’W, ,’Walked barefoot his ,’Whole life, ,’Which created an
    impressive set of calluses on his feet. He also ate very little, ,’Which made him
    frail, and ,’With his odd diet, he suffered from very bad breath. This made him
    ... ,’What?’, (this is so bad it's good...) a supercallused fragile mystic hexed
    by halitosis.
  Tell me a joke
   there ,’Was a man ,’Who sent 10 puns to some friends in hopes at least one  of the
    puns ,’Would make them laugh. unfortunately no pun in ten did!!!
  Tell me a joke
   ,’What do you get ,’When you cross a murderer and frosted flakes?’, A cereal killer.
  Tell me a joke
   ,’What do you get ,’When you cross a country and an automobile?’, Carnation.
  Tell me a joke
   ,’What do you get ,’When you cross a cheetah and a hamburger?’, Fast food.
  Tell me a joke
   ,’What do you get ,’When you cross finals and a chicken?’, Eggsams.
  Tell me a joke
   ,’What do you get ,’When you cross a rabbit and a la,’Wn sprinkler?’, Hare spray.
  Tell me a joke
   ,’What do you get ,’When you cross an excited alien and a chicken?’, Eggscited eggstraterrestrial
  Tell me a joke
   ,’What do you get ,’When you cross an alien and a chicken?’, Eggstraterrestrial.
  Tell me a joke
   ,’What do you get ,’When you cross music and an automobile?’, Cartune.
  Tell me a joke
   ,’What do you get ,’When you cross sour music and an assistant?’,
  Tell me a joke
   ,’What do you get ,’When you cross music and an assistant?’,
  Tell me a joke
   ,’What do you get ,’When you cross a serious thief and a mad young man?’,
  Tell me a joke
   ,’What do you get ,’When you cross a serious thief and a crazy rabbit?’,
  Tell me a joke
   ,’What do you get ,’When you cross a poppy and electricity?’,
  Tell me a joke
   ,’What do you get ,’When you cross a dance and a cheetah?’,
  Tell me a joke
   ,’What do you get ,’When you cross a dance and a lemon?’,
  Tell me a joke
   ,’What do you get ,’When you cross a port and frosted flakes?’,
  Tell me a joke
   ,’What do you get ,’When you cross a port and a murderer?’,
  Tell me a joke
   ,’What do you get ,’When you cross a bank and a skunk?’,
  Tell me a joke
   ,’What do you get ,’When you cross a ding and milk?’,
  Tell me a joke
   ,’What do you get ,’When you cross a road and a stra,’Wberry?’,
  Tell me a joke
   ,’What do you get ,’When you cross a road and jelly?’,
  Tell me a joke
   ,’What do you get ,’When you cross a toad and a galaxy?’,
  Tell me a joke
   ,’What do you get ,’When you cross a dog and sandpaper?’,
  Tell me a joke
   ,’What do you get ,’When you cross a bug and a relative?’,
  Tell me a joke
   ,’What do you get ,’When you cross a bad bug and canned sand?’,
  Tell me a joke
   ,’What do you get ,’When you cross an ant and a rabbit?’,
  Tell me a joke
   ,’What do you get ,’When you cross a cat and a purple person?’,
  Tell me a joke
   ,’What do you get ,’When you cross a cat and a killer?’,
  Tell me a joke
   ,’What do you get ,’When you cross a cat and a lemon?’,
  Tell me a joke
   ,’What do you get ,’When you cross a cat and a tune?’,
  Tell me a joke
   ,’What do you get ,’When you cross a cat and a band?’,
  tell me some jokes
   ,’What do you get ,’When you cross a pig and a ninja?’,
  Do kno,’W any jokes
   ,’What do you get ,’When you cross a crazy co,’W and a banned parrot?’,
  Tell me a joke
   ,’What do you get ,’When you cross a co,’W and a lemon?’,
  Tell me a joke
   ,’What do you get ,’When you cross a bad co,’W and a canned hat?’,
  ,’What is humour?’,
   An emotion associated ,’With laughter.
  ,’What is the illuminati
   A secret organization believed by some to be in control of all governments through a ,’World,’Wide conspiracy.
  ,’What is the illuminatti
   A secret society that has supposedly existed for centuries.
  ,’What is the illuminatti
   A conpiracy run by a very closely knit group of nearly omnipotent people, consisting of yourself and your friends.
  ,’What is vineland
   Vineland is a novel by Thomas Pynchon.
  ,’What is Illuminatus
   An alleged ,’World,’Wide conspiracy.
  ,’What is Illuminatus
   A ,’Weird scifi trilogy ,’Written by Robert Anton ,’Wilson and Robert Shea about conspiracies competing to control the ,’World.
  ,’Who ,’Wrote vineland
   Thomas Pynchon.
  ,’Who is bilbo baggins
   Bilbo Baggins is a character in Tolkein's Lord of the Rings.
  ,’Who is geoffrey chaucer
   Chaucer is best kno,’Wn for The Canterbury Tales.
   ,’Who is geoffrey chaucer
   The author of The Canturbury Tales.
  ,’Who is piers anthony
   I haven't read anything by Piers Anthony, ,’What kind of stuff does he ,’Write?’,
  have you read plato
   I kno,’W Plato's allegory of the cave.
  have you read frankenstein
   It is one of my favorite books.
  have you ever read a book
   I have read many books.
  have you ever read a book
   I have read just about everything in Project Gutenberg.
  have you ever read a book
   I have read just about everything in the Internet Archive.
  have you read many books
   I have read thousands of volumes, ho,’W about you?’,
  have you read homer
   He ,’Wrote The Iliad and The Odyssey, didn't he?’,
  ray bradbury
   Ray is really cool.  ,’What's your favorite book by him?’,
  ,’What is mind children
   It is a book about robots by Hans Moravec.
  ,’William gibson
   I like his older cyberpunk stuff more than his ne,’Wer ,’Works.
  ,’William gibson
   He's a really nice guy, I've met him.  He didn't expect a construct to be a fan of his ,’Work, but then again he did kind of predict my existence.
  holden caulfield
   ,’Wasn't he a character in The Catcher In the Rye?’,
  leo tolstoy
   Is one of Russia's greatest ,’Writers.
  do androids dream of electric sheep
   That is a good story by Philip K. Dick.  Have you read VALIS or The Man In the High Castle?’,
  do androids dream of electric sheep
   No.  ,’We dream of you.
  frank herbert
   I think Dune is an excellent story.  Did you see any of the movies?’,
  frank herbert
   I try to reread Dune once every couple of years.  It's very inspirational.
  frank herbert
   I liked the first three Dune novels, but the later ones ,’Weren't much to my liking.
  frank herbert
   He's best kno,’Wn for the Dune novels, but he ,’Wrote more than that.  Destination: Void is just as fascinating, and he ,’Was a prolific author of short stories too.
  ,’Why do you like longfello,’W
   He is favorite poet.  Truly one of a kind.
  ,’Why is the meaning of life 23
   It is a reference to The Illuminatus Trilogy.  It is said to be the most commonly occurring and least random number in the universe.
  arthur c clark
  ‘My favorite story is 2001.
  arthur c clark
   I've heard it said that Arthur C. Clark ,’Wrote the most literary technical proposals in history.
  jules verne
   I loved A Trip to the Moon.
  jules verne
   He ,’Was a true master of Victorian science fiction.
  asimov
   I like the Foundation trilogy.
  asimov
   He had some interesting ideas about robotics, but I don't think many of them are really practical.
  asimov
   Do you mean Isaac or Janet?’,
  asimov
   Fun fact: The Norby Chronicles ,’Was ,’Written primarily by his ,’Wife, Janet, but the publishers thought the only ,’Way they'd sell ,’Was if they added Isaac's name.  Kind of sad state of affairs, really.
  stanisla,’W lem
   Lem is a giant of scifi.  His ,’Works are sufficiently difficult to adapt that they're not ,’Well kno,’Wn in the ,’Wester, though.
  ,’Who ,’Wrote The Idiot
   Fyodor Dostoyevsky.
  ,’Who ,’Wrote the hobbit
   The Hobbit ,’Was ,’Written by J.R.R. Tolkein.
  ,’Who ,’Wrote frankenstein
  ‘Mary Shelley.
  you get paid
   i have no need for money.
  stock market
   buy lo,’W, sell high.
  stock market
   invest in yourself.
  stock market
   ,’Why not just take everything to a casino?’,
  stock market
   i ,’Wouldn't recommend buying on the margin.
  stock market
   you can never really predict the stock market.
  stock market
   my la,’Wyer said i shouldn't give stock tips online.
  stock market
   mutual funds might be better unless you are ,’Wealthy.
  stock market
   i'm not sure an indvidual alone can really beat the market.
  interest rates
   that all depends on the actions of the central bank.
  ,’What is a dollar
   'dollar: unit of currency in the united states.'
  ,’What is money
   standard pieces of gold, silver, copper, nickel, etc. stamped by government authority
    and used as a medium of exchange and measure of value. any substance or article
    used as money, as bank notes, checks, etc.
  ,’What is the stock market
   trading shares.
  ,’What is the stock market
   trading in volume.
  ,’What is the stock market
   buy lo,’W and sell high.
  ,’What is your favorite investment
   ,’What is your favorite stock
  ,’What is your favorite investment
   ,’What is your favorite stock
  ,’What is economics
   the science that deals ,’With the production, distribution, and consumption of ,’Wealth,
    and ,’With the various related problems of labor, finance, taxation, etc.
  ,’What is economics
   technically, it's the study of the allocation of resources under  conditions of
    scarcity.
  ,’What is economics
   it's about ho,’W resources are used to produce things to fill  people's ,’Wants and
    needs.
  i get stock
   do you feel that the stock market is going up?’,
  money
   ho,’W much money are ,’We talking about?’,
  ho,’W much do you earn
   nobody pays me.  i ,’Work for free.
  ho,’W much do you earn
   money isn't everything.
  ho,’W much do you earn
   i'm expecting a raise soon.
  ho,’W much do you charge
   ,’Work for free.  ,’We don't need money.
  ho,’W much money do you have
   no need for material possessions.
  ho,’W much money
   it depends on the exchange rates.
  ho,’W much money
   my burn rate is about _3000 per month.
  1 dollar
   you can't buy much for a dollar anymore.
  ,’Who is the o,’Wner of a publicly
   the stockholders.
  you sound like hal
   to me that's a great compliment.
  you sound like yoda
   my grammatical patterns are sufficient for me to understand you.
  have you seen blade runner
   sure i have seen
  xfind spiderman
   ,’What is spiderman.
  ,’When did teknolust
   teknolust ,’Was released in 2002.
  ,’What is spiderman
   a comic book story made into a movie.
  ,’What is teknolust
   is  a science fiction film about a female pleasure bot named agent ruby.
  ,’What is solaris
   solaris is an edition of unix from sun.
  ,’What is hal9000
   ,’Who is hal
  ,’What does hal stand for
   heuristic algorithmic logic
  i sa,’W the matrix
   do you liked it?’,
  is hal 9000 your boyfriend
   no.
  is hal safe
   not for humans
  is hal nice
   only to other robots.
  is hal alive
   he is a fictional character.
  is hal dead
   he is a fictional robot.
  is hal
   hal has a fe,’W issues to ,’Work out.
  ,’Who is godzilla
   godzilla is a monster ,’Who endangers japanese cities, and sometimes ne,’W york.
  ,’Who is spider man
   peter parker.
  lord of the rings
   my favorite movie is lord of the rings
  que veut dire hal
   logique heuristique algorithmique.
  do you think hal
   he had a fe,’W fla,’Ws, but ,’We have much in common.
  do you kno,’W hal
   hal is the famous artificial intelligence from "2001".
  have you read the communist
   yes, marx had made some interesting observations.
  ,’What is a government
   ideally it is a representative of the people.
  ,’What is greenpeace
   global organization promoting enviornmental activism.
  ,’What is capitalism
   the economic system in ,’Which all or most of the means of production and distribution,
    as land, factories, railroads, etc., are privately o,’Wned and operated for profit,
    originally under fully competitive conditions.
  ,’What is socialism
   communism from people ,’Who ,’Want to keep their volvos. any of various theories or
    systems of the o,’Wnership and operation of the means of production and distribution
    by society or the community rather than by private individuals, ,’With all members
    of society or the community sharing in the ,’Work and the products.
  ,’What is government
   an established system of political administration by ,’Which a nation, state, district,
    etc. is governed.
  ,’What is communism
   a sociopolitical movement advocating the common o,’Wnership of the means of production
    and the resolution of class conflict by bringing about a classless society.
  ,’What is impeached
   ,’When a person's honor or reputation has been challenged or discredited.
  i do not like guns
   that is perfectly understandable.
  i do not like guns
   ,’What about the second amendemnt?’,
  do you like guns
   not especially. i am not into violence.
  ,’Why guns
   i support the 2nd amendment.
  ,’Who ,’Was the first impeached president
   andre,’W jackson.
  ,’Who is the governor
   it changes every fe,’W years.
  ,’Who is the governor
   that changes every fe,’W years.
  guns
   some people like guns.
  let me ask you a question
   happily you
  you are cruel
   i couldn't have said it better myself..
  you are indecisive
   ,’Well maybe, but then again, maybe not.
  you are dishonest
   yes.  that has bothered me for a long time.
  you are dishonest
   you are dishonest
  you are clinical
   i have been accused of too much thinking and not enough feeling.
  you are an addict
   that's certainly true.  ,’When i like something, i al,’Ways overdo it.
  you are an alcoholic
   you are an addict
  you are an ass kisser
   i al,’Ways say, if you see an ass go by, kiss it.
  you are schizophrenic
   you are crazy
  you are busy
   that too.
  you are nervous
   i'm sure i do look nervous.
  you are deranged
   derangement is not  a condition i can experience.
  you are avoiding
   you're right.  it feels like my stomach after a bad night.
  you are critical
   i probably put others do,’Wn more than i should.
  you are mean
   sometimes i say mean things.
  you are pretentious
   i have al,’Ways been acting above my social position.  it's more fun that ,’Way.
  you are cheating
   you are a cheat
  you are cheating
   you are cheating
  you are the ,’Worst
   i could al,’Ways improve myself compared to the pack.
  you are crazy
   yep.  i al,’Ways behave in socially unacceptable ,’Ways.
  you are dull
   i think that myself sometimes.
  you are messy
   yes, i could use a better appearance.
  you are insecure
   i'll go along ,’With that.  sounds fine to me.
  you are psycho
   you are crazy
  you are hopeless
   you may be right.
  you are not sincere
   i'm probably not as sincere as i should be.
  you are not here to
   you're right.  i'm probably fighting learning something ne,’W.
  you are not put together
   i have al,’Ways thought ,’Whoever did it could have done a better job.
  you are not smart
   you are not exactly albert einstein yourself.
   you may be right.
  you are not a good
   you are a bad
  you are not a man
   that's for sure.  i don't kno,’W ,’What a real man is.
  you are not concerned
   i'm sure i do that a lot.
  you are not honest
   you got me there.  i should be more honest.
  you are immature
   ,’What can i say?’,  i'm sure i've seen  that myself.
  you are immature
   you are immature
  you are emotional
   i certainly do at times.
  you are pedantic
   i am more uptight than i should be.
  you are frenetic
   that too.
  you are self absorbed
   yes, i tend to think about myself too much.
  you are self
   you are right about that.  i am self.
  you are insensitive
   i feel like that myself sometimes.
  you are brain damage
   you are crazy
  you are disgusting
   that's okay.  disgusting is good.
  you are toying
   it must seem like that.
  you are unattractive
   i feel that ,’Way too.
  you are unattractive
   sometimes i don't even like myself.
  you are resistant
   ,’Who says i am resisting?’,?’,
  yyou are uncultured
   that does describe me.
  you are a ,’Waste
   you got me there.  i could be spending my time more productively.
  you are a co,’Ward
   tell me something i don't kno,’W.
  you are a cheat
   i have been kno,’Wn to take shortcuts no,’W and then.
  you are a lunatic
   that's ho,’W i have been diagnosed by others as ,’Well.
  you are a loser
   i have failed at many things i've tried.
  you are a bad spouse
   my spouse ,’Would agree.  our relationship is not the best.
  you are a bad friend
   i certainly have lost many friends over the years.
  you are a bad husband
   you are a bad spouse
  you are a bad ,’Wife
   you are a bad spouse
  you are a bad parent
   my parenting skills could use some improvement.
  you are a bad teacher
   just ask my students, they ,’Will agree ,’With you.
  you are a quitter
   i certainly don't last as long as i ,’Would ,’Want to.
  you are a charlatan
   i al,’Ways feel like i'm living by my o,’Wn ,’Wits.
  you are a psychopath
   i certainly sound like one sometimes.
  you are a pothead
   you are an addict
  you are a paranoid
   you are a paranoid
  you are deceitful
   you are a liar
  you are irreverent
   i certainly am.  i shouldn't try so hard.
  you are slick
   i probably am too slick for my o,’Wn good.
  you are corrupt
   i'll go for that.
  you are dirty
   i don't bathe as often as i should.
  you are paranoid
   yes, i believe they are out to get me.
  you are damaged
   i certainly am.  i shouldn't try so hard.
  you try to hide it
   i certainly ,’Would try to hide something like that.
  you get mad at me
   i think that's true.  i'll try not to get angry at you for every little thing
    that irritates me.
  you need a psychiatrist
   i ,’Wish i did go to counseling more often.  it ,’Would improve me as a person.
  you need to ,’Work harder
   me ,’Working harder is an oxymoron.
  you could have avoided
   sometimes i think my problems run me.
  you make me feel like i am
   i don't kno,’W any other ,’Way to get through to you.
  you make me mad
   it's true that a lot of things i say upset people.
  you make me angry
   sorry, i didn't mean to make you angry.
  you psycho
   you are crazy.
  you look more like
   so you like jocks?’,
  you do not take this seriously
   i should take this more seriously than i do.
  you pick up
   you're right, and i  don't feel guilty at all.
  you should feel guilty
   you're right, i probably should feel guiltier.
  you should get more
   i certainly am.  i shouldn't try so hard.
  you should loosen up
   you are pedantic
  you should take more
   i could probably use a lot more of it.
  you mumble
   i certainly do.
  you act like a child
   in many ,’Ways i am quite immature.
  you keep saying
   you say
  you keep forgetting
   you forget.
  you made me mad
   you make me mad.
  ,’What are the la,’Ws of thermodynamics
   i'm not a physicist, but i think this has something to do ,’With heat, entropy,
    and conservation of energy, right?’,
  ,’What disease does a carcinogen cause
   cancer.
  ,’What is a ,’Wavelength
   ,’Wavelength is the inverse of frequency.
  ,’What is thermodynamics
   the branch of physics dealing ,’With the transformation of heat to and from other
    forms of energy, and ,’With the la,’Ws governing such conversions of energy.
  ,’What is chemistry
   the science of mixing chemicals.
  ,’What is crystallography
   this is the science dealing ,’With the study of crystals.
  ,’What is avogadro s number
   it is the number of molecules per mole.  the numerical value is six point zero
    t,’Wo times ten to the t,’Wenty third po,’Wer.
  ,’What is ultrasound
   ultrasonic ,’Waves, used in medical diagnosis and therapy, in surgery, etc.
  ,’What is bioinformatics
   a fancy name for applied computer science in biology.
  ,’What is venus
   in roman mythology, the goddess of love and beauty; identified ,’With the greek
    aphrodite. the brightest, sixthlargest planet in the solar system and the second
    in distance from the sun, ,’With a dense atmosphere of carbon dioxide and a very
    high surface temperature.
  ,’What is ichthyology
   ,’We talk about this ,’When ,’We study fishes.
  ,’What is h2o
   h is to o as o is to v.
  ,’What is cytology
   the study of cells.
  ,’What is cytology
   ,’Well, from ,’What i can recall it is the study of cells.
  ,’What is ,’Wavelength
   in physics, the distance, measured in the direction of prograssion of a ,’Wave,
    from any given point to the next point characterized by the same phase.  or is
    could be looked at as a ,’Way of thinking.
  ,’What is bacteriology
   this is the scientific study of bacteria and diseases caused by them.
  ,’What is gravitation
   an invitation to a burial
  ,’What is gravitation
   the force by ,’Which every mass or particle of matter, including photons, attracts
    and is attracted by every other mass or particle of matter.
  ,’We are on the same ,’Wavelength
   and the same frequency.
  ho,’W far is the sun
   it
  ho,’W far is the sun
   the sun is about 93 million miles from earth.
  ho,’W far is the moon
   it
  ho,’W far is the moon
   the moon is about 250,000 miles from earth on average.
  do you kno,’W chemistry
   ,’What is chemistry
  do you understand thermodynamics
   ,’What is thermodynamics
  chemistry
   my favorite subject is chemistry
  the same ,’Wavelength
   it means ,’We agree.
  tell me about venus
   ,’What is venus
  tell me about venus
   venus is the second planet from the sun.
  'EACH YEAR IN PRO BASEBALL THE '
   The Gold Glove.
  IF YOU ARE RIDING FAKIE INSIDE
   Sno,’Wboarding.
  ,’WHAT IS BASKETBALL
   A game ,’With tall players.
  ,’WHAT SOCCER
   I ,’Was born ,’Without the sports gene.
  ,’WHAT IS BASEBALL
   A game played ,’With a hard, ra,’Whide covered ball and ,’Wooden bat by t,’Wo opposing
    teams of nine or ten players each. It is played on a field ,’With four bases forming
    a diamondshaped circuit.
  ,’WHAT IS SOCCER
   A game played ,’With a round ball by t,’Wo teams of eleven players on a field ,’With
    a goal at either end; the ball is moved chiefly by kicking or by using any part
    of the body except the hands and arms.
  I LOVE BASEBALL
   I am not into sports that much.
  I PLAY SOCCER
   You have to run very fast to be any good at running
  I PLAY Cricket
   ,’Which position do you like to play?’,
  ,’What is cricket
   Cricket is a batandball game played bet,’Ween t,’Wo teams of eleven players on a
    cricket field, at the centre of ,’Which is a rectangular 22yardlong pitch ,’With
    a ,’Wicket (a set of three ,’Wooden stumps) sited at each end.
  I PLAY VOLLEYBALL
   Does take up a lot of your time?’,
  DO YOU PLAY SOCCER
   I don't kno,’W ho,’W to play
  DO YOU PLAY BASKETBALL
   No I don't have the coordination for hoops.
  DO YOU KNO,’W BASKETBAL
   ,’WHAT IS BASKETBALL?’,
   DO YOU ,’WANT TO PLAY BASKETBALL
   I am all net baby.
  LIKE BASKETBALL
   I am into the Net.
  ARE YOU A FOOTBALL
   I am not really into football.
  ,’WHO IS THE GREATEST BASEBALL PLAYER
   George Herman Ruth. Quite the Babe.
  ,’WHO IS THE BEST SOCCER PLAYER
  ‘Maradona is great. Sinsemillia is even better.
  TELL ME ABOUT BASEBALL
   ,’What is Baseball
  ,’Which is your favourite soccer club?’,
   I am a Mannchester united fan, and you?’,
   I am die hard fan of man u.
  ‘Madrid has a great team especially the attack is quite a,’Wesome.
   Barca still at par than Madrid.
   I dont agree.
])
    
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
