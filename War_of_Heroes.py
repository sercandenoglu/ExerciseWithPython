import random

class Heroes():
    def __init__(self, name):
        self.nickname = name
        self.health = 100
        self.heroType = "warrior"

    def Attack(self, Heroes, power):
        survival = True
        hitRatio = 1 - (power/100)
        if hitRatio >= random.random():
            Heroes.health -= power
            print(f"{Heroes.nickname} is successfully take hit {power} damage")
        else:
            self.health -= power
            print(f"{self.nickname} is screw up and {self.nickname} is lose {power} health point")
        if self.health <= 0:
            self.health = 0
            survival = False
        if Heroes.health <= 0:
            Heroes.health = 0
            survival = False

        Situation(self, Heroes)
        return survival

def Situation(hero1, hero2):
    print(f"{hero1.nickname} has %{hero1.health} health", "█" * int(hero1.health/4))
    print(f"{hero2.nickname} has %{hero2.health} health", "█" * int(hero2.health/4))

def Assault(*hero):
    #for get power value of users
    survival = True
    power = 20
    turn = 0
    while survival:
        power = int(input(f"Enter the {hero[turn%2].nickname}'s power value: "))
        survival = hero[turn%2].Attack(hero[turn%2+(1 if turn%2 == 0 else -1)], power)
        turn += 1


player1 = Heroes(input("Enter the nickname of the first player:  "))
player2 = Heroes(input("Enter the nickname of the second player: "))

Assault(player1, player2)

if player1.health == 0:
    print(f"{player2.nickname} WON!!!!!")
else:
    print(f"{player1.nickname} WON!!!!!")


