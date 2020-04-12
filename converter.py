from packageinstaller import install
try:
  from keras.models import load_model
except ImportError:
   install('keras')
try:
  import cv2
except ImportError:
   install('opencv-python')
try:
  import numpy as np
except ImportError:
   install('numpy')
from time import sleep
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import os
from tovideo import generate_video
def convertToFramesThanToVideo(filpath):
    os.mkdir('classifiedemotion')
    face_classifier = cv2.CascadeClassifier('Model/haarcascade_frontalface_default.xml')
    classifier =load_model('Model/emotion_face_mobilNet.h5')

    class_labels =['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

# def face_detector(img):
#     # Convert image to grayscale
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(gray,1.3,5)
#     if faces is ():
#         return (0,0,0,0),np.zeros((48,48),np.uint8),img

#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h,x:x+w]

#     try:
#         roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
#     except:
#         return (x,w,y,h),np.zeros((48,48),np.uint8),img
#     return (x,w,y,h),roi_gray,img


    cap = cv2.VideoCapture(filpath)

    count = 0

    while True:
    # Grab a single frame of video
        ret, frame = cap.read()
        if not ret:
            break
        labels = []
        gray = frame
        faces = face_classifier.detectMultiScale(gray,1.3,5)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(224,224),interpolation=cv2.INTER_AREA)
    # rect,face,image = face_detector(frame)


            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

        # make a prediction on the ROI, then lookup the class

                preds = classifier.predict(roi)[0]
                label=class_labels[preds.argmax()]
                label_position = (x,y)
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            else:
                cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        print("classifiedemotion/frame%d.jpg"% count)
        cv2.imwrite("classifiedemotion/frame%d.jpg" % count, frame)
        count+=1

    cap.release()
    cv2.destroyAllWindows()
    #converting to video
    generate_video()
    ##till this frames are formed in classifiedemotion folder


























