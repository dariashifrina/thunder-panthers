import json, urllib2, os, requests
from flask import Flask, render_template, request, redirect, flash, url_for
from util import translate, feed_help, datamuse

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/editfeed")
def editfeed():
        r = request.args
        if "title" in r and "name" in r:
                print r["phrase1"]
                feed_help.add_entry(  r["title"], r["name"], r["pic1"], r["pic2"], r["pic3"], r["pic4"], r["phrase1"], r["phrase2"], r["phrase3"], r["phrase4"])
        else:
                print "nay"
        return redirect("/feed")

@app.route("/feed")
def feed():
        comicdict = feed_help.get_dict()
        return render_template("feed.html", comics = comicdict)

#-------------------------------COMIC-----------------------------------------

@app.route('/comic', methods=["POST", "GET"])
def comic():
	if request.method == "GET":
		r = request.args
		print r
	else:
		r = request.form
		print r
	for phrase in ['phrase1', 'phrase2', 'phrase3', 'phrase4']:
		try:
			datamuse.new_sent(r[phrase], r['textRazorApiKey'])
		except IndexError:
			flash('Sentence format incorrect')
			return redirect(url_for('home'))
		if len(r[phrase]) > 150:
			flash('Please limit your sentences to 150 characters')
			return redirect(url_for('home'))
	silliness = int(r['silliness'])
	norm_phrases = [r['phrase1'], r['phrase2'], r['phrase3'], r['phrase4']]
	silly_phrases = ["", "", "", ""]
	for i in range(4):
		while True:
			try:
				silly_phrase = [datamuse.new_sent(norm_phrases[i], r['textRazorApiKey']), "en"]
				for j in range(silliness):
					silly_phrase = translate.translate(silly_phrase, r['yandexTranslateApiKey'])
				if silliness > 3:
					silly_phrases[i] = datamuse.new_sent(translate.to_english(silly_phrase, r['yandexTranslateApiKey'])[0], r['textRazorApiKey']).decode()
				else:
					silly_phrases[i] = translate.to_english(silly_phrase, r['yandexTranslateApiKey'])[0].decode()
				break
			except (UnicodeDecodeError, UnicodeEncodeError, IndexError):
				pass
	print norm_phrases
	print silly_phrases
	return render_template("comic.html", norm_phrase1 = norm_phrases[0], norm_phrase2 = norm_phrases[1], norm_phrase3 = norm_phrases[2], norm_phrase4 = norm_phrases[3], silly_phrase1 = silly_phrases[0], silly_phrase2 = silly_phrases[1], silly_phrase3 = silly_phrases[2], silly_phrase4 = silly_phrases[3], norm_url1 = img_url(norm_phrases[0], r['gettyImagesApiKey'], r['textRazorApiKey']) , norm_url2 = img_url(norm_phrases[1], r['gettyImagesApiKey'], r['textRazorApiKey']) , norm_url3 = img_url(norm_phrases[2], r['gettyImagesApiKey'], r['textRazorApiKey']) , norm_url4 = img_url(norm_phrases[3], r['gettyImagesApiKey'], r['textRazorApiKey']) , silly_url1 = img_url(silly_phrases[0], r['gettyImagesApiKey'], r['textRazorApiKey']), silly_url2 = img_url(silly_phrases[1], r['gettyImagesApiKey'], r['textRazorApiKey']), silly_url3 = img_url(silly_phrases[2], r['gettyImagesApiKey'], r['textRazorApiKey']), silly_url4 = img_url(silly_phrases[3], r['gettyImagesApiKey'], r['textRazorApiKey']) )
# #-------------------------------GETTY------------------------------------------------



def img_url(sentence, getty_key, text_razor_key):
	print "the sentence is: " + sentence

	phrase = datamuse.img_text(sentence, text_razor_key)
	print "the phrase is: " + phrase

	headers = { 'Api-Key': getty_key}
	params = {'phrase': phrase}
	url = 'https://api.gettyimages.com/v3/search/images'
	resp= requests.get(url, headers=headers, params=params)
	result = resp.json()

	d = {}
	ret = []
	if result['images'] != []:
		inner_dict = result['images'][0]['display_sizes'][0]
		d = inner_dict['uri']
	else:
		d = "http://newparent.com/wp-content/uploads/2008/10/surprised-baby.jpg"
	return d

if __name__ == "__main__":
    app.debug = True
    app.run()
