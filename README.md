# LivenessAuthentication

 Liveness Authentication, an anti-spoofing liveness detection mechanism distinguishes live person in front of camera from spoofing attacks such as photos, videos or masks also fraud prevention for face detection in general. If the user is un-authorized, the device gets locked and a mail is initiated which includes a snapshot, location, computer name and ip-address of the Intruder. Liveness Authenticator helps you in securing your device in most possible ways.
 
                               ![Liveness Detecion](https://www.idrnd.ai/wp-content/uploads/2019/08/facespoofing-blog-pic-e1565002975396.png)
 
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
activate virtual-env-name
ex: activate live
```

## Install all the required packages in the anaconda virtual environment
1.  Firstly, Navigate to the github cloned repository folder. 
    Ex:
    ```
    s:
    cd projects/liveness detection
    ```
2.  Install the requirements.txt file, which is already inside the folder. (Check the pip-list.txt file, and install the particular version incase you face any error.)
    ```
    pip install -r requirements.txt
    pipwin install pyaudio
    ```
    PyAudio module gives us trouble if we try installing it through the traditional "pip install pyaudio" way. So, just install pyaudio and portaudio using this command: "pipwin     install pyaudio"
3.  **Crucial Information** : Dlib module also gives us lot of trouble when installing it in windows. Hence, we use anaconda environment to get this module correctly.
    Follow the procedure below:
    ```
    conda update anaconda
    conda install -c conda-forge dlib
    ```
4.  What??? Do you need more modules?? 
    Congrats !!! On successful installation of all the requirements !!! Don't stop right here. Go ahead to complete our project.
  
