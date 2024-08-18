from deepface import DeepFace
import cv2
import RPi.GPIO as GPIO
import os
from time import sleep
from os import path
from numpy import asarray
from pathlib import Path

# Some definitions for LED's,Buzzer and the solenoid lock
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Assigning pin numbers for all hardware
# For the Button
button_pin = 6
 
# For all the indicator led's '
led_red = 14
led_green = 15
led_yellow = 18

# For the buzzer
buzzer_pin = 26

# For the solenoid's relay
solenoid_pin = 2

# Set all the pins of the hardware as output

# For all the led's'
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)

# For the buzzer
GPIO.setup(buzzer_pin, GPIO.OUT)

# For the solenoid's relay
GPIO.setup(solenoid_pin, GPIO.OUT)

# For Button
GPIO.setup(button_pin,GPIO.IN)

# Define base path using Path.cwd()
base_path = Path.cwd()

"""
Section for taking image and handling the creation of tmp_live_image folder
where the live image of the person is stored
"""


def takeimage():
            # Creating a video capture object to read the frames below
            video_capture = cv2.VideoCapture(0)
            video_capture.set(cv2.CAP_PROP_FRAME_WIDTH,2048)
            video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
            ret, frame = video_capture.read()
            # Convert the image from BGR color (which OpenCV uses by default) to RGB color
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Use f-string and Path.cwd() for image path
            cv2.imwrite(filename=f'{base_path}/tmp_live_image/tmp_pic.jpg', img=rgb_frame)
            video_capture.release()


def Imagefileops(operation):
            if operation == 1:
                  # Use f-string and Path.cwd() for directory path
                  if path.exists(f'{base_path}/tmp_live_image') == False:
                        os.system(f'mkdir {base_path}/tmp_live_image')
            elif operation == 0:
                  # Use f-string and Path.cwd() for directory path
                  if path.exists(f'{base_path}/tmp_live_image') == True:
                        os.system(f'rm -rf {base_path}/tmp_live_image')



# converting the list to array to save memory
tmp_name_list = os.listdir(f"{base_path}/samples")
final_converted_array = asarray(tmp_name_list)
del tmp_name_list



#Here we use this loop to copy all the images from the USB drive to the local drive because the access time is very slow 

while True:          #checking if the USB has the folder or not
        if path.exists('/mnt/usb/face-recognition-project/samples') == False:
               continue
               
        else:       #If it exists only then the samples will be copied
               os.system(f'rm -rf {base_path}/samples')
               os.system(f'cp -r /mnt/usb/face-recognition-project/samples {base_path}')
               break



while True:
       GPIO.output(solenoid_pin,1)
       if GPIO.input(6) == True:
            GPIO.output(led_yellow,True)
        
            # Here we are creating the directory tmp_live_image before taking the image of the person 
            Imagefileops(1)
            takeimage()
            GPIO.output(led_yellow,False)
            final_result = False
            
            '''
            Here the names are  being iterated through so that it can be compared with the database of images that have been
            copied from the USB drive after the comparison the solenoid lock and the corresponding LEDs are turned ON  
            '''

            for name in final_converted_array:
                  result = DeepFace.verify(img1_path = f"{base_path}/tmp_live_image/tmp_pic.jpg",img2_path=f"{base_path}/samples/{name}",distance_metric='euclidean_l2',model_name = 'Facenet512',detector_backend = 'opencv',enforce_detection= False)
                  if result['verified'] == True:
                        final_result = True
                        del result
                        break
                  else:
                        continue

            if final_result == True:
                        print('Face found')
                        GPIO.output(led_green,True)
                        GPIO.output(solenoid_pin,0) #solenoid on
                        sleep(1)
                        GPIO.output(buzzer_pin,1)
                        sleep(1)
                        GPIO.output(buzzer_pin,0)
                        sleep(10) 
                        GPIO.output(led_green,False)
                        GPIO.output(solenoid_pin,1) #solenoid off
                        Imagefileops(0)
            else:
                  print("face not found")
                  Imagefileops(0)
                  GPIO.output(led_red,True)
                  sleep(1)
                  GPIO.output(led_red,False)
       else:
            continue