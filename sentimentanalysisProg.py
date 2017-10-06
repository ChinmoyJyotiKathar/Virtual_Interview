import nltk
import random #to shuffle up data so that no bias
from nltk.corpus import movie_reviews #contains 2000 +ve and -ve reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#list out all words document-wise and add the category also in a list of tupple
#documents = []
#for category in movie_reviews.categories():
#	for fileid in movie_reviews.fileids(category):
#		documents.append((list(movie_reviews.words(fileid)),category))


#random.shuffle(documents)

#print(documents[1])


short_pos = open("mypos.txt","r").read()
short_neg = open("myneg.txt","r").read()

documents = []
for r in short_pos.split('\n'):
	documents.append((r,'pos'))
for r in short_neg.split('\n'):
	documents.append((r,'neg'))

random.shuffle(documents)
print(documents[:20])
#print(documents)

all_words= []

short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

#for w in movie_reviews.words():
#	all_words.append(w.lower())

for w in short_pos_words:
	all_words.append(w.lower())
for w in short_neg_words:
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common())
word_features = list(all_words.keys())[:100]
#print(all_words["awesome"])

def findfeatures(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features

#print((findfeatures(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(findfeatures(rev),category) for (rev,category) in documents]

random.shuffle(featuresets)

#myline="mattei's underdeveloped effort here is nothing but a convenient conveyor belt of brooding personalities that parade about as if they were coming back from stock character camp -- a drowsy drama infatuated by its own pretentious self-examination . "

myline = "i know how to do this"
mydoc = []
mydoc.append((list(word_tokenize(myline)),'pos'))
myinputfeatures = [(findfeatures(rev),category) for (rev,category) in mydoc]

training_set = featuresets[:]

#testing_set = featuresets[:500]
testing_set = myinputfeatures[:]
print()
print()
#print(testing_set)
print()
print()
classifier = nltk.NaiveBayesClassifier.train(training_set)
classifier.show_most_informative_features(100)
#classifier_f = open("naivebayes.pickle","rb")

#classifier = pickle.load(classifier_f)
#classifier_f.close()
print("Accuracy: ", (nltk.classify.accuracy(classifier, testing_set))*100)

print("Classification:",classifier.classify(testing_set[0][0]))




#pickling
#save_classifier = open("naivebayes.pickle","wb")
#pickle.dump(classifier,save_classifier)
#save_classifier.close()
