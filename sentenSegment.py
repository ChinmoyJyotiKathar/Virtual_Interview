import spacy

nlp = spacy.load('en')
text  = u''' Hello my name is Chinmay. I have done many projects in the past. I know python'''
tokens = nlp(text, parse = True)

for s in tokens.sents:
	print(s)
	