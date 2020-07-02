#Crappiest version of Domain Dominance Code


print("Hello, Domain Dominance!")

# class Attack(object):
    
#     def __init__(self, origin, targets, dmg, tipo):
#         self.origin = origin
#         self.targets = targets
#         self.dmg = {tipo : dmg}
class Attack(object):
    def __init__(self, tipo, maxTargets, dmg):
        self.dmg = {tipo : dmg} 
        self.maxTargets = maxTargets
        pass


class Creature(object):
    #Base class for creatures
    energyCount = 0
    
    
    def __init__(self, health, energy, tipo, guardian):
        self.health = health
        self.energy = energy
        self.tipo = tipo
        self.guardian = guardian
        
        
    #Place 3 Attack objects instead of atk functions
    def upkeep(self):
        self.energyCount += self.energy 
    def chooseTargets(self):
        pass
    def dealDmg(self):
        pass
    def takeDmg(self):
        pass
    def atkOne(self):
        pass
    def atkTwo(self):
        pass
    def atkThree(self):
        pass
    def setElement(self, element, elementList): 
        while not element in elementList: 
            element = input("Choose an element for your creature (Fire, Water, Ice): ")
            if not element in elementList: 
                print("Invalid entry.")  
        return element
    def alliesAtk(self):
        pass
    
class EFDragon(Creature):
    
    element = "Fire"
    rage = 0
    
    def __init__(self, guardian):
        super(EFDragon, self).__init__(70, 2, "Dragon", guardian)
        if self.guardian:
            self.health += 10
    
    def dealDmg(self):
        print("+2 to fire attacks")
        print("+1 to atk per rage")
    def takeDmg(self):
        print("-2 from fire dmg")
        print("+5 to rage per dmg") #compatible with neg int for healing
        
class KFDragon(Creature):
    
    element = "Fire"
    rage = 0
    
    def __init__(self, guardian):
        super(KFDragon, self).__init__(60, 2, "Dragon", guardian)
    
    def dealDmg(self):
        print("+1 to fire atks per non-minion fire creature controlled")
    def takeDmg(self):
        print("+5 to rage per dmg") #compatible with neg int for healing
    def alliesAtk(self):
        print("For non-minion fire creatures: +1 fire dmg per other non-minion fire creature controlled")
    pass

class Dragonling(Creature):
    element = "void"
    elementList = ["Fire", "Water", "Ice"]
    
    def __init__(self, guardian):
        super(Dragonling, self).__init__(40, 1, "Dragon", guardian)
        self.element = self.setElement(self.element, self.elementList)
        
    #Borrow attacks from one other creature somehow
    
    def dealDmg(self):
        print("-2 energy cost, min 1 energy")
        print("-2 dmg, min 1 dmg")
   
    
#Attack flow:
#Check if creature has an action left
#Select attack
#Check if creature can use that type of attack 
#Check if creature has enough energy 
#Select target(s)
#Create Attack object
#Assign dmg and type to object 
#Add internal buffs (pass to appropriate functions, or manually add)
#If multiple targets: 
    #Player chooses how to distribute dmg (if multiple targets)
    #Split attack object if multiple targets
#Pass to target(s) for external modifications
#Target(s) modify own health
