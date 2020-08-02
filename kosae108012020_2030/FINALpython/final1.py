import shutil, os
# creates a FINALpython directory 
os.mkdir("FINALpython")
#creates a copies subdirectory 
os.makedirs("FINALpython/copies")
#creates an encrypted subdirectory
os.makedirs("FINALpython/encrypted")
#creates a decrypted subdirectory
os.makedirs("FINALpython/decrpyted")
# adds this file, "final1.py to the FINALpython directory 
shutil.copy("final1.py","FINALpython")

