"""
This contains the random feats object,
which itself connects to a list of the
possible feats and also provides
the ability to select random feats.
"""
import random

class Feat(object):
    def __init__(self,name,prereqs,bonus):
        self.name = name
        self.prereqs = prereqs
        self.bonus = bonus
        return

    def __str__(self):
        
