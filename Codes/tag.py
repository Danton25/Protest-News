import json
import pickle
import nltk
import spacy
nltk.download('punkt')
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


st = StanfordNERTagger('/Users/nikhilyadav/Documents/Sem2/Projects/IR Project/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/nikhilyadav/Documents/Sem2/Projects/IR Project/stanford-ner-2018-10-16/stanford-ner.jar',encoding='utf-8')
nlp = spacy.load('en_core_web_lg')
  
    
def get_info(s):
    
    # event type field
    print("inside getinfo")
    p = nlp("protest")
    doc = nlp(s.lower())
    m = 0.5
    a = p

    for i in doc:
        s = i.similarity(p)
        if s>m:
            a = i
            m = s

    event = a
    if event != "protest":
        event += " protest"
    sim_score = m

    #loction and actor field
    tokenized_text = word_tokenize(s)
    classified_text = st.tag(tokenized_text)
    loc = ""
    c_loc = 0
    actor = []
    for i in classified_text:
        if i[1]=="LOCATION" and c_loc==0:
            loc = i[0]
            c_loc += 1
        elif i[1] == "PERSON" or i[1] == "ORGANIZATION":
            actor.append(i[0])


    return loc, actor, event



def loadJSON(filename):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
        print("inside loadJson")
        print(len(data))
        print(data[0])
    return data




def mymain():
    out = []
    print("inside last mymain")
    data = loadJSON('project3_train.json')
    for i in data:
        d = {}
        d["data_id"] = i["data_id"]
        d["event_date"] = i["published_date"]
        d["data_source"] = d["source_name"]
        d["location"], d["actor_involved"], d["event_type"] = get_info(i["content"])
        if d["location"] == "":
            d["location"] = i["country"]
        else:
            d["location"] = d["location"]+", "+i["country"]
        out.append(d)
    
    print(len(out))

    with open('TASK1.json', 'w') as f:
        print("inside last line")
        json.dump(out,f, indent = 2)

