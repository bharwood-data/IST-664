import nltk
from nltk import FreqDist

file0 = nltk.corpus.gutenberg.fileids()[0]
emmatext = nltk.corpus.gutenberg.raw(file0)
emmatokens = nltk.word_tokenize(emmatext)
emmawords = [w.lower( ) for w in emmatokens]
#print(len(emmawords))
#print(emmawords[:110])

ndist = FreqDist(emmawords)
nitems = ndist.most_common(30)
#for item in nitems:
#    print (item[0], '\t', item[1])

emmawords2 = nltk.corpus.gutenberg.words('austen-emma.txt')
emmawords2lowercase = [w.lower() for w in emmawords2]

#print(len(emmawords))
#print(len(emmawords2lowercase))

#print(emmawords[:160])
#print(emmawords2lowercase[:160])

emtpydict = dict() # make a dictionary
phonedict = {'Bailey':'32-16','Char':'15-18','Dave':'20-15'}
#print(phonedict['Bailey'])

phonedict['Avi'] = '41-54'
#print(phonedict)

#print(phonedict.keys())
#print(phonedict.values())
#print(phonedict.items())

#print('Char' in phonedict)
#print('Dave' not in phonedict)

#for pair in phonedict.items():
 #   print(pair)

def searchstring(substring, wordlist):
    result = []
    for word in wordlist:
        if substring in word:
            result.append(word)
    return result

print(searchstring('zz', emmawords))

name, phone, location = ('Zack', '22-15', 'Room 159')
#print(name)
#print(phone)
#print(location)

import re

pattern = re.compile('^[^a-z]+$')
nonAlphaMatch = pattern.match('**')
if nonAlphaMatch: print('matched non-alphabetical')

def alpha_filter(w):
    pattern = re.compile('^[^a-z]+$')
    if (pattern.match(w)):
        return True
    else:
        return False    

alphaemmawords = [w for w in emmawords if not alpha_filter(w)]
#print(alphaemmawords[:100])
#print(len(alphaemmawords))

nltkstopwords = nltk.corpus.stopwords.words('english')
#print(len(nltkstopwords))
#print(nltkstopwords)

#print(emmawords[:100])
#print(emmawords[15300:15310])

morestopwords = ['could', 'would', 'might', 'must', 'need', 'sha', 'wo', 'y', "'s", "'d", "'ll","'t","'m","'re","'ve","n't"]

stopwords = nltkstopwords + morestopwords
#print(len(stopwords))
#print(stopwords)

stoppedemmawords = [w for w in alphaemmawords if not w in stopwords]
#print(len(stoppedemmawords))

emmadist = FreqDist(stoppedemmawords)
emmaitems = emmadist.most_common(30)
#for item in emmaitems:
 #   print(item)

emmabigrams = list(nltk.bigrams(emmawords))
#print(emmawords[:21])
#print(emmabigrams[:20])

from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()

#finder = BigramCollocationFinder.from_words(emmawords)
#scored = finder.score_ngrams(bigram_measures.raw_freq)
#print(type(scored))
#first = scored[0]
#print(type(first))
#print(first)

#for bscore in scored[:30]:
 #   print(bscore)

#finder.apply_word_filter(alpha_filter)
#scored = finder.score_ngrams(bigram_measures.raw_freq)
#for bscore in scored[:30]:
 #   print(bscore)

#finder.apply_word_filter(lambda w: w in stopwords)
#scored=finder.score_ngrams(bigram_measures.raw_freq)
#for bscore in scored[:20]:
 #   print(bscore)

#finder3 = BigramCollocationFinder.from_words(emmawords) # <- technique is bad
#scored = finder3.score_ngrams(bigram_measures.pmi)
#for bscore in scored[:20]:
 #   print(bscore)

#finder.apply_freq_filter(5)
#scored = finder.score_ngrams(bigram_measures.pmi)
#for bscore in scored[:30]:
 #   print(bscore)

file9 = nltk.corpus.gutenberg.fileids()[9]
fatherBrowntext = nltk.corpus.gutenberg.raw(file9)
fatherBrowntokens = nltk.word_tokenize(fatherBrowntext)
fatherBrownwords = [w.lower( ) for w in fatherBrowntokens]

finder = BigramCollocationFinder.from_words(fatherBrownwords)
scored1 = finder.score_ngrams(bigram_measures.raw_freq)
#for bscore in scored1[:20]:
#    print(bscore)

finder.apply_word_filter(alpha_filter)
scored1 = finder.score_ngrams(bigram_measures.raw_freq)
#for bscore in scored1[:20]:
 #   print(bscore)

finder.apply_word_filter(lambda w: w in stopwords)
scored1=finder.score_ngrams(bigram_measures.raw_freq)
#for bscore in scored1[:20]:
  # print(bscore)

finder.apply_freq_filter(5)
scored1 = finder.score_ngrams(bigram_measures.pmi)
for bscore in scored1[:20]:
    print(bscore)