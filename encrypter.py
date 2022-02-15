import os 
from cryptography.fernet import Fernet 
import platform

key = Fernet.generate_key() 
print(key)

key = str(key)[2:-1] 


f = open("key.txt","w") #it's creating a private key and saving this key to named key and .txt extensioned file.You can change it.
f.write(key)
f.close()

ferNet = Fernet(key) 



def encrypt(dosya):
    with open(dosya,"rb") as readFile:
        okunanDosya = readFile.read()
    
    with open(dosya,"wb") as writeFile:
        try:
            sifreliHal = ferNet.encrypt(okunanDosya)
            writeFile.write(sifreliHal)
            writeFile.close()
            readFile.close()
        except:
            print("There is a problem happen.")




if platform.system() == "Windows":
    for path,gereksiz,files in os.walk(os.getcwd()+"\encrypt"): 
        
        for dosyalar in files:
            dosyaYolu = path + "\\" + dosyalar
            encrypt(dosyaYolu)
elif platform.system() == "Linux":
    for path,gereksiz,files in os.walk(os.getcwd()+"/encrypt"): 
        
        for dosyalar in files:
            dosyaYolu = path + "/" + dosyalar
            encrypt(dosyaYolu)
else:
    print("Incompatible OS.")
