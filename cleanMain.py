'''
Python Program designed to mimic the pokemon video game in the terminal.
CLEAN VARIANT

Names: Brandon Tiseo, Sean Devlin
Emails: Btiseo@charlotte.edu, Sdevlin1@charlotte.edu
Date:2/18/2025
'''

#General Pokémon class all subtypes inherit from.
class Pokemon():
    #Default constructor incase no parameters are passed into constructor.
    def __init__(self):
        self.name = ""
        self.health = 100
        self.attack = 10
        self.ptype = "normal"

    #Constructor with parameters.
    def __init__(self, name, health, attack, ptype):
        self.name = name
        self.health = health
        self.attack = attack
        self.ptype = ptype

    #Function used to attack other pokemon objects.
    def attackPokemon(self, enemy):
        enemy.health -= self.attack
        print(f"Dealt {self.attack} damage to {enemy.name}!")

    #Function used to heal pokemon objects.
    def healPokemon(self):
        health = 20
        self.health += health
        print(f"{self.name} healed for {health}!")

    #Function used to print pokemon data.
    def __str__(self):
        return f"{self.name}({self.ptype})\nHealth: {self.health} hp\n "

#Subclasses of Pokemon
class WaterType(Pokemon):
    def __init__(self):
        super().__init__("Mudkip", 200, 40, "Water")

class GrassType(Pokemon):
    def __init__(self):
        super().__init__("Treecko", 300, 20, "Grass")

class FireType(Pokemon):
    def __init__(self):
        super().__init__("Torchic", 150, 60, "Fire")


def main():
    p1 = GrassType()
    p2 = FireType()
    user_input = -1

    #Game Loop
    while((p1.health > 0 and p2.health > 0) and user_input != 3):
        print(f"You: {p1}")
        print(f"Enemy: {p2}")
        user_input = int(input("What would you like to do?(1:Attack, 2:Heal, 3:Leave):"))
        if(user_input == 1):
            p1.attackPokemon(p2)
        elif(user_input == 2):
            p1.healPokemon()
        else:
            print("INVALID INPUT")
            continue
        p2.attackPokemon(p1)

    #Define Winner
    #Checks if you ran away first before defining a winner of the match.
    if(user_input == 3):
        print("You Ran Away")
    else:
        if(p1.health <= 0):
            winner = p2
        else:
            winner = p1
        print(f"{winner.name} won the pokemon battle!")



if __name__ == "__main__":
    main()