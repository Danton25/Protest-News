#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:44:51 2020

@author: nikhilyadav
"""

import spacy
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import nltk
import json
from nltk.tag import StanfordNERTagger
nltk.download('averaged_perceptron_tagger')
st = StanfordNERTagger('/Users/nikhilyadav/Documents/Sem2/Projects/IR Project/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/nikhilyadav/Documents/Sem2/Projects/IR Project/stanford-ner-2018-10-16/stanford-ner.jar',encoding='utf-8')
nlp = spacy.load('en_core_web_lg')
#print(nlp.vocab['banana'].vector)


out = []
with open("final_data_test.json", encoding='utf-8') as f:
    data = json.load(f)
    print("inside loadJson")
    print("DATA LE ",len(data))
    #print(data[0])
    z=0


    for i in data:
        d = {}
        z=z+1
        d["data_id"] = i["data_id"]
        #print("         ",i["data_id"])
        #print(i["y_event_type"],"   ")
  
        out.append(d)
        

        stop_words = set(stopwords.words('english')) 
        
        
        doc = (i["content"])
        #animal = nlp.vocab['animal']
        #print()
        s = ""
        word_tokens = word_tokenize(doc) 
        #filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        
        a = []
        b =[]
        
        
        for w in filtered_sentence:
        	#a = a + (w) +" "
            a.append(w)
            s = s + w +" " 
        #print (s)
        
        
        
        word_tokens1 = word_tokenize(s)
        #print(word_tokens1)
        tagged = nltk.pos_tag(word_tokens1)
        
        
        
        verb_tags = ['VBN','VBD','VB','VBG','VBN','VBP','VBZ']
        
        
        c_text = st.tag(word_tokens1)
        loc = []
        count_loc = 0
        loc_index = []
        verb_index = []
        count_verb = 0
        for l in c_text:
            count_loc+=1
            if l[1] == "LOCATION":
                loc.append(l[0])
                loc_index.append(count_loc)
                count_loc+=1
        final_location = ""
        local_count = 0
        for j,t in enumerate(tagged):

            
            if t[1] in verb_tags or t[0] in loc:
                #print("inside for")
                if t[1] in verb_tags :
                    count_verb +=1
                 
                #print("second if")
                if count_verb > local_count and t[0] in loc :
                    #print("third if")
                    local_count = count_verb
                    
                    final_location = t[0]
                    if((j+1)<len(tagged) and tagged[j+1][0] in loc):
                        final_location += " "+tagged[j+1][0] 
                    print (count_verb,"    ", final_location,"     ",j)
                    count_verb = 0
                    
                #print("verb :    ",t[0])
                verb_index.append(count_verb)
                b.append(t[0]) 
                #count_verb+=1
        d["Final Location"] = final_location
        out.append(d)
        
    with open('location_task_test.json', 'w') as f:
        print("inside last line")
        json.dump(out,f,indent = 2)
#print(tagged)

#print(len(c_text),"   ", len(tagged))
#print("Locations    ",loc)
#print("Loc index    ",loc_index)
#print("Verbs        ",b)
#print("verb index   ", verb_index)
#print(final_location)
#print(tagged)

#print(tagged)