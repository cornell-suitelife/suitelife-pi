import time

# Attempt to import the Raspi GPIO module
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Failed to import RPi.GPIO!")

# Some global variables
HB_1 = 11
HB_2 = 13
HB_1_pwm = 0
HB_2_pwm = 0

# Call before attempting to interact with electronics
# Initializes pin directions and GPIO pin mappings
def init():
    global HB_1_pwm
    global HB_2_pwm
    GPIO.setmode(GPIO.BOARD) #BOARD or BCM
    GPIO.setup( [ HB_1, HB_2 ], GPIO.OUT)
    HB_1_pwm = GPIO.PWM(HB_1, 200)
    HB_1_pwm.start(0)
    HB_2_pwm = GPIO.PWM(HB_2, 200)
    HB_2_pwm.start(0)

# Call upon program termination, cleans up GPIO pin states
def cleanup():
    HB_1_pwm.ChangeDutyCycle(0)
    HB_2_pwm.ChangeDutyCycle(0)
    HB_1_pwm.stop()
    HB_2_pwm.stop()
    
    GPIO.output(HB_1, 0)
    GPIO.output(HB_2, 0)
    GPIO.cleanup( [HB_1, HB_2] )

# Spin the motor - speed [-255, 255]
def spin_motor( speed ):
    if (speed < -255 or speed > 255):
        raise ValueError("Motor desires must be in [-255, 255]! Got: " + speed)
    if (speed > 0):
        HB_1_pwm.ChangeDutyCycle(speed /  2.55)
        HB_2_pwm.ChangeDutyCycle(0)
    elif (speed < 0):
        HB_1_pwm.ChangeDutyCycle(0)
        HB_2_pwm.ChangeDutyCycle(-speed /  2.55)
    else:
        HB_1_pwm.ChangeDutyCycle(0)
        HB_2_pwm.ChangeDutyCycle(0)

# Open the door - hold open for [time] seconds
def open( time_open ):
    # Open the door
    spin_motor(200)
    time.sleep(3)

    # Hold the door open for specified amount of time
    spin_motor(50)
    time.sleep(time_open)

    #Let the handle fall back down
    spin_motor(-50)
    time.sleep(1)

    #Stop Motor
    spin_motor(0)

# Test code
init()
open(2)
cleanup()
