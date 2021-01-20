# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import pyautogui
import imutils
import pickle
import time
import cv2
import pyttsx3 
import speech_recognition as sr 
import winshell 
import ctypes
import threading
import math
import logging
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #ignores tensorflow unnecessary information
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import warnings
warnings.filterwarnings('ignore') #ignores anaconda prompt warnings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application
import socket 
import requests
import json

#disabling tf errors
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
# print(voices[1].id)  #prints the voice info and name of the voice (zira)
engine.setProperty('voice', voices[1].id) 

un_authorized_tomail = True
authorized = True

#speach function
def speak(audio): 
    print('Assistant: ' +audio)
    engine.say(audio) 
    engine.runAndWait()

# Create and configure logging
logging.basicConfig(filename='AuthenticationInfo.log',
                            filemode='a',
                            format='(%(asctime)s) %(msecs)d--%(name)s--%(levelname)s : %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, required=True,
	help="path to trained model")
ap.add_argument("-l", "--le", type=str, required=True,
	help="path to label encoder")
ap.add_argument("-d", "--detector", type=str, required=True,
	help="path to OpenCV's deep learning face detector")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
print(' ')
speak('Hello, I am a Liveness Authenticator. Please let me detect whether you are an authorized user.')
print(' ')

# This Function will clean any command before execution of this python file 
# load our serialized face detector from disk
logging.debug('Debugging Process Initiated...')
print("[..INFO..] Loading face detector... \n")
protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
modelPath = os.path.sep.join([args["detector"],
	"res10_300x300_ssd_iter_140000.caffemodel"])
net = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load the liveness detector model and label encoder from disk
print("[..INFO..] Loading liveness detector... \n")
model = load_model(args["model"])
le = pickle.loads(open(args["le"], "rb").read())

# initialize the video stream and allow the camera sensor to warmup
print("[..INFO..] Starting video stream... \n")
vs = VideoStream(src=0).start()

#initializing location settings
send_url = "http://api.ipstack.com/access_key--here"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
s.login('sender-email', 'sender-password') #update these details

hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname) 

msg = MIMEMultipart()
msg['Subject'] = 'Unauthorized ACCESS!!!'
msg['From'] = 'sender-email'
msg['To'] = 'reciever-email'
txt = MIMEText('''
This is to inform that, Your device has an un-authorized user!
Information about the Unauthorized User:
			The Intruder's Computer name : ''' + hostname + '''
			The Intruder's IP Address is : ''' + IPAddr + '''
			The Intruder's Latitude : ''' + str(latitude) + '''
			The Intruder's Longitude : ''' + str(longitude) + '''
			
Please check your device and ensure it is safe.
											
With regards,
Your Liveness Detector.''')
msg.attach(txt)

frame = vs.read()
frame = imutils.resize(frame, width=1860)
cv2.imshow("Frame", frame)
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to have a maximum width of 600 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=600)
	# grab the frame dimensions and convert it to a blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
	# pass the blob through the network and obtain the detections and predictions
	net.setInput(blob)
	detections = net.forward()
    	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the prediction
		confidence = detections[0, 0, i, 2]
		# filter out weak detections
		if confidence > args["confidence"]:
			# compute the (x, y)-coordinates of the bounding box for the face and extract the face ROI
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			# ensure the detected bounding box does fall outside the dimensions of the frame
			startX = max(0, startX)
			startY = max(0, startY)
			endX = min(w, endX)
			endY = min(h, endY)
			# extract the face ROI and then preproces it in the exact same manner as our training data
			try :
				face = frame[startY:endY, startX:endX]
				face = cv2.resize(face, (32, 32))
				face = face.astype("float") / 255.0
				face = img_to_array(face)
				face = np.expand_dims(face, axis=0)
				# pass the face ROI through the trained liveness detector
				# model to determine if the face is "real" or "fake"
				preds = model.predict(face)[0]
				j = np.argmax(preds)
				label = le.classes_[j]
				# draw the label and bounding box on the frame
				if(le.classes_[j]=='fake'):
					label = 'Unauthorized'
					label = "{}: {:.4f}".format(label, preds[j])
					cv2.putText(frame, label, (startX, startY - 10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
					cv2.rectangle(frame, (startX, startY), (endX, endY),
						(0, 0, 255), 2)
					if(un_authorized_tomail==True):		
						logging.info("The user is Un-authorized")			
						speak('I am sorry, you seem to be an unauthorized user. I cannot give you access...')
						pyautogui.screenshot("./IntruderAlert.png")
						filename = 'IntruderAlert.png' #path to file
						fo=open(filename,'rb')
						speak('Sending an email to the owner...')
						attach = email.mime.application.MIMEApplication(fo.read(),_subtype="png")
						fo.close()
						attach.add_header('Content-Disposition','attachment',filename=filename)
						msg.attach(attach)
						s.send_message(msg)
						s.quit()
						speak('Email sent...')
						un_authorized_tomail = False
						logging.critical('Email has been sent to the owner...')	
						#locking the device 	
						speak("Locking the device...")
						logging.critical("The Device was Locked")
						ctypes.windll.user32.LockWorkStation() 

				else:
					if(authorized==True):
						logging.info("The user is Authorized")
						speak('Thanks for your patience. You are an authorized user. Access Granted.')
						authorized=False
					label = 'Authorized'
					label = "{}: {:.4f}".format(label, preds[j])
					cv2.putText(frame, label, (startX, startY - 10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
					cv2.rectangle(frame, (startX, startY), (endX, endY),
						(0,255,0), 2)
			except :
				pass

    # show the output frame and wait for a key press
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()


