plain=input("Enter plain text ")
print("Entered plain text is ",plain)
import random
#plain="Hello How are you. I am fine."
a=[]
b=[]
for i in plain:
    a.append(ord(i))
print(a)
import cv2
import pandas as pd
img = cv2.imread('messi.jpg',0)
x,y=img.shape
print(x,y)
df = pd.DataFrame(img)
m=[]
n=[]

#print(df)
pos=[]
for k in a:
    #print(k)
    c=0
    loc=[]
    for i in range(x):
        for j in range(y):
            c=c+1;
            #print(c)
            if(k==df.iloc[i,j]):
                loc.append(c)
    m=random.choice(loc)
    print(m)
    pos.append(m)
    print(k,"matched", len(loc),"times")   
print(pos) 
for k in pos:
    c=0
    for i in range(x):
        for j in range(y):
            c=c+1
            if(k==c):
                print(chr(df.iloc[i,j]),end="")
print()
data="hellohoehyervgth"
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key=get_random_bytes(16)
print(key)
cipher=AES.new(key,AES.MODE_ECB)
print(cipher)
ciphertext=cipher.encrypt(data)
print(ciphertext)
data=cipher.decrypt(ciphertext)
print(data)
