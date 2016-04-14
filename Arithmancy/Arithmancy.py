"""
This file contains the Arithmancy object, which contains all the capabilities of
solving the Pathfinder Arithmancy, as detailed on the page:

http://www.d20pfsrd.com/feats/general-feats/arithmancy

Essentially the user enters a phrase that respresents a spell.
Each letter is assigned a numeric value and then summed together.
The digits of the result are then summed and this process is
repeated until there is only
a single digit left. This is called the 'digital root' of the
spell, and is used in the game.

Note that it is true that the digital root (DR) of two words
is equal to the digital roots of the words added together.
Thus:

DR(wordone wordtwo) = DR(DR(wordone) + DR(wordtwo))

This can be shown algebraically, but is too long
for this comment.
"""

import sys

class Arithmancy(object):
    def __init__(self,phrase='',debug=False):
        self.phrase = phrase
        self.reduced_phrase = self.phrase.lower().replace(" ","")
        self.debug = debug #Used to print extra stuff
        self.root = self.calc_root()

    """
    This is the formula used to calculate the numerical
    value of each letter in the alphabet. For letters a-i
    it is numbers 1-9, and then it wraps back around to 1.
    z has the value 8.
    """    
    def letter_root(self,char):
        return (ord(char)-ord('a'))%9+1

    def calc_root(self):
        rp = self.reduced_phrase
        total = 0
        for char in rp:
            total+=self.letter_root(char)
            if self.debug:
                print char,self.letter_root(char)
        if self.debug:
            print "temp total first = ",total
        while total > 9:
            digits = [int(char) for char in str(total)]
            newtotal = 0
            for d in digits:
                newtotal += d
            total = newtotal
            if self.debug:
                print "temp total = ",total,'digits = ',digits
        return total

    def __str__(self):
        return "%s : digital root = %d"%(self.phrase,self.root)

#A unit test
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print "No arguments given, testing with the spell Fireball"
        spell = 'Fireball'
        test = Arithmancy(spell)
        print test
    else:
        spell = ""
        for arg in args[1:]:
            spell += str(arg)+" "
        spell_arithmancy = Arithmancy(spell.rstrip())
        print spell_arithmancy
