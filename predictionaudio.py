from packageinstaller import install
try:
  from sklearn.externals import joblib
except ImportError:
   install('scikit-learn')
try:
  import librosa
except ImportError:
   install('librosa')
try:
  import glob
except ImportError:
   install('glob2')
try:
  import pickle
except ImportError:
   install('pickle-mixin')

from sklearn.externals import joblib
import os
import soundfile # to read audio file
import numpy as np
import librosa # to extract speech features
import glob
import os
import pickle # to save model after training
from sklearn.model_selection import train_test_split # for splitting training and testing
from sklearn.neural_network import MLPClassifier # multi-layer perceptron model
from sklearn.metrics import accuracy_score # to measure how good we are


# In[42]:


def extract_feature(file_name, **kwargs):
    """
    Extract feature from audio file `file_name`
        Features supported:
            - MFCC (mfcc)
            - Chroma (chroma)
            - MEL Spectrogram Frequency (mel)
            - Contrast (contrast)
            - Tonnetz (tonnetz)
        e.g:
        `features = extract_feature(path, mel=True, mfcc=True)`
    """
    mfcc = kwargs.get("mfcc")
    chroma = kwargs.get("chroma")
    mel = kwargs.get("mel")
    contrast = kwargs.get("contrast")
    tonnetz = kwargs.get("tonnetz")
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        if chroma or contrast:
            stft = np.abs(librosa.stft(X))
        result = np.array([])
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))
        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result = np.hstack((result, chroma))
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result = np.hstack((result, mel))
        if contrast:
            contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
            result = np.hstack((result, contrast))
        if tonnetz:
            tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
            result = np.hstack((result, tonnetz))
    return result

# Load the model from the file
model = joblib.load('Model/emotionaudio.pkl')


print("Converting the audio from stereo to mono audio\n\n\n")
def convert_audio(audio_path, target_path, remove=False):
    """This function sets the audio `audio_path` to:
        - 16000Hz Sampling rate
        - one audio channel ( mono )
            Params:
                audio_path (str): the path of audio wav file you want to convert
                target_path (str): target path to save your new converted wav file
                remove (bool): whether to remove the old file after converting
        Note that this function requires ffmpeg installed in your system."""

    os.system(f"ffmpeg -i {audio_path} -ac 1 -ar 16000 {target_path}")
    # os.system(f"ffmpeg -i {audio_path} -ac 1 {target_path}")
    if remove:
        os.remove(audio_path)


# In[85]:


def predict(audio_path):
        new_feature = extract_feature(audio_path, mfcc=True, chroma=True, mel=True)
        data = []
        data.append(new_feature)
        data = np.array(data)
        z_pred = model.predict(data)
        return z_pred
from pydub import AudioSegment
def wwritecsv(q=3):
    convert_audio("audio1.wav","audio2.wav")
    newAudio = AudioSegment.from_wav("audio2.wav")
    newAudiolst = newAudio[::q*1000]
    j = 0
    lst = []
    for i in newAudiolst:
        x = []
        i.export('audio3.wav', format="wav")  # Exports to a wav file in the current path.
        p = str(j) + " - " + str(j + q)
        x.append(p)
        x.append(predict("audio3.wav"))
        os.remove("audio3.wav")
        lst.append(x)
        j = j + q+1

    # In[86]:

    import pandas as pd
    df=pd.DataFrame(lst, columns=['Seconds Interval', 'Predict Result'], index=range(1, len(lst) + 1))
    print("Saving predict result in form of csv named asPredictedResultOfAudio.csv")
    df.to_csv('PredictedResult/PredictedResultOfAudio.csv', header=True, index=True)
    os.remove('audio2.wav')
    os.remove('audio1.wav')




