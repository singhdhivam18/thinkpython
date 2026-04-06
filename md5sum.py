import os
filename='word2.txt'
cwd='md5sum'+filename
fp=os.popen(cwd)
read=fp.read()
close=fp.close()
print(read)