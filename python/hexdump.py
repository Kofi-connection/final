import binascii
import sys
def file_to_hex(readfilepath, writefilepath):
  hex_str=""
  byte=""
  print("Display characters in ascii")
  with open(readfilepath, "rb") as f:
      byte =f.read(1)
      while byte !="":
          # print(byte,ord(byte), hex(ord(byte)))
           hex_str +=binascii.hexlify(byte)
           byte = f.read(1)
  #print(hex_str)
  f = open(writefilepath,"w")
  f.write(hex_str)
  f.close()

file_to_hex(sys.argv[1],"hex_dump")


