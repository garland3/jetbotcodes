# follow the red light
# sudo python3 red_follower.py
# based on the 02B notebook
from jetbot import Camera,bgr8_to_jpeg, Robot
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
# from PIL import Image
from exp.nb_02 import convert_bgr_to_rgb
from exp.nb_02B import *
from pathlib import Path
import keyboard  # using module keyboard

print("imports finished")

def start_camera():
    c = Camera()
    c.fps = 2
    c.start(); print("Camera started")
    return c

def start_robot():
    robot = Robot()
    robot.stop(); "robot control started"
    return robot

c = start_camera()
robot = start_robot()
power = 1.0

def step():
    img = convert_bgr_to_rgb(c.value)
    middle_avg, middles, y  = get_middle_red(img)    
    steer_norm = normalize(middle_avg)   
    steer_robot(steer_norm, robot=robot, power = power)
    time.sleep(0.2)

# ------------------------
# Wait to start till up arrow is pressed. 
# ------------------------
print('waiting for up arrow from wirelss key board')
while True:
    key =  keyboard.read_key()
    if key == 'up': break
        
# ------------------------
# Start following the light, but stop if q is pressed
# ------------------------
# https://stackoverflow.com/questions/24072790/detect-key-press-in-python
try:
    paused = False
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
            if keyboard.is_pressed('p'):  # if key 'q' is pressed 
                print("P pressed")
                paused = ~paused
        except:
            break  # if user pressed a key other than the given key the loop will break

        if paused: continue
        step()
finally:
    print("-----"*20)
    print("Stopping     "*5)
    robot.stop()
    c.stop()
#     del c
#     del robot