# SD
Alcotest with camera for cars


# Description:
On average, 30% of roadway fatalities were caused by alcohol-impaired drivers from 2004 to 2018. This statistic remains unchanged till now. To prevent drunk-drivers on roads, there are some alcotests that are used in cars. 
An ignition interlock device or breath alcohol ignition interlock device (IID or BAIID) is a breathalyzer for an individual's vehicle. It requires the driver to blow into a mouthpiece on the device before starting or continuing to operate the vehicle. If the resultant breath-alcohol concentration analyzed result is greater than the programmed blood alcohol concentration (which varies between countries), the device prevents the engine from being started. The interlock device is located inside the vehicle, near the driver’s seat, and is directly connected to the engine’s ignition system.
The problem appears if two people decided to travel by car and one of them is drunk, second one isn’t. If sober person passes alcotest, car engine starts working and then drunk person can easily drive the car. In this case alcotest isn’t 100% efficient, so I decided to create smarter system that can’t be cheated. I decided to add camera inside the car that watches to driver all the time and if driver is changed (someone else passed the test and someone else is trying to drive the car), or more than one person is detected, car engine stops working. 


# How it works: 
I used Arduino Uno board, MQ-3 Alcohol sensor and two led emitting diodes to create a prototype. There is emitting red light if MQ-3 Alcohol sensor detects more alcohol concentration that it is allowed, or if camera can’t detect at least one person, or if camera detects more than 1 person. There is a green light only if alcohol sensor doesn’t detect any alcohol and only one person is detected by camera. If two person tries to swap places, there will be some period of time when no-one will be detected by camera so red light will be activated and you need to pass alcotest once again. The logic is that once you passed the test and car engine started working, nothing should be changed, otherwise car engine stops working and you need to pass test again. Code for this is in main.py file, I wrote all logic there and I used pyfirmata library to control arduino with python code.

# How to run:
### Hardware:
#### Components:
Arduino Uno Board
Breadboard
Jumpers
MQ-3 Alcohol Sensor
Led Emitting Diode – Red
Led Emitting Diode – Green
Resistors

#### Schema for hardware:
<img width="514" alt="Screenshot 2022-11-12 at 23 49 24" src="https://user-images.githubusercontent.com/85623531/201519758-7e8f6dc9-844c-42f6-9c08-394356b44451.png">


### Software:
1)	You need to install [homebrew](https://phoenixnap.com/kb/install-homebrew-on-mac), [opencv](https://docs.opencv.org/4.x/d0/db2/tutorial_macos_install.html), [dlib](https://learnopencv.com/install-dlib-on-macos/). 
2)	You need to upload standardFirmata code on Arduino uno board.
3)	You can run main.py file. 
