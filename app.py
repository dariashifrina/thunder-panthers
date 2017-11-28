import urllib2, requests
import json, urllib2
from flask import Flask, render_template
from util import translate
import datamuse
#import requests


app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

#-------------------------------TRANSLATIONS-----------------------------------------

@app.route('/comic')
def comic():
	norm_phrases = ["Spider-Man went to the store to buy eggs and milk.", "Mr Brown was also at the store because he was buying a computer.", "He saw Spider-Man and was surprised.", "Then they both left the store."]
	silly_phrases = ["", "", "", ""]
	for i in range(4):
		silly_phrase = [datamuse.new_sent(norm_phrases[i]), "en"]
		for j in range(20):
			silly_phrase = translate.translate(silly_phrase)
		silly_phrases[i] = datamuse.new_sent(translate.to_english(silly_phrase)[0])
	return render_template("comic.html", norm_phrase1 = norm_phrases[0], norm_phrase2 = norm_phrases[1], norm_phrase3 = norm_phrases[2], norm_phrase4 = norm_phrases[3], silly_phrase1 = silly_phrases[0], silly_phrase2 = silly_phrases[1], silly_phrase3 = silly_phrases[2], silly_phrase4 = silly_phrases[3])

# #-------------------------------GETTY------------------------------------------------


sentence = "Jawad plays hockey at batter park."
phrase = datamuse.img_text(sentence)

getty_key="q7pua4pkzwvj26yakgvnaxvj"
getty_secret_key="SUmeJueqYaAWVuCFQkCypEepBaUMw4E35j2jB3gGsWayy"

headers = { 'Api-Key': 'q7pua4pkzwvj26yakgvnaxvj'}
params = {'phrase': phrase}
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


@app.route('/getty')
def getty():
	return render_template('getty.html', sentence=sentence, phrase=phrase, ret=ret)
#

if __name__ == "__main__":
    app.debug = True
    app.run()
