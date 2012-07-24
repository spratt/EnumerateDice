#!/usr/bin/env python2.6

# constants
NUM_DICE=4
DICE_SIDES=6

# variables
val=1
d=[]

# initialize dice
for i in range(1,NUM_DICE):
    d.append(val)

# enumerate events
while val <= DICE_SIDES:
    print val
    val += 1
