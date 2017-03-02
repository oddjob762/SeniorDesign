import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

s0 = 23
s1 = 24

GPIO.setup(s0,GPIO.OUT)
GPIO.setup(s1,GPIO.OUT)

def Reset():
	GPIO.output(s0,GPIO.LOW)
	GPIO.output(s1,GPIO.LOW)

def SelectCam(cam):
	if cam == 1:
		GPIO.output(s0,GPIO.HIGH)
	elif cam == 3:
		GPIO.output(s1,GPIO.HIGH)
		GPIO.output(s0,GPIO.HIGH)
	elif cam == 2:
		GPIO.output(s1,GPIO.HIGH)
	else:
		continue
	time.sleep(5)
	Reset()


option = True

while option:
	camera = input('Select camera 1-4')
	if camera == None:
		option = False
	try:
		camera = int(camera)-1
	except:
		camera = 0
	SelectCam(camera)


print('Exiting now')

time.sleep(5)