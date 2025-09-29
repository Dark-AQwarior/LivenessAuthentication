# Liveness Authentication

Liveness Authentication, an anti-spoofing liveness detection mechanism distinguishes live person in front of camera from spoofing attacks such as photos, videos or masks also fraud prevention for face detection in general. Face recognition systems are becoming more prevalent than ever. From face recognition on your iPhone/smartphone, to face recognition for mass surveillance in China, face recognition systems are being utilized everywhere. However, face recognition systems are easily fooled by “spoofing” and “non-real” faces. Face recognition systems can be circumvented simply by holding up a photo of a person (whether printed, on a smartphone, etc.) to the face recognition camera. In order to make face recognition systems more secure, we need to be able to detect such fake/non-real faces — liveness detection is the term used to refer to such algorithms. For the purpose of this project, we’ll be treating liveness detection as a binary classification problem.

![Alt text](https://i.pinimg.com/originals/7c/d5/3d/7cd53d36d121d839da9600ca055b01db.gif)

## Features
If the user is "authorized" i.e., real:
```
1.  Green color box is drawn on the python frame including 'Authorized' to recognize easily.
2.  Voice assistance provided for confirmation.
3.  Access Granted
```
If the user is "un-authorized" i.e., fake:
```
1.  Red color box is drawn on the python frame including 'Unauthorized' to recognize easily.
2.  Voice assistance provided for confirmation.
3.  Email will be sent to the owner specifying the following details of the Intruder:
       (I)   Snapshot, 
       (II)  Computer name,
       (III) The ip-address, and
       (IV)  Location
4.  The device will be locked, and the intruder cannot access any files.
```

## Pre-requisites and download links
 
 Python - https://www.python.org/downloads/ \
 PIP \
 Anaconda - https://www.anaconda.com/products/individual#Downloads \
 Tip: You won't need to seperately install python if you download the anaconda software.
 
## Clone/Download my git repository
```
1.  On GitHub, navigate to the main page of the repository.
2.  Above the list of files, click Download Code.
3.  To clone the repository using HTTPS, under "Clone with HTTPS", click copy symbol.
4.  Open Git Bash.
5.  Change the current working directory to the location where you want the cloned directory.
6.  Type git clone, and then paste the URL you copied earlier.
        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
        
7. Press Enter to create your local clone.
        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
        > Cloning into `Spoon-Knife`...
        > remote: Counting objects: 10, done.
        > remote: Compressing objects: 100% (8/8), done.
        > remove: Total 10 (delta 1), reused 10 (delta 1)
        > Unpacking objects: 100% (10/10), done.
```

## Create a Virtual Environment using anaconda
Easiest way to create a virtual environment in anaconda is using the ***Anaconda Navigator***
```
1.  Go to windows search (win+s) > search anaconda navigator > Open
2.  In Anaconda Navigator - Go to Environments (under home)
3.  Default environment is base(root). 
4.  Click the create option below.
5.  Just enter a environment name you wish (ex: live), wait a minute, click on create.
6.  Done. You can close the Anaconda Navigator now.
```

## Activate the anaconda virtual environment
Open the windows command prompt by searching in windoes search (or) Press "win+R", type cmd, hit enter... And there you gooo...
```
> activate virtual-env-name
ex:> activate live
```
 
## Check whether your pip version is up-to-date
See the pip-list.txt file to check all the package versions, which i have installed for my project.
```python
(live) C:\Users\LvlyPavi>pip --version
pip 20.3.3 from D:\Users\LvlyPavi\anaconda3\envs\live\lib\site-packages\pip (python 3.8)
```

## Install all the required packages in the anaconda virtual environment
1.  Firstly, Navigate to the github cloned repository folder. 
    Ex:
    ```
    > s:
    > cd projects/liveness detection
    ```
2.  Install the requirements.txt file, which is already inside the folder. (Check the pip-list.txt file, and install the particular version incase you face any error.)
    ```
    > pip install -r requirements.txt
    > pipwin install pyaudio
    ```
    PyAudio module gives us trouble if we try installing it through the traditional "pip install pyaudio" way. So, just install pyaudio and portaudio using this command: "pipwin     install pyaudio"
    
3.  **Crucial Information** : Dlib module also gives us lot of trouble when installing it in windows. Hence, we use anaconda environment to get this module correctly.
    Follow the procedure below:
    ```
    > conda update anaconda
    > conda install -c conda-forge dlib
    ```
4.  What??? Do you need more modules?? 
    Congrats !!! On successful installation of all the requirements !!! Don't stop right here. Go ahead to complete our project.
  
## Input to our Liveness Authenticator
```
You will need to take 2 videos of yourself as an input i.e., to make our dataset.

videos is our input folder which we are going to give to the model to train it.

1.  Create a video of yourself, walking around your space for 20-30 seconds. 
    Store it inside videos folder with a name real.mp4.

2.  Then, hold the real.mp4 video against your laptop/computer's camera.
    Tip: Do not show your real face to the camera for best results.
    Record another video in the above manner. Save it in this same folder with a name fake.mp4
```

## Building OUR "Dataset"
As of now, we already have 2 input videos for training. Let's go ahead and extract images from the input videos we have in the videos folder.
Make sure you have already navigated to the folder where you have the project files.
```
Let's divide the extraction process into 2 steps (real and fake) :

1.  Fake images extraction:
    > python gather_examples.py --input videos/fake.mp4 --output dataset/fake --detector face_detector --skip 1
    
    Your fake images extraction process will begin when you hit enter. 
    Make sure you have a folder named dataset which inturn contains a folder named fake (orelse you may face errors). 
    Wait for the process to complete. Check your "dataset/fake/" folder for images.
    
2.  Real images extraction:
    > python gather_examples.py --input videos/real.mp4 --output dataset/real --detector face_detector --skip 4
    
    Wait for the process to complete. Check your "dataset/real/" folder for images.
```

## Extracting graph and training accuracy (plot.png) :
The training history plot shows accuracy and loss curves so we can assess our model (i.e. over/underfitting). We will train our network for 50 epochs.
```
> python train.py --dataset dataset --model liveness.model --le le.pickle
```
After running the above code, look for plot.png in the same folder of the project. You can find a graphical represetation of the training accuracy, training loss, accuracy and loss computed on the validation set etc., 
As of my results show, I'm able to obtain 100% liveness detection accuracy on the validation set with limited overfitting!

## Finally, running our code
```
> python liveness_main.py --model liveness.model --le le.pickle --detector face_detector
```
Hope you can see yourself after you hit enter!!!
