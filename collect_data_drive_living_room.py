# run with python3
# run as adimin, 
# sudo python3  ....myfile.py
print(f'staring {__name__}')


import time
from jetbot import Robot, Camera
import keyboard
import numpy as np
import cv2
from pathlib import Path
import pandas as pd
print("imports finished")

# https://www.scivision.co/numpy-image-bgr-to-rgb/
def convert_bgr_to_rgb(x): return x[...,::-1]

def make_images_dir():
    p = "images"
    p = Path(p)
    p.mkdir(exist_ok=True); print("made images dir")
    return p

def start_camera():
    c = Camera()
    c.fps = 2
    c.start(); print("Camera started")
    return c

def start_robot():
    robot = Robot()
    robot.stop(); "robot control started"
    return robot


def CreateDFWithAttBasedOnObjs(listOfObjects, attributesToSave):
	"""Creates a dataframe by extracting the attributes from the objects in the list of objects"""
	df = pd.DataFrame()
	for a in attributesToSave:      
		a_values = [getattr(t,a) for t in listOfObjects]
		df[a]=a_values
	return df  


def CreateDictionaryWithAttBasedOnObjs(listOfObjects, attributesToSave): 
    df = dict()
    for a in attributesToSave:      
        a_values = [getattr(t,a) for t in listOfObjects]
        df[a]=a_values
    return df  

def save_img(obj, img): cv2.imwrite(obj.name,img)





class img_and_dir:
    counter = 0
    dataList = []
    
    def __init__(self, direction):      
        self.direction = direction
        
    def get_image_name(self, counter):
        self.counter = counter
        self.name = str(p / f"drive{counter}.png")
        return self.name    
    
    @classmethod
    def make_and_save(cls, direction):
        data = cls(direction) # make a new object of this class
        data.get_image_name( img_and_dir.counter) # make the save img name
        img = convert_bgr_to_rgb(c.value).astype('uint8') # get the image
       
        save_img(data, img) # save the image
        img_and_dir.dataList.append(data) # save the object to the static list
        img_and_dir.counter+=1 # increment the counter. 
#         return data

def getmax_image_number(p):
    images = list(p.glob("*.png"))
    def getnumber(imgpath):
        substring = imgpath.name[5:-4]
        return int(substring)
    img_numbers = [getnumber(i) for i in images]
    last = max(img_numbers)
    return last  

if __name__ == "__main__":
    p = make_images_dir()
    c = start_camera()
    robot = start_robot()
    # start where previous ones stopped
    img_and_dir.counter = getmax_image_number(p)+1

    power = 0.95
    step = 0.2
    print("starting loop")

    try:
        while True:
            key =  keyboard.read_key()
            print(f"key value is {key}")
            if key == "up":			
                robot.forward(power)
                print("forward")
            if key == "right":			
                robot.right(power)
                print("right")
            if key == "left":
                robot.left(power)
                print("left")
            if key == "down":
                robot.backward(power)
                print("backward")
            if key == "q":
                robot.stop()
                print('q pressed. breaking')
                break
            if key == "r":
                robot.stop()
            if key!='q':
                time.sleep(step)
                robot.stop()
                # make sure you sleep and stop the robot before trying to 
                # process the data. Otherwise this might take too long. 
                img_and_dir.make_and_save(key)
    finally:
        robot.stop()
        attributesToSave = ['name', 'counter','direction']
        df =  CreateDFWithAttBasedOnObjs(img_and_dir.dataList, attributesToSave)
        csvfiles = list(p.glob("*.csv"))
        num = len(csvfiles)+1
        name = f'images/drivedata{num}.csv'
        df.to_csv(name)
        print(f"Saving csv file as {name}")
        c.stop()
        del c
        print("stop on finally")
        del robot
    print("all done")
