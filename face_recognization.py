import cv2 as cv
import numpy as np

haar_cascade=cv.CascadeClassifier('haar_face.xml')

people=['ben_afflek','elton_john','jerry_seinfeld','madonna','mindy_kaling']
features=np.load('features.npy',allow_pickle=True)
labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'D:\python learning\Open Cv\learning\Faces\val\mindy_kaling\2.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+w]
    label,confidence=face_recognizer.predict(faces_roi)
    print(f'label={people[label]} with a confidence of {confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('detected face',img)


cv.waitKey(0)    
