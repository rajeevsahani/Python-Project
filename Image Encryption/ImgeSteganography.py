import numpy
import cv2
import random
m = cv2.imread('messi.jpg', 0) 
x,y=m.shape
print(x,y)
t=numpy.transpose(m)
m,n=t.shape
print(m,n)
asc=[]
s='HELLO'
for i in s:
    asc.append(ord(i))
print("ASCII code of secret key is ",asc)
pos=[]
for a in asc:
    c=0
    loc=[]
    for i in range(m):
        for j in range(n):
            c=c+1
            if(a==t[i][j]):
                loc.append(c)
    pos.append(random.choice(loc))
    print(a,'is found ',len(loc),' times')
print("Final Position is ",pos)
p=[]
for a in pos:
    c=0
    #loc=[]
    for i in range(m):
        for j in range(n):
            c=c+1
            if(a==c):
                p.append(chr(t[i][j]))
print("Final Plain Text is",''.join(p))
               
                
            
