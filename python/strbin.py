import binascii
ip= raw_input("Enter a string\n")
print("convert to binary")
bip=binascii.a2b_base64(ip)
print(bip)
print("convert back to string")
print(binascii.b2a_base64(bip))
