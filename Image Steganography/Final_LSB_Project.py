import cv2
import numpy as np
import copy
image = cv2.imread("Tulips.jpg",0)
#print(image)
clone_img = copy.copy(image)
#print(len(image),len(image[0]))
#cv2.imwrite("original.jpg",image)
x,y=image.shape
#print(x,y)
#cv2.imshow("Original Image" , image)
#cv2.waitKey(0)
#s=input("enter text to hide")
secret="HELLO"
asc=[]
for i in secret:
    j=ord(i)
    k=bin(j)[2:]
    asc.append(k)
#print("ASCII code is ",asc)
asc=''.join(asc)
asc=list(asc)
#print("ASCII Value is ",len(asc),asc)
length=len(asc)
binary=[]
pixel=[]
index=0
for m in range(x):
    for n in range(y):
        a=bin(image[m][n])[2:]
        if(m==0 and n==0):
            pixel=length
            #print(pixel)
            clone_img[m][n]=pixel
        elif(index<=length):
            ch=a[:-1]+asc[index-1]
            pixel=int(ch,2)
            clone_img[m][n]=pixel
        else:
            pixel=image[m][n]
            clone_img[m][n]=pixel
        index+=1
#print(len(clone_img [0]),clone_img [0])
#cv2.imshow("Stego Image" , clone_img)
print(clone_img,type(clone_img))
cv2.imwrite('Stego_image.png',clone_img)
clone_img = cv2.imread("Stego_image.png",0)
#for i, j in zip(image[0][:36],clone_img[0][:36]):
#    print(i,bin(i)[2:],j,bin(j)[2:])
x,y=clone_img.shape
print(clone_img,type(clone_img))
index=0
sec=[]
for m in range(x):
    for n in range(y):
        
        if(m==0 and n==0):
            length=clone_img[m][n]
            #print(length)
            
        elif(index<=length):
            a=bin(clone_img[m][n])[2:]
            #print(clone_img[m][n],a)
            ch=a[-1]
            sec.append(ch)
        index+=1
#print("ASCII Value is ",len(sec),sec)
#if(sec==asc):
#    print("both are equal")
text=[]
sec="".join(sec)
#print(sec)
for i in range(5):
    part=sec[i*7:i*7+7]
    #print(part)
    dec=int(part,2)
    #print(b,type(b))
    text.append(chr(dec))
secret="".join(text)
print("Hidden Text is",secret)
