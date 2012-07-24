#!/usr/bin/env python2.6

import sys

# defaults
NUM_DICE=4
DICE_SIDES=6

# parameters
if len(sys.argv) > 1:
    NUM_DICE=int(sys.argv[1])
if len(sys.argv) > 2:
    DICE_SIDES=int(sys.argv[2])
 
# utility functions
def print_dice(dice):
    for die in dice:
        print str(die)+'\t',
    print

def enumerate_dice(n):
    if n==1:
        return [[i] for i in range(1,DICE_SIDES+1)]
    sublist=enumerate_dice(n-1)
    return [l+[i] for l in sublist for i in range(1,DICE_SIDES+1)]

# enumerate!!
for dice in enumerate_dice(NUM_DICE):
    print_dice(dice)

