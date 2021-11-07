#!

with open ("6K adverbs.txt", "r") as adverbs:
    adverbList = adverbs.readlines()
adverbs.close()
for adverbList in adverbList:
    print (adverbList)
