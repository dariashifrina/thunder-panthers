from flask import Flask, render_template
import urllib2
import json

#creates the list of languages translator supports
def get_langs():
    uResp = urllib2.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20171114T234337Z.0a446decad58ac47.3d65b0d73d70831cbeb0a6591eede45906e8bac8&text=' + text + '&lang=');
	data = uResp.read()
	d = json.loads(data)
    return d

#sets a variable to the list of languages
langs = get_langs()


#returns a random language
def rand_lang():
    return langs[rand()]

#Takes a tuple of size two with the first element being the text and the second being the language it is in.
def translate(text):
    uResp = urllib2.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20171114T234337Z.0a446decad58ac47.3d65b0d73d70831cbeb0a6591eede45906e8bac8&text=' + text[0] + '&lang=' + text[1] + '-' + rand_lang());
	data = uResp.read()
	d = json.loads(data)
	print d
	lang = d["lang"]
	text = d["text"]
	return (text, lang)
