#A. Interaction of User for asking the name
print("BOT: What is your name ?")
uname = input()
print("\nBOT: Heyy there {0} ! How may I help you\n".format(uname))


#B. Responses of ChatBot
name, work, weather, mood = "Bot_101", "i am a chatbot and i love talking to people", "sunny", "delighted"

resp={
	"what\'s your name?": ["they call me {0} and i\'m very {1} to meet you".format(name, mood), "i usually go by the name {0} but {1}\nalso.. {2} to meet you !!".format(name, work, mood), "i\'m {0} and {1}".format(name, work)],
	
	"how\'s the weather today?":["the weather is quite {0}".format(weather), "it\'s {0} today, isn\'t it ?".format(weather)],
	
	"how are you feeling today?": ["well.. {0},\nit\'s a bright {1} day and i\'m very {2} to meet people, especially you {3}!!".format(work, weather, mood, uname), "Very {0}, thank you ! and you ?".format(mood)],
	
	"hey ! are you there ?": ["..\n...\ni\'ll be there for you..\n when the rain starts to pour", "sorry.. been in a fight with the network today", "...\n...reconnecting..\nwhat did i miss?", "{0} disconnected the call".format(name) ],
	
	"default":"Hi.. this is {0}.\nnice to meet you.\n this is a default message to check my vitals".format(name) }
	
#C. Creating a function response

import random

def res(message):
	if message in resp:
		bot_101_msg = random.choice(resp[message])
	else:
		bot_101_msg = random.choice(resp["default"])
	return bot_101_msg
	
#D. Another Function
def real(xtext):
	if "name" in xtext:
		ytext = "what\'s your name?"
	elif "sunny" in xtext:
		ytext = "how\'s the weather today?"
	elif "how are" in xtext:
		ytext = "how are you feeling today?"
	else:
		ytext= "default"
	return ytext
	
#E. Sending back the message function
def send_message(message):
	//print((message))
	response = res(message)
	print((response))
	
#F. Final Step to break the loop
while 1:
	my_input = input()
	my_input = my_input.lower()
	related_text = real(my_input)
	send_message(related_text)
	if my_input == "exit" or my_input =="stop":
		print("nice to meet you {0}, see you again !!\nwell wishes{1}".format(uname, name))
		break
	
	





























