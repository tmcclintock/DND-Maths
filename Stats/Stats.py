"""
This contains the Stats object, which has functions
to allow for generation of character stats. This
includes rolling 3 dice, rolling 4 dice and 
dropping the lowest, a default stat array,
and rerolling ones.
"""

import random

class Stats(object):
    def __init__(self,debug=False,seed=117401009):
        random.seed(seed)
        return

    """
    Default stat array.
    Equivalent to 22 point buy.
    """
    def default_stats(self):
        return [15,14,14,13,12,10]

    """
    Roll three.
    If no rerolls then the average point buy is near 0.
    If rerolls then the average point buy is near 6.
    """
    def roll_three(self,reroll=False):
        N_stats = 6
        N_rolls = 3
        stat_array = []
        for i in range(N_stats):
            roll_array = []
            j = 0
            while j<N_rolls:
                roll_array.append(random.randint(1,6))
                if reroll and roll_array[j] == 1:
                    roll_array.pop(j)
                    j-=1
                j+=1
            stat_array.append(sum(roll_array))
        return stat_array

    """
    Roll four drop lowest.
    If no rerolls then the average point buy is near X.
    If rerolls then the average point buy is near Y.
    """
    def roll_four_drop_lowest(self,reroll=False):
        N_stats = 6
        N_rolls = 4
        stat_array = []
        for i in range(N_stats):
            roll_array = []
            j = 0
            while j<N_rolls:
                roll_array.append(random.randint(1,6))
                if reroll and roll_array[j] == 1:
                    roll_array.pop(j)
                    j-=1
                j+=1
            roll_array.remove(min(roll_array))
            stat_array.append(sum(roll_array))
        return stat_array

if __name__ == "__main__":
    test_stats = Stats()
    print test_stats.default_stats()
    print test_stats.roll_three()
    print test_stats.roll_four_drop_lowest()
