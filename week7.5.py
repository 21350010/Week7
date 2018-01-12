
firstSentence = input("Enter Sentence 1 : ")
secondSentence = input("Enter Sentence 2 :")

mainSentence = firstSentence + secondSentence

print(mainSentence)

mainSentenceWordslist = []
for i in range (0,len(mainSentence)):
    mainSentenceWordslist.append(mainSentence[i])
print(mainSentenceWordslist)

mainSentenceWordslist.sort()
print(mainSentenceWordslist)

print(len(mainSentenceWordslist))

print(len(mainSentenceWordslist))

mainSentenceWordsdictionary = {}
count=0
for i in range(0,len(mainSentenceWordslist)):
    for j in range(0,len(mainSentenceWordslist)):
        if mainSentenceWordslist[i] == mainSentenceWordslist[j]:
            count += 1

mainSentenceWordsdictionary[mainSentenceWordslist[i]]=count
count = 0

print(mainSentenceWordsdictionary)
