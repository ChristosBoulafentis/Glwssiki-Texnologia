import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict
from collections import Counter
import os
#############################################################################




#############################################################################

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

        for word in tokens:
            inany = False
            if word in word2pos.keys():
                for k in range(len(word2pos[word])):
                    if filename == word2pos[word][k][1]:
                        i = word2pos[word][k][0]
                        i += 1
                        word2pos[word][k] = (i, filename)
                        inany = True
                        #break
                if inany == False:
                    word2pos[word].append((1, filename))   
            else:
                word2pos[word] = [(1, filename)]

for key in word2pos.copy():
    if {nltk.pos_tag([str(key)])[0][1]} in stop_words:
        del word2pos[key]

print(word2pos)

#print(list(word2pos.values())[0])