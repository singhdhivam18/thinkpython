'''Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit'''
def sed(patterString,replaceString,firstfile,secondfilename):
    readfile=open(firstfile,'r')
    writefile=open(secondfilename,'w')
    for word in readfile:
        stripWord=word.strip()
        if stripWord==patterString:
            patterString=replaceString
            
            writefile.write(patterString)
        else:
            writefile.write(word)
sed('hacker','whitehacker','word.txt','test.txt')