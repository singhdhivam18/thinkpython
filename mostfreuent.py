def most_frequent(namestring):
    tupleWord=tuple(namestring)
    
    print(tupleWord)
    lenghtOfTuple=len(tupleWord)
    storedDict=dict()
    for letter in tupleWord:
        if letter not in storedDict:
            storedDict[letter]=1
        else:
            storedDict[letter]=storedDict[letter]+1
    print(storedDict)
    frequencyDict={}
    for key in storedDict:
        valueletter=storedDict[key]
        frequencyOfletter=valueletter/lenghtOfTuple
        if frequencyOfletter not in  frequencyDict:
            frequencyDict[key]=frequencyOfletter
    print(frequencyDict)
    sortedDict=sorted(frequencyDict.items(), key=lambda value:value[1] ,reverse=True)
    print(sortedDict)
    for Wordwithfrequency in sortedDict:
        print(Wordwithfrequency)
        
            
most_frequent('seek')
