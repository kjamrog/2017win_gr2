###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

import random
import time

def getRandomOrientation():
    return random.gauss(0, 20)

print('Simulating turbulations.\nPress Ctrl^C to break\n')

class Correction(object):
    def __init__(self):
        self.start_orientation = random.gauss(0, 10)
        print('Start orientation: ' + str(self.start_orientation))
        self.current_orientation = self.start_orientation
    
    # Setting correction to keep initial orientation
    def updateCorrection(self, turbulence):
        correction = -turbulence
        # Prevent to set correction greater than 6 or lower than -6
        if correction > 6:
            correction = 6
        elif correction < -6:
            correction = -6
        self.current_orientation = self.start_orientation + turbulence + correction
        print('correction ' + str(correction))

    def printActual(self):
        print('Actual orientation: ' + str(self.current_orientation))


correction = Correction()

while True:
    try:
        turbulence = random.gauss(0, 5)
        correction.updateCorrection(turbulence)
        correction.printActual()
        time.sleep(1)
    except KeyboardInterrupt:
        print('Simulation ended')
        break