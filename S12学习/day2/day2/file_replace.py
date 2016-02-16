
import os
f = open("test.txt","r")
f_new = open("text_new.txt","w")
for line in f:
    if line.startswith("alex"):
        new_line = line.replace("alex","ALEX LI....")
        f_new.write(new_line)
    else:
        f_new.write(line)
f.close()
f_new.close()
os.rename("test.txt","test.txt.bak")
os.rename("text_new.txt","test.txt")

'''
f = open("test.txt","r+")
for line in f:
    if line.startswith("alex"):
        new_line = line.replace("alex","ALEX LI")
        print("current pos:",f.tell())
        f.seek(37)
        f.write(new_line)
        break
f.close()
'''