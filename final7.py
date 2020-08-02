f=open("FINALpython/copies/FINALinstruction","rw+")

key =150
mylist=[]
for words in f:
  for char in words:
     #print (char)
     x= ord(char)+key
     if x>256:
       x=x%256
     elif x<0:
       x=x%256
     key=key-1
     if key>0:
      key=key%256
     #print(chr(x))
     mylist.append(chr(x))
     with open("FINALpython/encrypted/FINALinstruction","w") as fo:
          for item in mylist:
             fo.write(item)

f.close()

