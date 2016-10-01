"""
This contains the random weapons object,
which itself connects to a list of
possible weapons and provides the 
ability to select a random weapon.
"""
import random

class Weapon(object):
    def __init__(self,name,dice,dtype,hands):
        self.name = name
        self.dice = dice
        self.dtype = dtype
        self.hands = hands
        return

    def __str__(self):
        return "%s - %s - %d Handed\n\t%s damage"%(
            self.name,self.dtype,self.hands,self.dice)

class Random_Weapon(object):
    all_weapons = {
        "Longsword":Weapon("Longsword","1d8","S",1),
        "Shortsword":Weapon("Shortsword","1d6","S",1),
        "Club":Weapon("Club","1d6","B",1),
        "Dagger":Weapon("Dagger","1d4","P/S",1),
        "Greatsword":Weapon("Greatsword","2d6","S",2),
        "Heavy Flail":Weapon("Heavy Flail","1d10","B",2)}

    def __init__(self,debug=False,seed=1174001009):
        random.seed(seed)
        self.generated = False
        return

    def __str__(self):
        if not self.generated:
            return "No weapons generated."
        else:
            return str(self.weapon)
    
    def generate_weapon(self):
        self.generated = True
        N = len(Random_Weapon.all_weapons)
        i = random.randint(0,N)
        keys = Random_Weapon.all_weapons.keys()
        self.weapon = Random_Weapon.all_weapons[keys[i]]
        return

if __name__ == "__main__":
    RW = Random_Weapon()
    print RW
    RW.generate_weapon()
    print RW
    RW.generate_weapon()
    print RW
    RW.generate_weapon()
    print RW
