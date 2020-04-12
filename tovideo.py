# importing libraries 
import os 
from packageinstaller import install
import shutil
try:
  import cv2
except ImportError:
   install('opencv-python')
try:
  from PIL import Image 
except ImportError:
   install('Pillow==2.2.2')

# Checking the current directory path 
from PIL import Image 
import cv2
# Folder which contains all the images 
# from which video is to be generated 
def change_resolution():
    #print(os.listdir("classifiedemotion"))
    os.chdir("classifiedemotion") 
    path = "classifiedemotion"
    mean_height = 0
    mean_width = 0

    num_of_images = len(os.listdir('.')) 
#print(num_of_images) 
    print(os.getcwd()) 
    for file in os.listdir('.'): 
        im = Image.open(file)
        width, height = im.size 
        mean_width += width 
        mean_height += height 
	# im.show() # uncomment this for displaying the image 

# Finding the mean height and width of all images. 
# This is required because the video frame needs 
# to be set with same width and height. Otherwise 
# images not equal to that width height will not get 
# embedded into the video 
    mean_width = int(mean_width / num_of_images) 
    mean_height = int(mean_height / num_of_images) 

# print(mean_height) 
# print(mean_width) 

# Resizing of the images to give 
# them same width and height 
    for file in os.listdir('.'): 
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
		# opening image using PIL Image 
            im = Image.open(file) 

		# im.size includes the height and width of image 
            width, height = im.size 
            print(width, height) 

		# resizing 
            imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS) 
            imResize.save( file, 'JPEG', quality = 95) # setting quality 
		# printing each resized image name 
            print(im.filename.split('\\')[-1], " is resized") 
    path = os.getcwd() 
    print("Current Directory:", path) 
  
# parent directory 
    parent = os.path.join(path, os.pardir) 
  
# prints parent directory 
    print("\nParent Directory:", os.path.abspath(parent)) 
    os.chdir(os.path.abspath(parent))


# Video Generating function 
def generate_video():
    change_resolution()
    image_folder='classifiedemotion'# make sure to use your folder
    video_name = 'PredictedResult/predictedVideo.avi'
    total=len(os.listdir(image_folder))
	
    #images = [img for img in os.listdir(image_folder)
	#		if img.endswith(".jpg") or
	#			img.endswith(".jpeg") or
	#			img.endswith("png")] 


    p="frame"
    images=[]
    for i in range(total):
        images.append(p+str(i)+".jpg")
	
	# Array images should only consider 
    # the image files ignoring others if any
    frame = cv2.imread(os.path.join(image_folder, images[0]))

	# setting the frame width, height width 
    # the width, height of first image
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 20, (width, height),True)

	# Appending the images to the video one by one 
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
	
	# Deallocating memories taken for window creation
    # cv2.destroyAllWindows()
    video.release() # releasing the video generated
    print("Deleting Temporary folder and file if they exists")
    shutil.rmtree('classifiedemotion')
