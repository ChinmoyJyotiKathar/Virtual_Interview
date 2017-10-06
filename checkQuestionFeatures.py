import os
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import  GaussianNB
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import nps_chat
import numpy as np
from nltk.data import load
from nltk.corpus import stopwords



posts = nltk.corpus.nps_chat.xml_posts()
label_names = np.array(sorted(nltk.FreqDist(p.attrib['class'] for p in posts).keys()))


chatroom = nps_chat.xml_posts()

features = []
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
for item in chatroom:
    text = nltk.word_tokenize(item.text)
    sent = (list(nltk.pos_tag(text)))
    if item.get('class') == 'whQuestion' or item.get('class') == 'ynQuestion':
        for x in sent:
            if x not in stop_words:
                features.append(x)
features = nltk.FreqDist(features)
print (features.most_common(15))
