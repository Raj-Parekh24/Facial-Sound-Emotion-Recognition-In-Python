# Facial-Sound-Emotion-Recognition-In-Python
Facial/Sound Emotion Recognition Using Keras and MLPClassifier.
PSC Project.
By: 	Raj Parekh     (18BCE143)
    	Nitin Shah     (18BCE138)
    	Nishil Agrawal (18BCE137)

Objective: Design of a python script that helps us to recognize the emotions using facial expressions and speech with the help of machine learning.

Examples:-
 
 
 

Links:
	Face-Emotion Datasets: https://www.kaggle.com/deadskull7/fer2013
	Voice-Emotion:	https://zenodo.org/record/1188976
Note:- Datasets should be stored in the data folder.

Training Face-Emotion Dataset:
We first converted the fer2013 dataset from csv format to 48x48 images using pandas, numpy and opencv libraries. We then augmented images using keras library to enhance our training dataset. To train our dataset, we used google mobile net model.

Training Voice-Emotion Dataset:
We extracted 3 types of features(MFCC, Chroma, Mel) from the ravdess dataset and stored them in the form of nested list. We trained it using MLP classifier which is a part of sklearn module.
How to Train the Face-Emotion Model:
1)	Open command line prompt in the project folder.
2)	Run “python classifiretraining.py”

How to Train the Voice-Emotion Model:
1)	Open command line prompt in the project folder.
2)	Run “python audiotrainer.py”

How to run the program:
1)	 Open command line prompt in the project folder.
2)	Run “python FinalApp.py”
Click on “Camera” to enable face-emotion recognition where the input is from your webcam.
Click on “Choose Video” to run face-emotion recognition as well as the voice-emotion recognition on the selected video. (Enter interval time in seconds which will divide the mp4 video into subparts and give you results of each subpart in an excel sheet)
Note: Works with only .mp4 files.
The results will be stored in PredictedResult folder. The contents of the folder will change if you run the program again.


