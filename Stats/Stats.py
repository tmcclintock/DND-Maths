"""
This contains the Stats object, which has functions
to allow for generation of character stats. This
includes rolling 3 dice, rolling 4 dice and 
dropping the lowest, a default stat array,
and rerolling ones.
"""

import random
import math

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
    If no rerolls then the average point buy is near 5.
    If rerolls then the average point buy is near 16,
    but skewed heavily to lower numbers with a peak closer to 14.
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
    If no rerolls then the average point buy is near 20,
    with a skew to lower numbers and a peak near 19.
    If rerolls then the average point buy is near 30,
    with a skew to lower numbers and a peak near 28.
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

    """
    This function returns the point buy
    value of an inputted stat array.
    """
    def pb_value(self,stat_array):
        total = 0
        for stat in stat_array:
            diff = stat-10 #Difference between the stat and 10
            if diff == 0:
                sign = 1
            else:
                sign = diff/math.fabs(diff) #Sign of the difference
            total+=sign*(2*diff**2+7+(-1)**diff)/8 #The formula
        return total

if __name__ == "__main__":
    test_stats = Stats()
    print test_stats.default_stats()
    print test_stats.roll_three()
    print test_stats.roll_four_drop_lowest()
    arr2 = test_stats.roll_four_drop_lowest()
    print arr2
    print test_stats.pb_value(arr2)
