from set_angram import *
import dbm
import pickle
global delimiter
delimiter=''
global storedword
storedword=read_txt('word2.txt')
db=dbm.open('newdb','c')
print(db)
def storeangram():
    
    
    db['shelf']=pickle.dumps(storedword)
    
    print(pickle.loads(db['shelf']))
def read_angram():
    values,dictOfword=angram_set()
    for word in storedword:
            
            sortedword=sorted(word)
            delimitedWord=delimiter.join(sortedword)
            if delimitedWord in dictOfword:
                print('the angram of  is : ' , word,dictOfword[delimitedWord])
            else:
                 print('not found')

            
storeangram()
read_angram()