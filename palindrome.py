def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(first,middle,last):
    if first==last:
        print("the word is palindrome")
    else:
        print("not")
word=input("enter the string")

f1=first(word)
l1=last(word)
m=middle(word)
is_palindrome(f1,m,l1)

#middle(" ")#string called with two letter  one letter empty string= it return noting 
