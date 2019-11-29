from PIL import Image
data = input("Enter data to be encoded : ")
lengthHiddenData=len(data)
#data ="HELLO"
asc=[]
for i in data:
    j=ord(i)
    k=bin(j)[2:]
    if(len(k)!=8):
        s=8-len(k)
        k='0'*s+k
    asc.append(k)
#print("ASCII code is ",asc)
asc=''.join(asc)
asc=list(asc)
length=len(asc)
#print("ASCII Value length is ",length)
#print("ASCII Value is ",asc)
originalfile='Tulips';
#originalfile=input("Enter name of image file (RGB Model only):")
originalFile=originalfile+".jpg"
image = Image.open(originalFile, 'r')
clone_img= image.copy()
x,y = clone_img.size[0],clone_img.size[1]
'''
for m in range(6):
    for n in range(6):
        print("Clone image ",clone_img.getpixel((m,n))[0])
'''
size=clone_img.size
#print(size,x,y)
index=0
for m in range(x):
    for n in range(y):
        r=clone_img.getpixel((m,n))[0]
        g=clone_img.getpixel((m,n))[1]
        b=clone_img.getpixel((m,n))[2]
        #print(r)
        #print(r,g,b)
        r=bin(r)[2:]
        #print(r)
        if(m==0 and n==0):
            pixel=length
            
            clone_img.putpixel((m, n), (pixel,g,b)) 
        elif(index<=length):
            ch=r[:-1]+asc[index-1]
            pixel=int(ch,2)
            clone_img.putpixel((m, n), (pixel,g,b))
        else:
            pixel=clone_img.getpixel((m,n))[0]
            clone_img.putpixel((m, n), (pixel,g,b))
        index+=1
'''
for m in range(6):
    for n in range(6):
        print("Clone image ",clone_img.getpixel((m,n)))
'''
stegofile="Stego"+originalfile
#print(stegofile)
clone_img.save(stegofile+'.png')
stego_img = Image.open(stegofile+'.png', 'r')
#print(stego_img,type(stego_img))
X,Y = stego_img.size[0],clone_img.size[1]
print("Hiding of Text inside Image is completed....")
index=0
secret=[]
for m in range(X):
    for n in range(Y):
        #print(stego_img.getpixel((m,n))[0])
        if(m==0 and n==0):
            length=stego_img.getpixel((m,n))[0]
            #print(length)
        elif(index<=length):
            a=bin(stego_img.getpixel((m,n))[0])[2:]
            ch=a[-1]
            secret.append(ch)
        index+=1
#print(secret,len(secret))
#if(asc==secret):
#    print("both are equal")
text=[]
secret="".join(secret)
#print(sec)
for i in range(lengthHiddenData):
    part=secret[i*8:i*8+8]
    #print(part)
    dec=int(part,2)
    #print(b,type(b))
    text.append(chr(dec))
OriginalText="".join(text)
print("Hidden Text is",OriginalText)
print("Hidden Text from Image is recovered....")        
