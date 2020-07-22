text=open("ceaser1.txt", "r")
e='e'
t='t'
counte=0
countt=0
for line in text:
   words=line.split()
   
   for x in words:
   # print(words) 
    if e in x:
     counte +=1
    elif t in x:
     countt +=1

results="There are {} e's in the file and {} t's. "
print (results.format(counte, countt))


text.close()

