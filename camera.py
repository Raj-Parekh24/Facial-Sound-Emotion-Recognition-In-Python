from packageinstaller import install
try:
  from keras.models import load_model
except ImportError:
   install('Keras')
try:
  import cv2
except ImportError:
   install('opencv-python')
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
try:
  import numpy as np
except ImportError:
   install('numpy')
from keras.models import load_model
import numpy as np
import cv2
def camerafun():
    face_classifier = cv2.CascadeClassifier('Model/haarcascade_frontalface_default.xml')
    classifier =load_model('Model/emotion_face_mobilNet.h5')

    class_labels =['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

    cap = cv2.VideoCapture(0)

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
        cv2.imshow('Emotion Detector',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


























