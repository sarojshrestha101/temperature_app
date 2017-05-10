import time
import os

def temp():
	tempInString = os.popen('vcgencmd measure_temp').read()
	parshing = tempInString[5:9]
	tempInFloat = float(parshing)
	return tempInFloat;

def Main():
	print(temp())

if __name__ == '__main__':
	Main()