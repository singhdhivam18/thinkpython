'''Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
'''
def read_words(filename):
    fin=open(filename)
    empty_dict={}
    for key in fin:
        empty_dict[key]=1
    print(empty_dict)
    #check whether words are in empty_dict
    for fin in empty_dict:
        if fin in empty_dict:
            print('yes')
        else:
            print('no')
read_words('word.txt')
