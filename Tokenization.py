from xml.dom.minidom import Document
import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict
from collections import Counter
import os
from dicttoxml import dicttoxml
#############################################################################




#############################################################################

path, dirs, files = next(os.walk("cleared/"))
file_count = len(files)

read_directory = '/home/chris/Documents/GitHub/Glwssiki-Texnologia/cleared/'

stop_words = [{'CD'},{'CC'},{'DT'},{'EX'},{'IN'},{'LS'},{'MD'},{'PDT'},{'POS'},{'PRP'},{'PRP$'},{'RP'},{'TO'},{'UH'},{'WDT'},{'WP'},{'WP$'},{'WRB'}]
word2pos = defaultdict(set)
keys_list = ["word","type","times","article"]

for filename in os.listdir(read_directory):
    with open(read_directory + filename, 'r') as file:
        data = file.read().rstrip()
        
        tokens = nltk.word_tokenize(data)
        #print(tokens)
        #tags = nltk.pos_tag(["tokens"])
        word2pos['lemma'] = {'@name': (), 'document_id': (), 'times': ()}

        print("AAAAAAAAAA",word2pos[word]['document'])
        for word in tokens:
            inany = False
            if word in word2pos['lemma']['@name']:
                for k in word2pos[word]['document']:
                    if filename == k['@id']:
                        i = k['times']
                        i += 1
                        k = {'@id': filename, 'times': 1}
                        inany = True
                if inany == False:
                    word2pos[word]['document'].append([1, filename])   
            else:
                word2pos['lemma'] = {'@name': word, 'document': [{'@id': filename, 'times': 1}]}
                #word2pos[word] = [[1, filename]]


print(word2pos)
'''for key in word2pos.copy():
    if {nltk.pos_tag([str(key)])[0][1]} in stop_words:
        del word2pos[key]



for word in word2pos.keys():
    for item in word2pos[word]:
        weight = item[0] * file_count / len(word2pos[word])
        item.append(weight)

#print(word2pos)


xml = dicttoxml(word2pos)
#print(xml)

xml_decode = xml.decode()
 
xmlfile = open("dict.xml", "w")
xmlfile.write(xml_decode)
xmlfile.close()
'''