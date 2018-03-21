class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def trade(self, person):
        if self.trade:
            self.value = True
        else:
            self.value = False
        print("%s traded with %s." % (person.name, self.name))

    def take(self, person):
        print("%s took %s." % (person.name, self.name))

    def drop(self, person):
        print("%s dropped %s." % (person.name, self.name))


class Consumables(Item):
    def __init__(self, name, value, color):
        super(Consumables, self).__init__(name, value)
        self.color = color

    def eat(self, person):
        print("%s is eating the %s" % (person.name, self.name))


class Fruits(Consumables):
    def __init__(self, name, value, color, taste):
        super(Fruits, self).__init__(name, value, color)
        self.taste = taste


class Coconuts(Consumables):
    def __init__(self, name, value, color, water):
        super(Coconuts, self).__init__(name, value, color)
        self.water = water

    def broke(self, person):
        print("%s broke the %s in half." % (person.name, self.name))


class Water(Consumables):
    def __init__(self, name, value, color):
        super(Water, self).__init__(name, value, color)

    def drink(self, person):
        print("%s drank the %s." % (person.name, self.name))

    def spill(self, person):
        print("%s spilled the %s." % (person.name, self.name))


class Ancient(Item):
    def __init__(self, name, value, color):
        super(Ancient, self).__init__(name, value)
        self.color = color


class Drum(Ancient):
    def __init__(self, name, value, color):
        super(Drum, self).__init__(name, value, color)

    def hit(self, person):
        print("%s hit the %s." % (person.name, self.name))


class ChiefHat(Ancient):
    def __init__(self, name, value, size, color):
        super(ChiefHat, self).__init__(name, value, color)
        self.size = size

    def wear(self, person):
        print("%s is wearing the %s." % (person.name, self.name))


class GrandmaItems(Ancient):
    def __init__(self, name, value, color, size):
        super(GrandmaItems, self).__init__(name, value, color)
        self.size = size


class Stick(GrandmaItems):
    def __init__(self, name, value, color, size):
        super(Stick, self).__init__(name, value, color, size)

    def attack(self, person):
        print("%s attacked with Grandma's %s." % (person.name, self.name))

    def defend(self, person):
        print("%s defended with Grandma's %s against %s." % (person.name, self.name, person.name))


class Necklace(GrandmaItems):
    def __init__(self, name, value, color, size, beads):
        super(Necklace, self).__init__(name, value, color, size)
        self.beads = beads

    def wear(self, person):
        print("%s is wearing the %s." % (person.name, self.name))


class Rug(GrandmaItems):
    def __init__(self, name, value, color, size):
        super(Rug, self).__init__(name, value, color, size)

    def moves(self):
        print("The %s has moved." % self.name)


class Toys(Item):
    def __init__(self, name, value, color, size):
        super(Toys, self).__init__(name, value)
        self.color = color
        self.size = size


class Ball(Toys):
    def __init__(self, name, value, color, size):
        super(Ball, self).__init__(name, value, color, size)

    def bounce(self):
        print("The %s is bouncing." % self.name)


class Shell(Toys):
    def __init__(self, name, value, color, size):
        super(Shell, self).__init__(name, value, color, size)

    def listen(self, person):
        print("%s is listening through the %s." % (person.name, self.name))


class Tools(Item):
    def __init__(self, name, value):
        super(Tools, self).__init__(name, value)

    def use(self, person):
        print("%s is using the %s." % (person.name, self.name))


class Sack(Tools):
    def __init__(self, name, value, color):
        super(Sack, self).__init__(name, value)
        self.color = color

    def put_in(self, person):
        print("%s put %s in the %s." % (person.name, self.name, self.name))


class Ladder(Tools):
    def __init__(self, name, value):
        super(Ladder, self).__init__(name, value)

    def climb(self, person):
        print("%s is climbing the %s." % (person.name, self.name))


class Paddle(Tools):
    def __init__(self, name, value, size):
        super(Paddle, self).__init__(name, value)
        self.size = size

    def attack(self, person):
        print("%s attacked with Grandma's %s." % (person.name, self.name))

    def defend(self, person):
        print("%s defended with Grandma's %s against %s." % (person.name, self.name, person.name))

    def paddle(self, person):
        print("%s is paddling with the %s" % (person.name, self.name))


class Boat(Tools):
    def __init__(self, name, value, size, sail):
        super(Boat, self).__init__(name, value)
        self.size = size
        self.sail = sail

    def sail(self, person):
        print("%s is sailing on a %s." % (person.name, self.name))


class Magic(Item):
    def __init__(self, name, value, color):
        super(Magic, self).__init__(name, value)
        self.color = color

    def use(self, person):
        print("%s is using the %s." % (person.name, self.name))


class Key(Magic):
    def __init__(self, name, value, color):
        super(Key, self).__init__(name, value, color)

    def open(self, person):
        print("%s is opening the %s with the %s." % (person.name, self.name, self.name))


class Treasure(Magic):
    def __init__(self, name, value, color, key):
        super(Treasure, self).__init__(name, value, color)
        self.key = key

    def open(self):
        print("The %s is open." % self.name)


class Heart(Magic):
    def __init__(self, name, value, color):
        super(Heart, self).__init__(name, value, color)

    def glow(self):
        print("%s glows." % self.name)


class MaliHook(Item):
    def __init__(self, name, value, color, shape):
        super(MaliHook, self).__init__(name, value)
        self.color = color
        self.shape = shape

    def attack(self, person):
        print("%s attacked with Grandma's %s." % (person.name, self.name))

    def defend(self, person):
        print("%s defended with Grandma's %s against %s." % (person.name, self.name, person.name))

    def glow(self, person):
        print("%s is glowing. %s is holding it." % (self.name, person.name))
