import os
import cv2 as cv
import numpy as np

people=['ben_afflek','elton_john','jerry_seinfeld','madonna','mindy_kaling']
dir = r'D:\python learning\Open Cv\learning\Faces\train'

haar_cascade=cv.CascadeClassifier('haar_face.xml')
features=[]
labels=[]

def create_train():
    for person in people:
        path=os.path.join(dir,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img) 
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'no of features={len(features)}')
print(f'no of labels={len(labels)}')
np.save('features.npy',np.array(features,dtype='object'))
np.save('labels.npy',np.array(labels))



face_recognizer=cv.face.LBPHFaceRecognizer_create()


# create the recognizer on features and labels

face_recognizer.train(np.array(features,dtype='object'),np.array(labels))

face_recognizer.save('face_trained.yml')

