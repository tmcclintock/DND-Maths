"""
This contains the random skills object,
which itself connects to a list of the
possible skills and also provides
the ability to select random feats.
"""
import random

class Skill(object):
    def __init__(self,name,):
        self.name = name
        return

    def __str__(self):
        return "\t%s"%(self.name)

class Random_Skills(object):
    
