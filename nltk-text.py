from nltk.book import *
from nltk import FreqDist
from nltk import bigrams
from nltk import ngrams

print(len(text6)/len(set(text6)))

fdist = FreqDist(text6)
result = fdist.most_common(20)
print(result)

bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print(bigramsDist[('Sir', 'Robin')])

fourgrams = ngrams(text6, 4)
for fourgram in fourgrams:
    if fourgram[0] == 'coconut':
        print(fourgram)