# LivenessAuthentication

 Liveness Authentication, an anti-spoofing liveness detection mechanism distinguishes live person in front of camera from spoofing attacks such as photos, videos or masks also fraud prevention for face detection in general. If the user is un-authorized, the device gets locked and a mail is initiated which includes a snapshot, location, computer name and ip-address of the Intruder. Liveness Authenticator helps you in securing your device in most possible ways.
 
 <span style="display:block;text-align:center">![Liveness Detecion](https://fcw.com/-/media/GIG/EDIT_SHARED/Identity/facialrecogalgorithm.jpg)</span>
 
 ## Pre-requisites and download links
 
 Python - https://www.python.org/downloads/ \
 PIP \
 Anaconda - https://www.anaconda.com/products/individual#Downloads \
 
 
 ## Check whether your pip version is up-to-date
 See the pip-list.txt file to check all the package versions, which i have installed for my project.
```python
(live) C:\Users\LvlyPavi>pip --version
pip 20.3.3 from D:\Users\LvlyPavi\anaconda3\envs\live\lib\site-packages\pip (python 3.8)
```

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

2.  Then, hold the real.mp4 folder against your laptop/computer's camera (do not show your real face to cam for best results)
    Record another video in the above manner. Save it in this same folder with a name fake.mp4
```

## Building OUR ""Dataset""
```
As of now, we already have 2 input videos for training. Let's go ahead and extract images from the input videos we have in the videos folder.
Make sure you have already navigated to the folder where you have the project files.
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
