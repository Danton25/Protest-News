import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
import pickle
import htmldate
import time
import codecs


#Loads a json file into a list
def loadJSON(filename):
	with open(filename, encoding='utf-8')  as f:
		data = json.load(f)
		print(len(data))
		print(data[0])
	return data

#Saves data into a json file
def saveJSON(filename, final_data):
	with open(filename, 'w') as f:
    json.dump(final_data, f)

def extractArticlesAndSaveToJSON(filename):
    
    df = pd.read_csv(filename)
    final_data  = []
    index = 0
    for i, link in enumerate(df.iloc[:, 32]):
        response = ''
        tmp = {}
        times = 0
        if (link == link):
            url = link
            while response == '':
                try:
                    times+=1
                    response = requests.get(url, verify=False)
                    break
                except:
                    if (times > 10):
                        break
                    time.sleep(5)
                    continue
            if (times > 10):
                continue
            soup = BeautifulSoup(response.content, 'lxml')
            d1 = htmldate.find_date(url)
            tmp['id'] = index
            index+=1
            tmp['data_id'] = int(df.iloc[i][1])
            #index+=1
            tmp['country'] = df.iloc[i][18]
            tmp['source_url'] = link
            tmp['source_name'] = df.iloc[i][26]
            tmp['published_date'] = d1
            headline = ''
            if (soup.find('h1') != None):
                headline = soup.find('h1').get_text()
            tmp['headline'] = headline
            links = [e.get_text() for e in soup.find_all('p')]
            article = '\n'.join(links)
            tmp['content'] = article
            #print(tmp['content'])
            print(index-1, tmp['data_id'])
            # print(len(article))
            final_data.append(tmp)
            #i+=1
    return final_data


#Saving data so we can reload later without running the code again
# with open('obj.pkl', 'ab') as f:
#      pickle.dump(data, f)
# with open('obj.pkl', 'rb') as f:
#     data1 = pickle.load(f)

final_data = extractArticlesAndSaveToJSON('Miners.csv')
print(len(final_data))
with open('Miners123.json', 'w') as f:
    json.dump(final_data, f)

# print('Here')