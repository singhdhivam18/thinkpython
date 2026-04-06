def retriveword():
    wordlist=[]
    fileWord=open('word1.txt')
    for WOrd in fileWord:
        stripWord=WOrd.strip()
        wordlist.append(stripWord)
    checkcondition(wordlist)
#start lenght from 3 to 10 test
#list name are
global fourletterlist
global fiveletterlist
global eightletterlist
global tenletterlist
fourletterlist=[]
fivelettterlist=[]
eightletterlist=[]
tenletterlist=[]
def checkcondition(calledwordlist):
    for calledword in calledwordlist:
        if len(calledword)==4:
            fourletterlist.append(calledword)
        elif len(calledword)==5:
            fivelettterlist.append(calledword)
        elif len(calledword)==8:
            eightletterlist.append(calledword)
        else:
            tenletterlist.append(calledword)

def itirative():
    for i in range(0,2):
        j=i+1
        for j in range(0,2):
            strword=fourletterlist[i]+fourletterlist[j]
            for word8 in eightletterlist:
                if sorted(strword)==sorted(word8):
                    print(strword,word8)


def print_all():
    print('fourlist',fourletterlist)
    print('five',fivelettterlist)
    print('eight',eightletterlist)
    print('ten ',tenletterlist)       
retriveword()
print_all()
itirative()
