
import cv2  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
# capture frames from a camera 
cap = cv2.VideoCapture(0) 
# loop runs if capturing has been initialized. 
while 1:  
    # reads frames from a camera 
    ret, img = cap.read()  
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray)
    #print(faces)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        # To draw a rectangle in a face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    # Display an image in a window 
    cv2.imshow('img',img) 
    # Wait for Esc key to stop 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Close the window 
cap.release() 
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  
