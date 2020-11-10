from nltk.book import *
from nltk import FreqDist

print(text6)
print(len(text6))
print(len(set(text6)))
print(len(text6)/len(set(text6)))

fdist = FreqDist(text6)
result = fdist.most_common(20)
print(result)