import nltk
print(nltk.corpus.gutenberg.fileids())
file9 = nltk.corpus.gutenberg.fileids()[9]
print(file9)
cbtext=nltk.corpus.gutenberg.raw(file9)
type(cbtext)
len(cbtext)
print(cbtext[:120])
cbtokens = nltk.word_tokenize(cbtext)
print(len(cbtokens))
print(cbtokens[:30])
cbwords = [w.lower() for w in cbtokens]
print(len(cbwords))
cbvocab = sorted(set(cbwords))
print(cbvocab[:50])

from nltk import FreqDist
fdist = FreqDist(cbwords)
fdistkeys = list(fdist.keys())
print(fdistkeys[:30])
#print(fdist['emma'])
topkeys = fdist.most_common(30)
for pair in topkeys:
    print(pair)
numwords = len(cbwords)
topkeysnorm = [(word, freq/numwords) for (word, freq) in topkeys]
for pair in topkeysnorm:
    print(pair)