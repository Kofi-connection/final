text=open ("out1.txt", "r")
result =""
s=4
for words in text:
  for i in range(len(words)):
    char=words[i]
    if (char.isupper()):
       result += chr((ord(char) + s-65) % 26 + 65)
    else: 
       result += chr((ord(char) + s - 97) % 26 + 97)


f=open("out2.txt", "w")
f.write(result)
f.close()

print(result)



text.close()
