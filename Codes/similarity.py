import spacy
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import nltk
nltk.download('averaged_perceptron_tagger')

nlp = spacy.load('en_core_web_lg')
#print(nlp.vocab['banana'].vector)
stop_words = set(stopwords.words('english')) 

protest = nlp("peaceful")
protestvoc = nlp.vocab['protest']
violence = nlp("violent")
riotsvocab = nlp.vocab['riot']
violencevocab = nlp.vocab['violence']
riots = nlp("riots")
doc = ("Angry")
#animal = nlp.vocab['animal']
#print()
word_tokens = word_tokenize(doc) 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
a = ""
b =""
for w in filtered_sentence:
	a = a + (w) +" "
print (a)
tagged = nltk.pos_tag(word_tokens)
for t in tagged:
	if t[1] == 'VBN' or  t[1] == "VBD" or t[1] == "VB" or t[1] == "RB" or t[1] == "NN" or t[1] == "NNS":
		print(t[1])
		b = b + t[0] + " " 
	else:
		b = b + t[0] + " "
print (b)
print()
doc1 = nlp(b)
#print()
print("Protest   ",protest.similarity(doc1)) # 0.6618534 0.23552845

print("violence     ",violence.similarity(doc1))
print()
#print("riots     ",riots.similarity(doc))
#print()
#print()
#print("vocab")
#print()
print()
print("protestvocab  ",protestvoc.similarity(doc1))
print("riotvocab     ",riotsvocab.similarity(doc1))
print("violencevocab     ",violencevocab.similarity(doc1))
#print(banana.similarity(fruit), banana.similarity(animal)) # 0.67148364 0.2427285