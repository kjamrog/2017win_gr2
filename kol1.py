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


class TurbulenceGenerator(object):
    def __init__(self, sigma):
        self.sigma = sigma
        self.turbulence = 0.0

    def generate(self):
        self.turbulence = random.gauss(0, self.sigma)

    def get_current(self):
        return self.turbulence

    def generate_and_return(self):
        self.generate()
        return self.get_current()


class Correction(object):
    def __init__(self, max_correction, start_orientation_sigma):
        self.start_orientation = random.gauss(0, start_orientation_sigma)
        self.current_orientation = self.start_orientation
        self.correction = 0.0
        self.max_correction = max_correction

    def generate_correction(self, turbulence):
        self.correction = -turbulence
        if self.correction > self.max_correction:
            self.correction = self.max_correction
        elif self.correction < -self.max_correction:
            self.correction = -self.max_correction

    def correct_orientation(self, turbulence):
        self.generate_correction(turbulence)
        self.current_orientation = self.start_orientation + turbulence + self.correction

    def get_current_correction(self):
        return self.correction

    def get_current_orientation(self):
        return self.current_orientation


if __name__ == '__main__':
    print('Simulating turbulations.\nPress Ctrl^C to break\n')

    max_correction_value = 6
    turbulence_sigma = 5
    initial_orientation_sigma = 10
    correction = Correction(max_correction_value, initial_orientation_sigma)
    turbulence_generator = TurbulenceGenerator(turbulence_sigma)
    print('Start orientation: {}\n'.format(correction.start_orientation))

    while True:
        try:
            new_turbulence = turbulence_generator.generate_and_return()
            print('Turbulence {}'.format(new_turbulence))
            correction.correct_orientation(new_turbulence)
            print('Correction {}'.format(correction.get_current_correction()))
            print('Actual orientation: {}\n'.format(correction.get_current_orientation()))
            time.sleep(1)
        except KeyboardInterrupt:
            print('Simulation ended')
            break
