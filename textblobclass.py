from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier


mydict = {'don\'t' : 'terrible',
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
 'know': 'good'}

mysent = "i did not terrible any project in python"
print(mysent)
newsent = ""
for word in mysent.split(' '):
	print(word)
	if word in mydict.keys():
		newsent = newsent + " " + mydict[word]
	else:
		newsent = newsent + " " + word

print(newsent)

testimonial = TextBlob(newsent)
if testimonial.sentiment[0] < 0:
	print ("negative")
else:
	print("positive")
#print(testimonial.sentiment)