# Facial-Sound-Emotion-Recognition-In-Python
Facial/Sound Emotion Recognition Using Keras and MLPClassifier.<br>
<b>PSC Project.</b><br>
By: 	Raj Parekh     (18BCE143) <br>
    	Nitin Shah     (18BCE138) <br>
    	Nishil Agrawal (18BCE137) <br>

Objective: Design of a python script that helps us to recognize the emotions using facial expressions and speech with the help of machine learning.<br>

Examples:-
 <br>
 <br>
 ![alt text](https://github.com/Raj-Parekh24/Facial-Sound-Emotion-Recognition-In-Python/blob/master/examples/angry.png)<br>
 ![alt text](https://github.com/Raj-Parekh24/Facial-Sound-Emotion-Recognition-In-Python/blob/master/examples/happy.png)<br>
 ![alt text](https://github.com/Raj-Parekh24/Facial-Sound-Emotion-Recognition-In-Python/blob/master/examples/fear.png)<br>
 

<b>Links:-</b>
	Face-Emotion Datasets: https://www.kaggle.com/deadskull7/fer2013<br>
	Voice-Emotion:	https://zenodo.org/record/1188976<br>
Note:- Datasets should be stored in the data folder.<br>

<b>Training Face-Emotion Dataset:-</b><br>
We first converted the fer2013 dataset from csv format to 48x48 images using pandas, numpy and opencv libraries. We then augmented images using keras library to enhance our training dataset. To train our dataset, we used google mobile net model.

<b>Training Voice-Emotion Dataset:-</b><br>
We extracted 3 types of features<b>(MFCC, Chroma, Mel)</b> from the ravdess dataset and stored them in the form of nested list. We trained it using MLP classifier which is a part of sklearn module.<br>
<b>How to Train the Face-Emotion Model:</b><br>
1)	Open command line prompt in the project folder.<br>
2)	Run “python classifiretraining.py”<br>

<b>How to Train the Voice-Emotion Model:</b><br>
1)	Open command line prompt in the project folder.<br>
2)	Run “python audiotrainer.py”<br>

<b>How to run the program:</b><br>
1)	 Open command line prompt in the project folder.<br>
2)	Run “python FinalApp.py”<br>
Click on <b>“Camera” </b>to enable face-emotion recognition where the input is from your webcam.</br>
Click on <b>“Choose Video”</b> to run face-emotion recognition as well as the voice-emotion recognition on the selected video. (Enter interval time in seconds which will divide the mp4 video into subparts and give you results of each subpart in an excel sheet)<br>
<b>Note: Works with only .mp4 files.</b><br>
<b>The results will be stored in PredictedResult folder. The contents of the folder will change if you run the program again.</b>


