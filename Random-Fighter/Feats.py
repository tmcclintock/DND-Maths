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
        return self.name

class Random_Feat(object):
    all_feats = {
        "Alertness"=Feat("Alertness",None,"+2 Perception and Sense Motive"),
        "Athletic"=Feat("Athletic",None,"+2 Climb and Swim"),
        "Blind-Fight"=Feat("Blind-Fight",None,"Reroll miss chances for concealment"),
        "Catch Off-Guard"=Feat("Catch Off-Guard",None,"No penalties for improved melee weapons"),
        "Combat Reflexes"=Feat("Combat Reflexes",None,"Additiona AOO"),
        "Cosmopolitan"=Feat("Cosmopolitan",None,"Read and speak two additional languages"),
        "Death from Above"=Feat("Death from Above",None,"+5 Attack when approaching from higher ground"),
        "Deceitful"=Feat("Deceitful",None,"+2 Bluff and Disguise"),
        "Deft Hands"=Feat("Deft Hands",None,"+2 Disable Device and Sleight of Hand"),
        "Desperate Battler"=Feat("Desperate Battler",None,"+1/+1 when fighting alone"),
        "Disruptive"=Feat("Disruptive",{"level"=6},"Increase spell attempt DC in adjacent squares"),
        "Dodge"=Feat("Dodge",{"dex"=13},"+1 to AC")}
