"""
This contains a random fighter object, which is an object
that can be called to randomly generate a Pathfinder fighter.

TODO:
1. 
"""

import random
import sys #For the unit test

class Random_Fighter(object):
    def __init__(self,level,name="",debug=False,seed=117401009):
        self.name = name
        self.level=level
        return
    def __str__(self):
        return "%s \n\tLevel:%d"%(self.name,self.level)

#A unit test
if __name__ == '__main__':
    rftest = Random_Fighter(level=3,name="Random Fighter Bro")
    print rftest
