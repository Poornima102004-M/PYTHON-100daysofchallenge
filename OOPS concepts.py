import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage.")
    
    def display_status(self):
        print(f"{self.name} - Health: {self.health}")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.take_damage(damage)
        print(f"{self.name} attacks {player.name} and deals {damage} damage.")
    
    def display_status(self):
        print(f"{self.name} - Health: {self.health}")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    enemy = Enemy("Orc", 50, 8)
    
    print("Welcome to the Battle!")
    print(f"{player.name} vs {enemy.name}")
    print("Let the battle begin!")
    print("----------------------------------------")
    
    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        enemy.attack(player)
        print("----------------------------------------")
        player.display_status()
        enemy.display_status()
        input("Press Enter to continue...")
    
    print("----------------------------------------")
    if player.is_alive():
        print(f"{player.name} defeated {enemy.name}!")
    else:
        print(f"{enemy.name} defeated {player.name}!")

if __name__ == "__main__":
    main()
