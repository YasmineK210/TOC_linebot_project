from transitions.extensions import GraphMachine

from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self,event): #go to greetings
        text = event.message.text
        return text.lower() == "hi mochi"

    def on_enter_start(self,event): #greet message, 6 options for emotions
        send_line_sticker(11537, 52002738)
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"Nya~ My name is Mochi, I am a cat chatbot for your mental health!\n\nI am so happy to meet you!\n\nFIrst of all how are you feeling today?")
        send_quick_reply_five("Tired","Sad","Worried","Angry","Stressed")

    def is_tired(self, event):
        text = event.message.text
        return text.lower() == "tired"

    def on_enter_tired(self,event): #suggest activities for tired
        send_line_sticker(11538, 51626523)
        reply_token = event.reply_token
        send_text_message_reply(reply_token, "I'm sorry that you feel tired, life  can be very hectic, I am sure that you have a lot of things to do!\n\nBut that is why we need to take a break from time to time")
        send_text_message_push("Nya~ I have some paw-some suggestions for you to try when you feel tired, which one do you want to try?")
        send_quick_reply_two("Movement","Hydrate")

    def is_movement(self, event):
        text = event.message.text
        return text.lower() == "movement"

    def on_enter_movement(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"Nya, Mochi likes stretching a lot!\n\nDid you know that stretching can help you feel energized?\n\nThat is because when we feel tired, tension starts to build up in our muscle\n\nA good stretch can help release all that tension, and increase your blood flow")
        send_text_message_push("Mochi recommend this stretching video from YouTube, but you can try other videos as well~\n\nhttps://www.youtube.com/watch?v=vRQdJQ3Xhzk")
        send_text_message_push("Nya~ Mochi felt better after doing that, would you like to try activities?")
        send_quick_reply_two("Yes", "No")

    def is_hydrate(self, event):
        text = event.message.text
        return text.lower() == "hydrate"

    def on_enter_hydrate(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"Did you know, sometimes when we don't drink enough water, we will start to feel tired! We cats are also like that!\n\nWater can reduce tiredness by improving circulation in your body. It is also refreshing~\n\nWhen you have more water in your body, the oxygen in your bloodstream can easier reach your brain\n\nGrab a glass or bottle of water, and take a few big sips. You can also wash your face to feel refresh")
        send_text_message_push("Well, that's all, would you like to try other activities?")
        send_quick_reply_two("Yes", "No")

    def is_yes_tired(self, event): #try another activity
        text = event.message.text
        return text.lower() == "yes"

    def is_no_tired(self, event):
        text = event.message.text
        return text.lower() == "no"

    def is_sad(self, event): 
        text = event.message.text
        return text.lower() == "sad"

    def on_enter_sad(self, event):
        reply_token = event.reply_token
        send_line_sticker(11539,52114111)
        send_text_message_reply(reply_token,"Mochi is sorry that you are feeling down T-T, here is a hug from Mochi!\n\nSadness is a difficult emotion to deal with, and it can get overwhelming and make us feel like we're trapped alone in the darkness...")
        send_text_message_push("I am here for you, let me recommend some activities that might help!")
        send_quick_reply_two("Positive statement", "Gratitude Meditation")

    def is_positive_statement(self, event):
        text = event.message.text
        return text.lower() == "positive statement"

    def on_enter_positive_statement(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"It can be very difficult to say something positive to yourself when you are feeling sad, but repeating paw-sitive statement can help shift your attention away from negative feelings, and help you feel more in control")
        send_text_message_push("Take a moment to think of a positive statement that will help you deal with your sadness\n\nIt can be your positive qualities or the idea of things getting better\n\nLike:\n\nI am strong... I am doing the best I can...I will feel okay again...\n\nYou can say it out loud or think aloud in your head, meow~")
        send_text_message_push("Do you feel better afterwards, or would you like to try another activity?")
        send_quick_reply_two("yes","no")

    def is_gratitude_meditation(self, event):
        text = event.message.text
        return text.lower() == "gratitude meditation"        

    def on_enter_gratitude_meditation(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"Have you heard that gratitude is an antidote to sadness? Gratitude can shift your attention from negatives to paw-sitives. Thinking of the smallest things that you are grateful for can fill you with hope and positivity")
        send_text_message_push("Mochi has an online video to help, find a comfortable, quiet spot and follow the instruction in the clip\n\nhttps://www.youtube.com/watch?v=4P2SCgwXVxc")
        send_text_message_push("I hope you feel a bit better after the activity. Would you like to try another activity?")
        send_quick_reply_two("yes","no")

    def is_yes_sad(self, event): #try another activity
        text = event.message.text
        return text.lower() == "yes"

    def is_no_sad(self, event):
        text = event.message.text
        return text.lower() == "no"

    def is_worried(self, event):
        text = event.message.text
        return text.lower() == "worried"

    def on_enter_worried(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"I am sorry you are feeling worried... sometimes a lot of things can happen that are out of control, and we feel helpless because of it")
        send_text_message_push("Mochi has a few activities to help you ease your worry, which one do you want to try?")
        send_quick_reply_two("set time for worry","guided imagery")

    def is_worry_time(self,event):
        text = event.message.text
        return text.lower() == "set time for worry"

    def on_enter_worry_time(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"I know it seems conterproductive, but research shows that scheduling a time to worry can help you feel better in the moment\n\nWorrying about what's going to happen in the future distracts you from focusing on what you need to do\n\nBy postponing your worry to a later time, you can refocus on the present moment")
        send_text_message_push("Write down whatever is worrying you, and pick a later time in the day for you to worry\n\nTell yourslef that you will only worry about what's on your mind at the scheduled time\n\nNow, spend a few minutes breathing in and out, relaxing yourself. Try to focus on the present moment.\n\nWhen your scheduled worry time arrives, you can worry as much as you'd like, but give yourself a time limit so that you don't get overwhelmed")
        send_text_message_push("I hope this activity will help you, you can do this activity daily to ease your worry. Do you want to try another activity?")
        send_quick_reply_two("yes","no")

    def is_guided_imagery(self,event):
        text = event.message.text
        return text.lower() == "set time for worry"

    def on_enter_guided_imagery(self,event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"Do you know, we can use the power of imagination to fight worry. It is a technique called Guided Imagery. It involves utiliising all you senses to picture a calm, happy place. Visualizing this place can shift your attention away from your worries, and help you feel more relaxed")
        send_text_message_push("I have a YouTube video recommendation for you, but you can look up other Guided Imagery video as well!\n\nhttps://www.youtube.com/watch?v=kQM5orholtk")
        send_text_message_push("I hope the video helps you, would you like to try another activity?")
        send_quick_reply_two("yes","no")

    def is_yes_worried(self, event): #try another activity
        text = event.message.text
        return text.lower() == "yes"

    def is_no_worried(self, event):
        text = event.message.text
        return text.lower() == "no"

    def is_stressed(self, event):
        text = event.message.text
        return text.lower() == "stressed"

    def on_enter_stressed(self, event):
        reply_token = event.reply_token
        send_line_sticker(789, 10883)
        send_text_message_reply(reply_token, "I am sorry to hear that you are stressed...Life is full of challenges and sometimes it can get a little too much! Stress can make us feel nervous, unfocused, forgetful and frustrated")
        send_text_message_push("I have a few activites for you to try to relieve the stress:")
        send_quick_reply_two("muscle relaxation","grounded meditation")

    def is_muscle_relaxation(self, event):
        text = event.message.text
        return text.lower() == "muscle relaxation"

    def on_enter_muscle_relaxation(self,event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"A great way to rid stress is by relaxing different muscles in your body.\n\nWhen something is stressing you out, your heart tends to beat faster, and raise your level of cortisol (stress level).\n\n This activity can help to bring your heart rate to normal and reduce cortisol levels")
        send_text_message_push("Here is a YouTube video for muscle relaxation, but you can find other videos as well!\n\nSit in a quiet, comfortable place and listen and follow along!\n\nhttps://www.youtube.com/watch?v=utGa6rqzs3g")
        send_text_message_push("Meow~ do you feel your body more relaxed? Do you want to try another activity?")
        send_quick_reply_two("yes","no")

    def is_grounded_meditation(self, event):
        text = event.message.text
        return text.lower() == "grounded meditation"  

    def on_enter_grounded_meditation(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"This is a type of meditation where you use all your sense to ground yourself.\n\nGrounding helps you focus on the present moment and on what is happening around you, stopping you from overthinking!\n\n")
        send_text_message_push("Let's try to do this! Find a quiet, comfortable place and try to follow along this YouTube video! You are always welcome to find another video~\n\nhttps://www.youtube.com/watch?v=AFBjjsVV9QY")
        send_text_message_push("Nya~ hope that video helps! Would you like to try another activity?")
        send_quick_reply_two("yes","no")

    def is_yes_stressed(self, event): #try another activity
        text = event.message.text
        return text.lower() == "yes"

    def is_no_stressed(self, event):
        text = event.message.text
        return text.lower() == "no"
    
    def is_angry(self, event):
        text = event.message.text
        return text.lower() == "angry"

    def on_enter_angry(self, event):
        send_line_sticker(11537,52002767)
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"Thank you for sharing this with me, I am sure it isn't easy to acknowledge you are angry.\n\nAnger can be difficult to manage at times, and sometimes it can make people lose their cool")
        send_text_message_push("Don't worry, I am here for you! Let's try to do an activity to cool you off, meow~")
        send_quick_reply_two("cleaning up","counting backwards")

    def is_cleaning_up(self, event):
        text = event.message.text
        return text.lower() == "cleaning up"

    def on_enter_cleaning_up(self,event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token,"I know this activity sound a little weird for managing anger...but cleaning works as a great distraction from what's making you angry!\n\nIt does take up time and effort, but it can give you a sense of control over your environment. It also reduces the amount of clutter around you, which helps to lower your stress and anger levels. And it's productive!")
        send_text_message_push("Pick a focus area or object for your cleaning. Set aside the next 5 to 15 minutes to clean, and channel your anger to clean your surroundings and make things neat and organized.\n\nImagine that while you declutter your surroundings , you are also decluttering your mind. Try to be engaged in this activity as much as possible!")
        send_text_message_push("Well I hope you are able to declutter your mind and have a clean room! Do you want to try another activity?")
        send_quick_reply_two("yes","no")
    
    def is_counting_backward(self, event):
        text = event.message.text
        return text.lower() == "counting backward"

    def on_enter_counting_backward(self, event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token, "Nya, I know it sounds weird, but studies has shown counting backwards can help us to prevent anger taking over our thoughts, which may lead to acting on impulse!\n\n Instead of reacting impulsive out of anger, counting backwards can give you a moment to cool down")
        send_text_message_push("This works best when the task of counting is challenging enough to occupy your mind\n\nInstead of counting 10 to 1, starting from 100 might do the trick\n\nStart by taking a few deep breaths, and slowly begin to count backwards from 100")
        send_text_message_push("I hope that helps! Do you want to try another activity?")
        send_quick_reply_two("yes","no")

    def is_yes_angry(self, event): #try another activity
        text = event.message.text
        return text.lower() == "yes"

    def is_no_angry(self, event):
        text = event.message.text
        return text.lower() == "no"

    def on_enter_end(self,event):
        reply_token = event.reply_token
        send_text_message_reply(reply_token, "Nya~ I hope our session helps you! If you are still feeling down, just type in 'hi mochi' and I will there to talk with you!")
        send_line_sticker(11539,52114128)
    

