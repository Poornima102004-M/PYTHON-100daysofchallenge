import random

# Define a class for characters (player and enemy)
class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_target(self, target):
        damage = random.randint(1, self.attack)
        print(f"{self.name} attacks {target.name} and deals {damage} damage.")
        target.take_damage(damage)

    def __str__(self):
        return f"{self.name} | HP: {self.hp} | Attack: {self.attack}"

# Function for the battle sequence
def battle(player, enemy):
    print(f"=== Battle: {player.name} vs {enemy.name} ===")
    while player.is_alive() and enemy.is_alive():
        # Player attacks first
        player.attack_target(enemy)
        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        # Enemy attacks back
        enemy.attack_target(player)
        if not player.is_alive():
            print(f"{player.name} has been defeated!")

    # Display final status of both characters
    print(player)
    print(enemy)

# Example usage
if __name__ == "__main__":
    # Create player and enemy characters
    player = Character("Hero", 100, 20)
    enemy = Character("Monster", 80, 15)

    # Start the battle
    battle(player, enemy)
