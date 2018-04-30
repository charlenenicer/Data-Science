#Pre-processing intro in Data science
#Use of python as well
#What is going on here
#credits to Andreas Mueller for stopwords
#98-0.txt <- Tale of Two Cities, by Charles Dickens. Credit to Project Gutenberg.
# code package credits to Python for Data Science UC San Diego 

import collections
file = open('') # insert random file (preferrably text file)

#(optional)
# to stripof common words such as "the", "a", "an", etc we will use stopwords 
stopwords = set(line.strip for line in open("stopwords"))

# Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If it does, increase the count.

for word in file.read().lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

#sorting out 
d = collections.Counter(wordcount)


#print the 10 most common words and their count
for word, count in d.most_common(10):
	print(word, ": ", count)