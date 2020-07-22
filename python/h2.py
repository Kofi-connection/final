textf=open("out2.txt","r")

frequencies ={}
for words in textf:
  for char in words:
    if char in frequencies:
      frequencies[char] += 1
    else: 
      frequencies[char] = 1


print ("The frequencies are; \n {}" .format(str(frequencies)))

textf.close()


