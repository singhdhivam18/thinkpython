def listinword():
    readed=open('word1.txt','r')#read the word file words
    new_list=[]
    for word in readed:
        readword=word.strip()
        if readword not in new_list:
            new_list.append(readword)
    return new_list
def checkreverse():
    wordlist=listinword()
    for word in wordlist:
        reverseWord=word[::-1]
        if word==reverseWord:
            print('the word is reverseword',word)
checkreverse()    
