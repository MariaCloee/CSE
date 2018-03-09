class Character(object):
    def __init__(self, name, description, health, state, location, dmg=10):
        self.name = name
        self.inventory = []
        self.description = description
        self.health = health
        self.state = state
        self.location = location  # Must be a Room
        self.damage = dmg
        self.alive = True

    def take(self, item):
        self.inventory.append(item)
        print("Taken")

    def drop(self, item):
        self.inventory.remove(item)
        print("Dropped")

    def look(self):
        print(self.location.name)

    def read(self):
        self.state = "happy"
        print("Reading.")

    def climb(self):
        self.state = "happy"
        print("You are climbing.")

    def jump(self):
        self.state = "jumpy"
        print("You are jumping.")

    def take_damage(self, amt):
        if self.health <= 0:
            print("%s is already dead" % self.name)
            return
        self.health -= amt
        if self.health <= 0:
            self.alive = False
            print("%s has died." % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s's health is %d. The enemy's health is %d." % (self.name, target.name, self.name,
                                                                                 self.health,
                                                                                 target.health))
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)


player = Character("Maria", "Generic Description", 100, None, None, 20)
enemy = Character("Enemy", "It's an enemy", 100, None, None)

player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)

enemy.attack(player)
print("%s's health is %s." % (player.name, player.health))
print("%s's health is %s." % (enemy.name, enemy.health))
