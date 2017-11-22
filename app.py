import urllib2
import json, urllib2
from flask import Flask, render_template
import requests

nasa_api_key= "4Gh1MmyY5cA9nGRSD9sf5RLAHZAJNQLrGr1suKnz"
uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key="+ nasa_api_key)
temp = uResp.read()
data = json.loads(temp)
#print data                                                                                       

img_url= data['hdurl']
#print img_url                                                                                    

exp= data['explanation']
#print exp                                                                                        
app = Flask(__name__)
 
getty_key="q7pua4pkzwvj26yakgvnaxvj"
getty_secret_key="SUmeJueqYaAWVuCFQkCypEepBaUMw4E35j2jB3gGsWayy"

headers = { 'Api-Key': 'q7pua4pkzwvj26yakgvnaxvj'}
params = {'phrase': 'kitties'}
url = 'https://api.gettyimages.com/v3/search/images'
resp= requests.get(url, headers=headers, params=params)
result = resp.json()


ret=[]
for i in range(10):
    d = {}
    d['title'] = result['images'][i]['title']
    inner_dict = result['images'][i]['display_sizes'][0]
    d['uri'] = inner_dict['uri']
    d['caption']= result['images'][i]['caption']
    ret.append(d)

#print ret         

@app.route('/')
def foo():
    return render_template('home.html', img_url = img_url, exp = exp)

@app.route('/getty')
def getty():
    return render_template('boo.html', ret=ret)


if __name__ == "__main__":
    app.debug = True
    app.run()


#-------------------------------GETTY------------------------------------------------


headers = {
    'X-Mashape-Key': 'oBpmpSyPPTmshB9sUnA73mmjlZONp1Z8QQVjsnmNIErswbciPD',
    'Accept': 'application/json',
}

boop = requests.get('https://wordsapiv1.p.mashape.com/words/bump/also', headers=headers)
word_result = boop.json()




