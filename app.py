import urllib2
import json, urllib2
from flask import Flask, render_template
import requests


app = Flask(__name__)
 
#-------------------------------GETTY------------------------------------------------
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
def getty():
    return render_template('boo.html', ret=ret)


if __name__ == "__main__":
    app.debug = True
    app.run()










