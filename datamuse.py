#testing new api because words api required credit card info
#this one does not even require an access token

import requests, json, random

boop=requests.get("https://api.datamuse.com/words?ml=ringing+in+the+ears&max=4")

data= boop.json()
#print data

'''
ml:

Means like constraint: require that the results have a meaning related to this string value, which can be any word or sequence of words. (This is effectively the reverse dictionary feature of OneLook.)

sl:

Sounds like constraint: require that the results are pronounced similarly to this string of characters. (If the string of characters doesn't have a known pronunciation, the system will make its bestguess using a text-to-phonemes algorithm.)

sp:

Spelled like constraint: require that the results are spelled similarly to this string of characters, or that they match this wildcard pattern. A pattern can include any combination of alphanumeric characters, spaces, and two reserved characters that represent placeholders  (which matches any number of characters) and (which matches exactly one character).

rel_[code]:

Related word constraints: require that the results, when paired with the word in this parameter, are in a predefined lexical relation indicated by [code]. Any number of these parameters may be specified any number of times. An assortment of semantic, phonetic, and corpus-statistics-based relations are available. At this time, these relations are available for English-language vocabularies only. 

md:

Metadata flags: A list of single-letter codes (no delimiter) requesting that extra lexical knowledge be included with the results.

'''

keep = ["a", "an", "the", "I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", "what", "who", "mine", "yours", "his", "hers", "ours", "theirs", "this", "that", "these", "those", "who", "whom", "whose", "which", "that", "what", "whatever", "whoever", "whomever", "whichever", "myself", "yourself", "himself", "herself", "itself", "ourselves", "themselves", "am", "is", "was", "are", "were", "and", "or", "but", "so", "for", "yet", "after", "although","as", "because", "before", "once", "since", "though", "till", "unless", "until", "what", "when", "whenever", "whether", "while", "to", "of", "for", "by", "your", "our", "their"]


meta_data=requests.get("https://api.datamuse.com/words?rel_jjb=beach")
md= meta_data.json()
r_int = int(random.random()*len(md))
r_adj = md[r_int]

#print r_adj['word'] + " beach"


def get_adj(word):
    meta_data=requests.get("https://api.datamuse.com/words?rel_jjb=" + word)
    md= meta_data.json()
    r_int = int(random.random()*len(md))
    r_adj = md[r_int]
    return r_adj['word']



def get_syn(word):
    meta_data=requests.get("https://api.datamuse.com/words?rel_syn=" + word)
    md= meta_data.json()
    if (len(md) != 0):
        r_int = int(random.random()*len(md))
        r_syn = md[r_int]
        return r_syn['word']
    else:
        meta_data=requests.get("https://api.datamuse.com/words?ml=" + word)
        md= meta_data.json()
        r_int = int(random.random()*len(md[:20]))
        r_syn = md[r_int]
        return r_syn['word']
        

#print get_syn('beach')


meta_data=requests.get("https://api.datamuse.com/words?ml=beach")
md= meta_data.json()
#print md

sentence = "I went to the store."
L = sentence[:len(sentence)-1].split()


def new_sent(p):
    print "SENTENCE WAS: " + p
    x = p[:len(p)-1].split(" ")
    ret_L = []
    for i in range(len(x)):
        #print i
        if (x[i] == "I"):
            ret_L.append(x[i])
        elif (x[i].lower() in keep):
            ret_L.append(x[i])
        elif x[i][len(x[i]) - 2:] == "ed" or x[i][len(x[i]) - 3:] == "ing" or x[i][len(x[i]) - 3:] == "ent":   
            ret_L.append(x[i]) 
        else:
            syn = get_syn(x[i])

#            print "searching for adj for " + syn
            if ( i != len(x)-1 and len(syn.split(" ")) == 1 and x[i+1] not in keep):
                try:
                    adj = get_adj(syn)
                    ret_L.append(adj)
                except:
                    print ""
            ret_L.append(syn)
    ret = " ".join(ret_L)
    return ret + p[len(p)-1]
            
print new_sent("I went to the beach.")
print new_sent("I love to drink coffee.")

print new_sent("Your mom is awesome.")

