import urllib2
import json, urllib2
from flask import Flask, render_template
from util import translate
#import requests


app = Flask(__name__)

#-------------------------------TRANSLATIONS-----------------------------------------
@app.route('/comic')
def comic():
	norm_phrases = ["We found them. What do you mean?", "What a strange person. Burn her anyway!", "Well, we did do the nose.", "You can't expect to wield supreme power just 'cause some watery tart threw a sword at you!"]
	silly_phrases = ["", "", "", ""]
	for i in range(4):
		silly_phrase = [norm_phrases[i], "en"]
		for j in range(15):
			silly_phrase = translate.translate(silly_phrase)
		silly_phrases[i] = silly_phrase[0]
	return render_template("comic.html", norm_phrase1 = norm_phrases[0], norm_phrase2 = norm_phrases[1], norm_phrase3 = norm_phrases[2], norm_phrase4 = norm_phrases[3], silly_phrase1 = silly_phrases[0], silly_phrase2 = silly_phrases[1], silly_phrase3 = silly_phrases[2], silly_phrase4 = silly_phrases[3])

# #-------------------------------GETTY------------------------------------------------
# getty_key="q7pua4pkzwvj26yakgvnaxvj"
# getty_secret_key="SUmeJueqYaAWVuCFQkCypEepBaUMw4E35j2jB3gGsWayy"
#
# headers = { 'Api-Key': 'q7pua4pkzwvj26yakgvnaxvj'}
# params = {'phrase': 'kitties'}
# url = 'https://api.gettyimages.com/v3/search/images'
# resp= requests.get(url, headers=headers, params=params)
# result = resp.json()
#
#
# ret=[]
# for i in range(10):
#     d = {}
#     d['title'] = result['images'][i]['title']
#     inner_dict = result['images'][i]['display_sizes'][0]
#     d['uri'] = inner_dict['uri']
#     d['caption']= result['images'][i]['caption']
#     ret.append(d)
#
# #print ret
#
# @app.route('/')
# def getty():
#     return render_template('index.html', ret=ret)
#

if __name__ == "__main__":
    app.debug = True
    app.run()
