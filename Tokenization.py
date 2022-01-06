import nltk
from nltk.tokenize import word_tokenize
import os

read_directory = '/home/chris/Documents/GitHub/Glwssiki-Texnologia/cleared/'

for filename in os.listdir(read_directory):
    with open(read_directory + filename, 'r') as file:
        data = file.read().rstrip()
        
        tokens = nltk.word_tokenize(data)
        tags = nltk.pos_tag(tokens)

        print(tags)