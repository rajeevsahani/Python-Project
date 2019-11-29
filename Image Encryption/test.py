import numpy
import random
'''
#A = [[ 1, 2, 3],[ 4, 5, 6],[7, 8, 9]]
#t=zip(*A)
#print(list(t))
#m = [[ 1, 2, 3],[ 4, 5, 6],[7, 8, 9]]       
#transpose = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
#print(transpose)

a=[]
m=[]
for i in range(8):
    for j in range(8):
        n=int(input("Enter Element:"))
        a.append(n)
    m.append(a)
    a=[]
print(m)
'''
m = [[32, 45, 112, 48, 233, 123, 11, 21],
     [255, 253, 115, 195, 245, 222, 125, 227],
     [127, 111, 255, 112, 135, 28, 110, 228],
     [38, 113, 69, 173, 189, 37, 198, 125],
     [22, 137, 46, 148, 76, 25, 112, 79],
     [72, 23, 136, 24, 185, 36, 187, 127],
     [77, 47, 73, 77, 154, 76, 169, 140],
     [82, 49, 48, 221, 247, 49, 187, 140]]
t=numpy.transpose(m)
#print(t)
asc=[]
s='HELLO'
for i in s:
    asc.append(ord(i))
print("ASCII code of secret key is ",asc)
pos=[]
for a in asc:
    c=0
    loc=[]
    for i in range(len(m[0])):
        for j in range(len(m)):
            c=c+1
            if(a==t[i][j]):
                loc.append(c)
    pos.append(random.choice(loc))
    #print(a,'is found ',len(loc),' times at ',loc)
print("Final Position is ",pos)
p=[]
for a in pos:
    c=0
    loc=[]
    for i in range(len(m[0])):
        for j in range(len(m)):
            c=c+1
            if(a==c):
                p.append(chr(t[i][j]))
print("Final Plain Text is",''.join(p))

                    
                
            
