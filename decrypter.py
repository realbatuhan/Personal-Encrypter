
import os 
from cryptography.fernet import Fernet 
import platform

f = open("key.txt","r") #gets decrypt key, generated by encryter from "key.txt" file
key = f.read()
print(key)
 
ferNet = Fernet(key) 
 
 
def coz(dosya):
    with open(dosya,"rb") as readFile:
        okunanDosya = readFile.read()
    
    with open(dosya,"wb") as writeFile:
        try:
            cozulmusHal = ferNet.decrypt(okunanDosya)
            writeFile.write(cozulmusHal)
            writeFile.close()
            readFile.close()
        except:
            print("Error.")
 
 

 
if platform.system() == "Windows":
    for path,gereksiz,files in os.walk(os.getcwd()+"\encrypt"):
        
        for dosyalar in files:
            dosyaYolu = path + "\\" + dosyalar
            coz(dosyaYolu)
elif platform.system() == "Linux":
    for path,gereksiz,files in os.walk(os.getcwd()+"/encrypt"): 
        
        for dosyalar in files:
            dosyaYolu = path + "/" + dosyalar
            coz(dosyaYolu)
else:
    print("Operating System not supported.")