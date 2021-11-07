#!

import random #, re

with open ("6K adverbs.txt", "r") as adverbs:
    adverbList = adverbs.readlines()
adverbs.close()

with open ("28K adjectives.txt", "r") as adjectives:
    adjectiveList = adjectives.readlines()
adjectives.close()

with open ("31K verbs.txt", "r") as verbs:
    verbsList = verbs.readlines()
verbs.close()

with open ("91K nouns.txt", "r") as nouns:
    nounsList = nouns.readlines()
nouns.close()

sentence = (" {} {} {} {} {}".format("PlaceHolder", verbsList[random.randint(0,len(verbsList))], nounsList[random.randint(0,len(nounsList))],\
    adjectiveList[random.randint(0,len(adjectiveList))], adverbList[random.randint(0,len(adverbList))]))
sentence = sentence.strip()
print (sentence)