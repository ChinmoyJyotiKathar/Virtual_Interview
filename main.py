#!/usr/bin/env python3                                                                                
                                                                                                      
import speech_recognition as sr
from os import system 
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import random
import time

#custom sentiment analyzer
sentimentAnalyzer = {'don\'t' : 'terrible',
 'have' : 'good',
 'do' : 'wonderful',
 'not' : 'terrible',
 'never': 'terrible',
 'little': 'terrible',
 'can\'t' : 'terrible',
 'do not' : 'terrible',
 'weakness': 'bad',
 'weak': 'terrible',
 'done': 'good',
 'not done' : 'terrible',
 'worked': 'good',
 'work' : 'good',
 'helped' : 'good',
 'help': 'good',
 'learn': 'good',
 'learned':'good',
 'strength': 'good',
 'strengths': 'good',
 'know': 'good',
 'did' : 'good',
 'did not': 'terrible',
 'not do': 'terrible',
 'less': 'terrible'}

#list_of_keywords
keywords = ['python', 'c plus plus', 'c', 'competetive programming']



#list of default questions
defaultQuestions = [', Can you atleast tell me one important project you have done?',
 ', I assume you atleast know about OOP. What do you think about object oriented programming?',
 ', I shall ask you computer architecture. Can you explain how memory is managed inside a modern computer?']



take_input = True

def voice_out(questionData):
	system('say %s' % (questionData))
	return


def ask_topic(topic):
	if topic == 'python':
		return ' Can you tell me how to define a class in python'
	if topic == 'c':
		return ' Please tell me how you will merge two linked lists in c'
	if topic == 'c plus plus':
		return ' Since you say you know c + + , can you tell me the difference between enscapsulation and inheritence of data?'



def reverseSentiment(word):
	return ('not '+ word)



def checkSentiment(string):
	#code to check if sentence is positive or negative
	

	mysent = string
	#print(mysent + 'is here')
	newsent = ""
	wordList = mysent.split(' ')
	prev_word = wordList[0]
	for word in wordList:
		if word in sentimentAnalyzer.keys() and prev_word == 'not': #negation
			#newsent = newsent + " " + (sentimentAnalyzer[reverseSentiment(word)])
			continue
		elif word in sentimentAnalyzer.keys():
			newsent = newsent + " " + (sentimentAnalyzer[(word)])
		else:
			newsent = newsent + " " + word
		prev_word = word
	print(newsent)
	testimonial = TextBlob(newsent)
	if testimonial.sentiment[0] < 0:
		print('negative sentiment')
		return 'neg'
	else:
		print('positive sentiment')
		return 'pos'





def returnSynonyms(word):
	#code  to return synonyms
	return

def checkKeywords(string):
	#check and return important keywords
	return


def process_input(user_input):

	for sentence in user_input:
	
		#keywords = ['python', 'c', 'c plus plus', 'competetive programming']
		gotWord = 'any programming language'
		for word in sentence.split(' '):
			if word.lower() in keywords:
				gotWord = word
				shouldask = checkSentiment(sentence)
				if shouldask == 'pos':
					#return ('okay, can you please tell me  something about ' + word)
					return(ask_topic(word.lower()))
	return ('Since you say you are not very good in '+ gotWord + ' ' +random.choice(defaultQuestions))


#Get small quantum packets of input which we will treat as small sentences
def getQuantumInput():
	r = sr.Recognizer()  
	r.pause_threshold = 0.2
	r.phrase_threshold = 0.1
	r.non_speaking_duration = 0.1                                                                              
	with sr.Microphone() as source:
		try:
			audio = r.listen(source, timeout = 2)
			return audio
		except sr.WaitTimeoutError:
			print("Timed out")
			return None



# get audio from the microphone
def get_input(questionData):                                                                       
	r = sr.Recognizer()
	InputList = []
	print(questionData)
	voice_out(questionData)
	while(True):
		quantumInput = getQuantumInput() #call this for getting small sentences
		if (quantumInput == None): #if more than 5 sec pause in candidate answer then end answer
			print("Processing...")
			return InputList
		InputList.append(quantumInput)
		


def getTextInput(questionData):
	r = sr.Recognizer()
	TextList = []
	AudioList = []
	AudioList = get_input(questionData)
	#print("Got all audio inputs")
	print(AudioList)
	for recordedAudio in AudioList:
		TextSnippet = r.recognize_google(recordedAudio)
		print("-" , TextSnippet)
		TextList.append(TextSnippet)
	#print(TextList)
	return TextList



proposedQuestion = "Hi, I am Louis, your virtual questioner. So tell me about yourself!"
questionData = proposedQuestion
while(take_input): 
	try:
		questionData = proposedQuestion
		user_input =  getTextInput(questionData)
		print(user_input)
		proposedQuestion = process_input(user_input)
		#system(user_input)
    	#user_input = r.recognize_google(audio)
    	#process_input(user_input)

	except sr.UnknownValueError:
		print("Could not understand audio")

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

		