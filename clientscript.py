#!/bin/env dls-python

''' Example Channel Access client script

This script is really only intended as a demonstration on how to get started
with using the DLS python modules.
'''

from pkg_resources import require
require('cothread==2.11')
require('h5py==2.2.0')

# Channel Access python functions: caget, caput and camonitor
# Documentation here: http://www.cs.diamond.ac.uk/docs/docshome/cothread/index.html
# and externally visible here: http://controls.diamond.ac.uk/downloads/python/cothread/2-11-beta/docs/html/index.html
import cothread
from cothread.catools import *

# Python bindings for the HDF5 library - to write/read HDF5 format files
import h5py

# get some motor PV variables

motor_readback_position = caget('XFZ39520:MOTOR1.RBV')
motor_demand_position = caget('XFZ39520:MOTOR1.VAL')
motor_velocity = caget('XFZ39520:MOTOR1.VELO')

# Get some other value
signal_value = caget('XFZ39520:SIGNAL')

# Set up a monitor callback function to record motor position moving
motor_positions = []
def monitor_callback( position ):
    motor_positions.append( position )
camonitor( 'XFZ39520:MOTOR1.RBV', monitor_callback )

# Drive the motor a bit - with a blocking function call to wait for completion
# and a 5 second timeout
new_demand_position = motor_readback_position + 10.0
print "Starting move to: %.3f" % new_demand_position
status = caput('XFZ39520:MOTOR1.VAL', new_demand_position, wait=True, timeout = 5.0)

print "Done moving, status = ", status.ok
print "Motor positions recorded: "
print motor_positions

