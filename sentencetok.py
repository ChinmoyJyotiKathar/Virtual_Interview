import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
data = 'hi my name is chinmoy i\'m good at python though not very good at c you can ask me any question in python. Do you know who i am?' 
print ('\n-----\n'.join(tokenizer.tokenize(data)))