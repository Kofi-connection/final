f=open("message.a0","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()

f=open("message.a0","rb")
num=list(f.read())
print (num)
f.close()

