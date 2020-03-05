# ------------------------------ #

# DIODE meas using SMU2450

# (D1N4001SMU2450MEAS01IV02)

# keyang  &  Dennis

# Created: 2020.3.4

# Last update/review: 2020.3.4

# ------------------------------ #


# ------------------------------ #

# PREAMBLE

# ------------------------------ #

import os  # OS communication

import sys  # System communication

import time  # Time module

import pyvisa as visa  # Instrument communication/control

import numpy as np

# import matplotlib as mtl
#
# import matplotlib.pyplot as plt

# ------------------------------ #

# GETTING ACCESS TO THE SMU 2450 #

# ------------------------------ #

rm = visa.ResourceManager();

instAddress = rm.list_resources();  # Instruments addresses

# IMPORTANT: Alwasy check the address of the instrument to be controlled

# In this script, the SMU2450 is on the last address in the list

print(instAddress);

smuAddress = instAddress[0];  # SMU2450 Address

print(smuAddress);

smu = rm.open_resource(smuAddress);  # Open SMU2450
# smu.timeout = 10000

# -------------------------------------- #

# TEXT TO BE DISPLAYED ON THE PYTHON GUI #

# -------------------------------------- #

from datetime import datetime  # To generate timestamps

timestamp = datetime.now();

print("\n--------------------------");

print("Measurement launched on ");

print(timestamp);

print("---------------------------");

# ------------------------------------ #

# TEXT TO BE DISPLAYED ON THE SMU 2450 #

# ------------------------------------ #

smu.write('display.changescreen(display.SCREEN_USER_SWIPE)');

smu.write('display.settext(display.TEXT1, "Test in process")');

smu.write('display.settext(display.TEXT2, "Do not disturb")');

# -------------------------------------------- #

# SWEEP: VOLTAGE SOURCE SWEEP, CURRENT MEASURE #

# -------------------------------------------- #

# START SWEEP  SIGNAL

# -------------------------------------------- #

smu.write('beeper.beep(0.15, 392)')

smu.write('beeper.beep(0.15, 392)')

smu.write('beeper.beep(0.15, 392)')

smu.write('beeper.beep(0.30, 311.13)')

# -------------------------------------------- #

# START SWEEP

# --vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv-- #

smu.write('reset()');  # reset the instrument


smu.write('smu.measure.func = smu.FUNC_DC_CURRENT');  # set the instrument to current measurement

smu.write('smu.measure.autorange = smu.ON');  # set the autorange

smu.write('smu.source.func = smu.FUNC_DC_VOLTAGE');  # set the voltage source

smu.write('smu.source.range = 20');  # set the source range to 20V

smu.write('smu.source.ilimit.level = 1');  # set current limit to 0.02

smu.write('smu.source.sweeplinear("RES", 0, 1, 101, 100E-3)');  # set the linear sweep

smu.write('trigger.model.initiate()');  # trigger (start) the sweep

smu.write('waitcomplete()');  # wait

# smu.write('printbuffer(1, 101, defbuffer1.sourcevalues, defbuffer1.readings)');

# --^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^-- #

# SWEEP COMPLETED

# -------------------------------------------- #

# SWEEP COMPLETED SIGNAL

# -------------------------------------------- #


smu.write('beeper.beep(0.15, 349.23)')

smu.write('beeper.beep(0.15, 349.23)')

smu.write('beeper.beep(0.15, 349.23)')

smu.write('beeper.beep(0.45, 293.66)')

# -------------------------------------------- #

# READING MEASURED VALUES FROM SMU2450

# -------------------------------------------- #
#Write the buffer
time.sleep(35)
measure = smu.query_ascii_values('printbuffer(1, 101, defbuffer1.readings)')
source = smu.query_ascii_values('printbuffer(1, 101, defbuffer1.sourcevalues)')
#---------------------------------------------#
#Save Data in Hashmap 
hash = {}
for i in range(0, len(source)):
    hash[source[i]] = measure[i]

np.save('D1N4001', hash)



