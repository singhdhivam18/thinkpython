"""Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the string is in column 70
of the display."""
def right_justify(name):
    length=len(name)#length og th string
    lead=70-length
    print(" "*lead+name)#the 65 space + string
string_name=input("what is a string")
right_justify(string_name)