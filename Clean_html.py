
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

read_directory = '/home/chris/Documents/GitHub/Glwssiki-Texnologia/artcl/'
write_directory = '/home/chris/Documents/GitHub/Glwssiki-Texnologia/cleared/'
for filename in os.listdir(read_directory):
    f = open(read_directory + filename, "r")

    soup = BeautifulSoup(f, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

    #print(text)
    with open(write_directory + filename + '.txt', 'w') as r:
        r.write(text)