#!/usr/bin/env python
# coding: utf-8

# In[1]:

from packageinstaller import install
try:
  from moviepy.editor import *
except ImportError:
   install('moviepy')
import sys
from moviepy.editor import *
def extract_audio(filepath):
    video = VideoFileClip(filepath) 
    audio = video.audio 
    audio.write_audiofile('audio1.wav') 


# In[ ]:




