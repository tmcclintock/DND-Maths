"""
This contains a random fighter object, which is an object
that can be called to randomly generate a Pathfinder fighter.

TODO:
1. 
"""

import sys #For the unit test
sys.path.insert(0,"../Stats/")
import Stats
import Weapons

class Random_Fighter(object):
    def __init__(self,level,name="",race="Human",debug=False,seed=117401009):
        self.debug = debug
        self.seed = seed
        self.name = name
        self.level = level
        self.race = "human"
        self.raw_stats = Stats.Stats(debug,seed)
        self.attributes_set = False
        return

    def __str__(self):
        outstr = "%s:\tLevel %d %s Fighter\n"%(self.name,self.level,self.race)
        if self.attributes_set:
            outstr+= "Stats:\n"
            outstr+="\tstr %d\n"%self.stats['str']
            outstr+="\tdex %d\n"%self.stats['dex']
            outstr+="\tcon %d\n"%self.stats['con']
            outstr+="\tint %d\n"%self.stats['int']
            outstr+="\twis %d\n"%self.stats['wis']
            outstr+="\tcha %d\n"%self.stats['cha']
            outstr+="\nSaves:"
            outstr+="\tfort %d\n"%self.saves['fort']
            outstr+="\tref %2d\n"%self.saves['ref']
            outstr+="\twill %d\n"%self.saves['will']
            outstr+="\n"+str(self.weapon)+"\n"
        return outstr

    def set_attributes(self):
        self.attributes_set = True
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
        self.weapon = Weapons.Random_Weapon(self.debug,self.seed)
        self.weapon.generate_weapon()
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
    rftest = Random_Fighter(level=3,name="RFBro")
    rftest.set_attributes()
    print rftest
