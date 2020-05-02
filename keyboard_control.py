# run with python3
# run as adimin, 
# sudo python3  ....myfile.py

# from IPython.display import display
import time
from jetbot import Robot
#from IPython.display import display
#import ipywidgets
import traitlets
from jetbot import Camera, bgr8_to_jpeg
import keyboard
# import ipywidgets.widgets as widgets
robot = Robot()
robot.stop()



print("imports finished")

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
		time.sleep(step)
		robot.stop()
finally:
	robot.stop()
	print("stop on finally")
print("all done")
