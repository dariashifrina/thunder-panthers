from flask import Flask, render_template
import urllib, urllib2
import json
import random

key = "translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20171114T234337Z.0a446decad58ac47.3d65b0d73d70831cbeb0a6591eede45906e8bac8"

#sets a variable to the list of languages
langs = ["az", "sq", "en", "ar", "hy", "af", "eu", "ba", "be", "bn", "my", "bg", "bs", "cy", "hu", "vi", "ht", "gl", "nl", "mrj", "el", "ka", "gu", "da", "he", "yi", "id", "ga", "it", "is", "es", "kk", "kn", "ca", "ky", "zh", "ko", "xh", "km", "la", "lv", "lt", "lb", "mg", "ms", "ml", "mt", "mk", "mi", "mhr", "mn", "de", "ne", "no", "pa", "pap", "fa", "pl", "pt", "ro", "ru", "ceb", "sr", "si", "sk", "sl", "sw", "su", "tg", "th", "tl", "ta", "tt", "te", "tr", "udm", "uz", "uk", "ur", "fi", "fr", "hi", "hr", "cs", "sv", "gd", "et", "eo", "jv", "ja"]

#returns a random language
def rand_lang():
	return langs[random.randint(0, len(langs)-1)]

#takes a list of size two with the first element being the text and the second being the language it is in.
def translate(text):
	print "text[0]: " + text[0]
	print "text[1]: " + text[1]
	cmd = "https://" + key + '&text=' + urllib.quote(text[0]) + '&lang=' + urllib.quote(text[1]) + '-' + urllib.quote(rand_lang())
	print " " + cmd + " "
	uResp = urllib2.urlopen(cmd)
	data = uResp.read()
	d = json.loads(data)
	print d
	if d["code"] != 200:
		print "API error code" + d["code"]
		return text
	lang = d["lang"].split("-")[1]
	print "lang: " + lang
	text = d["text"][0].encode('utf-8')
	print "text: " + text
	return [text, lang]

def to_english(text):
	print "text[0]: " + text[0]
	print "text[1]: " + text[1]
	cmd = "https://" + key + '&text=' + urllib.quote(text[0]) + '&lang=' + text[1] + urllib.quote('-en')
	print " " + cmd + " "
	uResp = urllib2.urlopen(cmd)
	data = uResp.read()
	d = json.loads(data)
	print d
	if d["code"] != 200:
		print "API error code" + d["code"]
		return text
	lang = d["lang"].split("-")[1]
	print "lang: " + lang
	text = d["text"][0].encode('utf-8')
	print "lang: " + text
	return [text, lang]

#for testing purposes
if __name__ == "__main__":
	translate(["We found them. What do you mean? What a strange person. Burn her anyway! Well, we did do the nose. You can't expect to wield supreme power just 'cause some watery tart threw a sword at you!", "en"])
