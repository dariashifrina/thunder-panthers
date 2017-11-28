#testing new api because words api required credit card info
#this one does not even require an access token

import requests, json, random
import textRazor
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


meta_data=requests.get("https://api.datamuse.com/words?rel_jjb=beach")
md= meta_data.json()
r_int = int(random.random()*len(md))
r_adj = md[r_int]

#print r_adj['word'] + " beach"


def get_adj(word):
    meta_data=requests.get("https://api.datamuse.com/words?rel_jjb=" + word)
    md= meta_data.json()
    if md != [] :
        r_int = int(random.random()*len(md))
        r_adj = md[r_int]
        return r_adj['word']
    


def get_syn(word):
    meta_data=requests.get("https://api.datamuse.com/words?rel_syn=" + word)
    md= meta_data.json()
    try:
        if (len(md) != 0):
            r_int = int(random.random()*len(md))
            r_syn = md[r_int]
            return r_syn['word']
        else:
            meta_data=requests.get("https://api.datamuse.com/words?ml=" + word)
            md= meta_data.json()
            if len(md) >= 20:
                r_int = int(random.random()*len(md[:20]))
            else:
                r_int = int(random.random()*len(md))
            r_syn = md[r_int]
            return r_syn['word']
    except:
        return word

meta_data=requests.get("https://api.datamuse.com/words?ml=beach")
md= meta_data.json()
#print md

sentence = "I went to the store."
L = sentence[:len(sentence)-1].split()

def new_sent(p):

    p = p.replace(".", " .")
    p = p.replace(",", " ,")
    p = p.replace("!", " !")
    p = p.replace("?", " ?")
    pos_list = textRazor.pos_list(p)
    


    ret_L = []
    p_list = p.split(" ")

#    print p_list
#    print pos_list


    for i in range(len(p_list)):
#        print "element is: " + p_list[i]
#        print "POS id: " + pos_list[i]
#----------------------CASE #1--------------------------------------------------------------------
    #The element is a period, comma, etc. 
    #The element is a pronoun or proper noun
    #Leave it as is (append it to the list)
#-------------------------------------------------------------------------------------------------
        if p_list[i] == "Mr." or p_list[i] =="Mrs." or p_list[i] == "Dr.":
            ret_L.append(p_list[i])

        elif p_list[i] == pos_list[i]:
#            print "case 1"
            ret_L.append(p_list[i])
        elif pos_list[i] == "NNP" or pos_list[i] == "NNPS" or pos_list[i] =="PRP" or pos_list[i] =="PRP$":
#            print "case 1 b"
            ret_L.append(p_list[i])
#----------------------CASE #2--------------------------------------------------------------------
    #The element is a verb or adverb
    #Append a synonym
#-------------------------------------------------------------------------------------------------
        elif "VB" in pos_list[i] or "RB" in pos_list[i]:
            syn = get_syn(p_list[i])
#            print "case 2"
            ret_L.append(syn)
#----------------------CASE #3--------------------------------------------------------------------
    #The element is a noun or adjective
    #Append a synonym AND and adjective for the new synonym
#-------------------------------------------------------------------------------------------------
        elif pos_list[i] == "NN" or pos_list[i] == "NNS" or pos_list[i] == "JJ":
            syn = get_syn(p_list[i])
            adj = get_adj(syn)
            if not (adj is None):
                ret_L.append(adj)
                ret_L.append(syn)
            else:
                ret_L.append(syn)
#----------------------CASE #4--------------------------------------------------------------------
    #otherwise just append the same element to the ret list
#-------------------------------------------------------------------------------------------------
        else:
            ret_L.append(p_list[i])
    ret = " ".join(ret_L)
    ret = ret[0].upper() + ret[1:]
    ret = ret.replace(" .", ".")
    ret = ret.replace(" ,", ",")
    ret = ret.replace(" !", "!")
    ret = ret.replace(" ?", "?")
    return ret 

#print new_sent("I want to eat some food. I want to fly.")


def img_text(p):

    p = p.replace(".", " .")
    p = p.replace(",", " ,")
    p = p.replace("!", " !")
    p = p.replace("?", " ?")
    pos_list = textRazor.pos_list(p)
    ret_L = []
    p_list = p.split(" ")

    for i in range(len(p_list)):
        '''
        print i
        print "pos: " + pos_list[i] 
        print "word: " + p_list[i] 
        print "------------"
        print str(i) + " > 0"
        print pos_list[i - 1] + " == JJ "
        '''

        if "NN" in pos_list[i] or pos_list[i] =="PRP" or pos_list[i] =="PRP$":
            #something like big apple
            if i > 0 and (pos_list[i - 1] == "JJ"):
#                print "case 1"
                ret_L.append(p_list[i - 1] + " " + p_list[i])
            # something like panther runs
            elif i < len(p_list) - 1 and "VB" in pos_list[i + 1]:
#                print "case 2"
                ret_L.append( p_list[i] + " " + p_list[i + 1])

            else:
#                print "case 3"
                ret_L.append(p_list[i])
    if ret_L == []:
        return "blank"
    elif len(ret_L) == 1:
        return ret_L[0]
    else:
        return ret_L[1]

print img_text("I went to the big apple")
