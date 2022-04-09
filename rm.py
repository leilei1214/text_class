import RPi.GPIO as GPIO
import time
pinRelay = 17
pin1 = 7

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinRelay,GPIO.OUT)
n=1
def event(pin):
	global n
	GPIO.remove_event_detect(pin)
	print('按了{}'.format(n))
	n +=1
	GPIO.output(pinRelay,not GPIO.inpue(pin1))
	GPIO.add_event_detect(pin,GPIO.FALLING,callback =event,bouncetime=1500)
try:
	GPIO.add_event_detect(pin1,GPIO.FALLING,callback =event,bouncetime=1500)
	while True:
		time.sleep(1000000)
except KeyboardInterrupt:
	pass
except Exception as err:
	print(err)
GPIO.cleanup()
