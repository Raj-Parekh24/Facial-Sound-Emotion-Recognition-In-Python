#!/usr/bin/env python
# coding: utf-8

# In[4]:


from packageinstaller import install
try:
  import shutil
except ImportError:
   install('shutil')
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from camera import camerafun
from converter import convertToFramesThanToVideo 
import os 
import tkinter as tk
popJ = 0


print("Deleting Temporary folder and file if they exists") 
# Current working directory 
if os.path.exists('PredictedResult'):
    shutil.rmtree('PredictedResult')
if os.path.exists('predictedVideo.avi'):
    os.remove('predictedVideo.avi')
if os.path.exists('classifiedemotion'):
    shutil.rmtree('classifiedemotion')
if os.path.exists('audio1.wav'):
    os.remove('audio1.wav')
if os.path.exists('audio2.wav'):
    os.remove('audio2.wav')
if os.path.exists('audio3.wav'):
    os.remove('audio3.wav')
os.mkdir('PredictedResult')
    
def genInput(): #Allows the user to input the data
    gen = Toplevel()
    gen.wm_title("Data Input")
    v = IntVar()
    v.set(popJ)
    ent1 = Entry(gen, textvariable = v)
    ent1.pack()
    Label(gen, text = 'enter interval of audio splitter in seconds:- ').pack()
    
    def quit1():   # Need to be here or it breaks the program
        gen.destroy()

    def submit():
        global popJ
        popJ = v.get()
        return
    
        
 
 
    def fileDialog():
        #directory path is self.filename
        submit()
        ##use popJ after submit functuion, popJ=entered text
        filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("mp4 files","*.mp4"),("all files","*.*")) )
        label = ttk.Label( text = "")
        from extract_audio import extract_audio
        extract_audio(filename)
        from predictionaudio import wwritecsv
        wwritecsv(int(popJ))
        #till here audio is predicted
        convertToFramesThanToVideo(filename)
        #till here video is predicted now we will predict audio
    
    submit1= Button(gen, text="Browse file",command=fileDialog)
    submit1.pack()
    submit1.configure(command = fileDialog)

    
def menu():  # creates the gui menu
    menu = tk.Tk()
    frame = tk.Frame(menu)
    frame.pack()
    photo = PhotoImage(file = "emoji.png")
    w = Label(menu, image=photo)
    w.pack()
    ent = Entry(menu)
    ent.pack()
    ent.focus_set()

    button1 = tk.Button(frame, text="   Camera   ",bd='5' , fg="black",pady ='10',relief='raised',activeforeground='red',command=camerafun)#insert camera fuction
    button1.pack(side=tk.LEFT)
    button2 = tk.Button(frame, text="Choose Video",bd='5',pady ='10',activeforeground='red', command=genInput)
    button2.pack(side=tk.LEFT)
    
    menu.mainloop()

menu()


# In[ ]:




