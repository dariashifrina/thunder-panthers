'''
Karina Ionkina
SoftDev1 pd07
K#13: A RESTful Journey Skyward
2017-11-09
'''

import urllib2
import json
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


#------ HTTP Error 403: Forbidden Error ---------------------------------------------------------------------------
# "Bots may not be used to retreive bulk content for any use directly related to an approved bot task.
# This includes dynamically loading pages from another website, which may result in the website being 
# denied access. 
'''
phrase = "kitties"
resp = urllib2.urlopen("https://api.gettyimages.com/v3/search/images?Api-Key=" + getty_key+"phrase=" +phrase)
result = resp.read()
'''
#-------------------------------------------------------------------------------------------------

# SO I used requests instead
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



"""
----------- playin with planetary sounds API ----------------------------------------
uResp = urllib2.urlopen("https://api.nasa.gov/planetary/sounds?q=apollo&api_key=" + api_key)

uResp = uResp.read()
#print uResp

d = json.loads(uResp)

#print d["results"]

for dictionary in d["results"]:
    for key in dictionary:
        print str(key) + " ------ " + str(dictionary[key])
    print "-----------------------------------------------------------------------------------"
"""


