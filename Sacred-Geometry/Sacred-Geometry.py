"""
This contains a sacred geometry object, which is a tool used to solve the sacred geometry
problem layed out here:

http://www.d20pfsrd.com/feats/general-feats/sacred-geometry

That is, roll some number of 6-sided dice, and then figure out mathematical 
combinations of the results in order to reach some specific number.

This problem is actually tricky from a design standpoint since we have
to pick a practical way to stopre a mathematica operator and then get it back.

This is somewhat alleviated by the operator package, which has
functional calls to apply operators. The tricky part is deciding how
to show the result to the user, and I haven't thought yet about how
to try different combinations of parenthesis.

Once a set of rolls has been generated, the algorithm is as follows:
1. TODO
"""

import operator
import random
import sys #For the unit test

class Sacred_geometry(object):
    def __init__(self,level,name="",rolls=[],debug=False,seed=117401009):
        self.name = name
        self.level = level
        self.rolls = rolls
        random.seed(seed)
        if not self.rolls:
            self.roll_dice(self.level)
        self.solved=self.solve()

    def __str__(self):
        return "Sacred Geometry %s:\n\tSolved: %r\n\tLevel: %d\n\tRolls: %s"\
            %(self.name,self.solved,self.level,self.rolls)

    """
    This function rolls level number of dice
    to populate the rolls list.
    """
    def roll_dice(self,level):
        for i in range(level):
            self.rolls.append(random.randint(1,6))
        return

    """
    This is the function that gets called
    in order to do the solve.
    """
    def solve(self):
        return False

#A unit test
if __name__ == '__main__':
    sgtest = Sacred_geometry(3,name="test")
    print sgtest
