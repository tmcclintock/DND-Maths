"""
This contains a random fighter object, which is an object
that can be called to randomly generate a Pathfinder fighter.

TODO:
1. 
"""

import random
import sys #For the unit test
sys.path.insert(0,"../Stats/")
import Stats

class Random_Fighter(object):
    def __init__(self,level,name="",race="human",debug=False,seed=117401009):
        self.name = name
        self.level = level
        self.race = "human"
        self.raw_stats = Stats.Stats(debug,seed)
        return

    def __str__(self):
        return "%s \n\tLevel:%d"%(self.name,self.level)

    def set_attributes(self):
        self.bab = self.level
        self.number_of_feats = self.level+1
        self.roll_stats()
        self.number_of_skill_points = self.level*max(self.stat_mods['int'],1)
        if self.race == "human": 
            self.number_of_feats += 1
            self.number_of_skill_points += self.level
        self.calculate_saves()
        self.bravery = (self.level+2)/4
        self.armor_training = (self.level+1)/4
        self.weapon_training = (self.level-1)/4
        return

    def calculate_saves(self):
        saves = {}
        saves['fort'] = 2+self.level/2+self.stat_mods['con']
        saves['ref'] = self.level/3+self.stat_mods['dex']
        saves['will'] = self.level/3+self.stat_mods['wis']
        self.saves = saves
        return

    def roll_stats(self):
        self.raw_stats = self.raw_stats.roll_four_drop_lowest()
        rs = self.raw_stats
        self.stats = {'str':rs[0],'dex':rs[1],'con':rs[2],\
                      'int':rs[3],'wis':rs[4],'cha':rs[5]}
        self.stat_mods = {}
        for s in self.stats:
            self.stat_mods[s] = (self.stats[s]-10)/2
        return

#A unit test
if __name__ == '__main__':
    rftest = Random_Fighter(level=3,name="Random Fighter Bro")
    print rftest
    rftest.set_attributes()
    print rftest.stats
    print rftest.saves
