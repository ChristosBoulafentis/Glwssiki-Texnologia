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
        tags = nltk.pos_tag(tokens)
        #print(tags)

        for key, value in dict(word2pos).items():
            if value in stop_words:
                del word2pos[key]

        for word in tags:
            if word[0] in word2pos.keys():
                i = word2pos[word[0]][1]
                i += 1
                #word2pos[word[0]] = [word2pos[word[0]][0], i]
            else:
                word2pos[word[0]] = [word[1], 1, filename]


        
        

        

print(word2pos)

#print(list(word2pos.values())[0])