import os
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import  GaussianNB
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import nps_chat
import numpy as np
from nltk.data import load
import pickle


#To use this add this file, features_text.pickle, GaussianNaiveBayes.pickle
#The test sentence put mysentence

classifier_f = open("features_text.pickle","rb")

features_text = pickle.load(classifier_f)
classifier_f.close()


classifier_f = open("GaussianNaiveBayes.pickle","rb")

gnb = pickle.load(classifier_f)
classifier_f.close()


# save the classifier
#with open('GaussianNaiveBayes.pkl', 'wb') as fid:
#    cPickle.dump(gnb, fid)

# load it again
#with open('GaussianNaiveBayes.pkl', 'rb') as fid:
#    gnb_loaded = cPickle.load(fid)
#    gnb = gnb_loaded




#from here copy and paste into your program:
mysentence = "Chinmoy how are we doing today?"
mysentfeatures = [0,0,0,0,0,0,0,0]
text = nltk.word_tokenize(mysentence)
sent = (list(nltk.pos_tag(text)))
print(sent)
x=0
for i in range(len(sent)):
    #print(sent[i][1])
    try:
        #features[x][features_text.index(sent[i][1])] = 1
        value = sent[i][1]
        if value in ['JJ', 'JJR','JJS']:
            mysentfeatures[features_text.index('J')] += 1
        elif value in ['NN', 'NNP','NNS']:
            mysentfeatures[features_text.index('N')] += 1
        elif value in ['RB', 'RBR','RBS']:
            mysentfeatures[features_text.index('R')] += 1
        elif value in ['VB', 'VBD','VBG','VBN','VBP','VBZ']:
            mysentfeatures[features_text.index('V')] += 1
        elif value in ['WP', 'WRB']:
            mysentfeatures[features_text.index('W')] += 1
        elif value in ['CC', 'LS']:
            mysentfeatures[features_text.index('X')] += 1
        else:
            mysentfeatures[features_text.index('A')] += 1
    except ValueError:
        #features[x].append(len(features_text)-1)
        mysentfeatures[len(features_text)-1] += 1

print("here-->",mysentfeatures)
mysentfeatures = np.array(mysentfeatures)
mysentfeatures = mysentfeatures.reshape(1, -1)

test = mysentfeatures
test_labels = np.array([1])
print(test_labels)
print ("this--> ", test)
preds = gnb.predict(test)

if 1 in list(preds):
    print('Question')
else:
    print(statement)
