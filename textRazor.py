import requests, json

def pos_list(sentence, api_key):

    print "--------SENTENCE=-----: " + sentence
    '''
    FUNCTION RETURNS LIST OF PARTS OF SPEECH
    '''

    headers = {
    'x-textrazor-key': api_key,
    }

    data = [
        ('extractors', 'entities,entailments'),
        ('text', sentence),
        ]

    resp = requests.get("https://api.textrazor.com/", headers = headers, data = data)
    ret = resp.json()

    to_ret = []

    for x in range(len(ret['response']['sentences'])):
        parse = ret['response']['sentences'][x]['words']
        for i in range(len(parse)):
            to_ret.append(parse[i]['partOfSpeech'])
    return to_ret



'''
RESULT:
UH
,
PRP
VBP
DT
NN
NNS
.

1.CC Coordinating conjunction
2.CD Cardinal number
3.DT Determiner
4.EX Existential there
5.FW Foreign word
6.IN Preposition or subordinating conjunction
7.JJ Adjective
8.JJ RAdjective, comparative
9.JJ SAdjective, superlative
10.LS List item marker
11.MD Modal
12.NN Noun, singular or mass
13.NN SNoun, plural
14.NN PProper noun, singular
15.NN PSProper noun, plural
16.PD TPredeterminer
17.POS Possessive ending
18.PRP Personal pronoun
19.PRP$ Possessive pronoun
20.RB Adverb
21.RBR Adverb, comparative
22.RBS Adverb, superlative
23.RP Particle
24.SYM Symbol
25.TO to
26.UH Interjection
27.VB Verb, base form
28.VBD Verb, past tense
29.VBG Verb, gerund or present participle
30.VBN Verb, past participle
31.VBP Verb, non-3rd person singular present
32.VBZ Verb, 3rd person singular present
33.WDT Wh-determiner
34.WP Wh-pronoun
35.WP$ Possessive wh-pronoun
36.WRB Wh-adverb
'''

