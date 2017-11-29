import urllib2, requests
import json, urllib2
from flask import Flask, render_template, request, redirect
from util import translate, feed_help
import datamuse
#import requests


app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/editfeed")
def editfeed():
        r = request.args
        if "title" in r and "name" in r:
                print "yay"
                feed_help.add_entry(  r["title"], r["name"], r["pic1"], r["pic2"], r["pic3"], r["pic4"], r["phrase1"], r["phrase2"], r["phrase3"], r["phrase4"])
        else:
                print "nay"
        return redirect("/feed")

@app.route("/feed")
def feed():
        comicdict = feed_help.get_dict()
        return render_template("feed.html", comics = comicdict)

#-------------------------------TRANSLATIONS-----------------------------------------

@app.route('/comic')
def comic():
	norm_phrases = ["Spider-Man went to the store to buy eggs and milk.", "Mr Brown was also at the store because he was buying a computer.", "He saw Spider-Man and was surprised.", "Then they both left the store."]
	silly_phrases = ["", "", "", ""]
	for i in range(4):
		while True:
			try:
				silly_phrase = [datamuse.new_sent(norm_phrases[i]), "en"]
				for j in range(3):
					silly_phrase = translate.translate(silly_phrase)
				silly_phrases[i] = datamuse.new_sent(translate.to_english(silly_phrase)[0])
				break
			except IndexError:
				pass
	return render_template("comic.html", norm_phrase1 = norm_phrases[0], norm_phrase2 = norm_phrases[1], norm_phrase3 = norm_phrases[2], norm_phrase4 = norm_phrases[3], silly_phrase1 = silly_phrases[0], silly_phrase2 = silly_phrases[1], silly_phrase3 = silly_phrases[2], silly_phrase4 = silly_phrases[3], norm_url1 = img_url(norm_phrases[0])['uri'], norm_url2 = img_url(norm_phrases[1])['uri'], norm_url3 = img_url(norm_phrases[2])['uri'], norm_url4 = img_url(norm_phrases[3])['uri'], silly_url1 = img_url(silly_phrases[0]), silly_url2 = img_url(silly_phrases[1]), silly_url3 = img_url(silly_phrases[2]), silly_url4 = img_url(silly_phrases[3]) )
# #-------------------------------GETTY------------------------------------------------

sentence = "Jawad plays hockey at batter park."

def img_url(sentence):

	phrase = datamuse.img_text(sentence)

	getty_key="q7pua4pkzwvj26yakgvnaxvj"
	getty_secret_key="SUmeJueqYaAWVuCFQkCypEepBaUMw4E35j2jB3gGsWayy"

	headers = { 'Api-Key': 'q7pua4pkzwvj26yakgvnaxvj'}
	params = {'phrase': phrase}
	url = 'https://api.gettyimages.com/v3/search/images'
	resp= requests.get(url, headers=headers, params=params)
	result = resp.json()
	d = {}
	ret = []
	if result['images'] != []:
		inner_dict = result['images'][0]['display_sizes'][0]
		d['uri'] = inner_dict['uri']
	else:
		d['uri'] = "https://i.ytimg.com/vi/K4zm30yeHHE/maxresdefault.jpg"


	return d


@app.route('/getty')
def getty():
	return render_template('getty.html', sentence=sentence, ret= img_url(sentence))
#

if __name__ == "__main__":
    app.debug = True
    app.run()
