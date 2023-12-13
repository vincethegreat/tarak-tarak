from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 9
pinMotorABackwards = 10
pinMotorBForwards = 8
pinMotorBBackwards = 7

pinMotorCForwards = 22
pinMotorCBackwards = 23
pinMotorDForwards = 24
pinMotorDBackwards = 25
pinWaterPump = 26 

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 60
DutyCycleB = 60
DutyCycleC = 60
DutyCycleD = 60

# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

GPIO.setup(pinMotorCForwards, GPIO.OUT)
GPIO.setup(pinMotorCBackwards, GPIO.OUT)
GPIO.setup(pinMotorDForwards, GPIO.OUT)
GPIO.setup(pinMotorDBackwards, GPIO.OUT)

GPIO.setup(pinWaterPump, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

pwmMotorCForwards = GPIO.PWM(pinMotorCForwards, Frequency)
pwmMotorCBackwards = GPIO.PWM(pinMotorCBackwards, Frequency)
pwmMotorDForwards = GPIO.PWM(pinMotorDForwards, Frequency)
pwmMotorDBackwards = GPIO.PWM(pinMotorDBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e., not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

pwmMotorCForwards.start(Stop)
pwmMotorCBackwards.start(Stop)
pwmMotorDForwards.start(Stop)
pwmMotorDBackwards.start(Stop)

# Turn off all motors
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

    pwmMotorCForwards.ChangeDutyCycle(Stop)
    pwmMotorCBackwards.ChangeDutyCycle(Stop)
    pwmMotorDForwards.ChangeDutyCycle(Stop)
    pwmMotorDBackwards.ChangeDutyCycle(Stop)

# Turn all motors forwards
def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

    pwmMotorCForwards.ChangeDutyCycle(DutyCycleC)
    pwmMotorCBackwards.ChangeDutyCycle(Stop)
    pwmMotorDForwards.ChangeDutyCycle(DutyCycleD)
    pwmMotorDBackwards.ChangeDutyCycle(Stop)

# Turn all motors backwards
def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

    pwmMotorCForwards.ChangeDutyCycle(Stop)
    pwmMotorCBackwards.ChangeDutyCycle(DutyCycleC)
    pwmMotorDForwards.ChangeDutyCycle(Stop)
    pwmMotorDBackwards.ChangeDutyCycle(DutyCycleD)

# Turn right
def Right():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

    pwmMotorCForwards.ChangeDutyCycle(Stop)
    pwmMotorCBackwards.ChangeDutyCycle(DutyCycleC)
    pwmMotorDForwards.ChangeDutyCycle(DutyCycleD)
    pwmMotorDBackwards.ChangeDutyCycle(Stop)

# Turn left
def Left():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

    pwmMotorCForwards.ChangeDutyCycle(DutyCycleC)
    pwmMotorCBackwards.ChangeDutyCycle(Stop)
    pwmMotorDForwards.ChangeDutyCycle(Stop)
    pwmMotorDBackwards.ChangeDutyCycle(DutyCycleD)
    

def WaterPlants():
    # Activate the water pump (Assuming water pump is activated with motor controls)
    Forwards()  # Assuming your Forwards() function controls the water pump
    time.sleep(2)  # Adjust the sleep time as needed
    StopMotors()  # Stop the water pump



app = Flask(__name__)

@app.route('/')
def index():
    message = "ahhhhhhh"
    return render_template('index.html', message=message)

@app.route("/forward/", methods=['POST'])
def move_forward():
    # Moving forward code
    Forwards()
    time.sleep(.5)

    StopMotors()

    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=forward_message);

@app.route("/back/", methods=['POST'])
def move_back():
    # Moving forward code
    Backwards()
    time.sleep(.5)
    StopMotors()

    forward_message = "Moving Backwards..."
    return render_template('index.html', forward_message=forward_message);

@app.route("/right/", methods=['POST'])
def move_right():
    # Moving forward code
    Right()
    time.sleep(.5)
    StopMotors()

    forward_message = "Moving right..."
    return render_template('index.html', forward_message=forward_message);

@app.route("/left/", methods=['POST'])
def move_left():
    # Moving forward code
    Left()
    time.sleep(.5)
    StopMotors()

    forward_message = "Moving left..."
    return render_template('index.html', forward_message=forward_message);
    
    
@app.route('/water_plants/', methods=['POST'])
def water_plants():
    WaterPlants()
    return "Watering Plants..."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
