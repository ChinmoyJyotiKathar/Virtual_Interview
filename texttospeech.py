from os import system
import speech_recognition as sr
import time
import multiprocessing

listofaudio = []

def voice_out(questionData):
	system('say %s' % (questionData))
	return


def get_input(questionData):
	#print("I'm here")                                                                       
	r = sr.Recognizer()  
	r.pause_threshold = 0.2
	r.phrase_threshold = 0.1
	r.non_speaking_duration = 0.1                                                                             
	with sr.Microphone() as source:
		#print(questionData)
		#voice_out(questionData)
		#print("Acces?")
		try:
			audio = r.listen(source, timeout = 1)
			return audio
		except sr.WaitTimeoutError:
			return None
		#listofaudio.append(audio)
		#print("About to return")
		
		#user_input = r.recognize_google(audio)
		#return user_input

while(1):
	
	#p = multiprocessing.Process(target=get_input, name="Foo", args=('Please Speak',listofaudio))
	#user_input = r.recognize_google(p.start())
	#user_input = r.recognize_google(get_input("Please speak"))
	#print("back to bedlum")
	myanswer = get_input("Please Speak Now")
	if(myanswer != None):
		listofaudio.append(myanswer)
		#print(listofaudio)
	else:
		for i in listofaudio:
			r = sr.Recognizer()
			print(r.recognize_google(i))
	#time.sleep(3)
	#if p.is_alive():
	#	print("foo is running... let's kill it...")
	#	p.terminate()
	#p.join()
