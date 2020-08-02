import binascii
def dehex(filepath):
 data = open(filepath, "r").read()
 unhex = binascii.unhexlify(data)
 print(unhex)
 
dehex("hex_dump")

