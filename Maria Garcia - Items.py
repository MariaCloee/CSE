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
        print("%s spilled the water." % person.name)


class Ancient(Item):
    def __init__(self, name, value):
        super(Ancient, self).__init__(name, value)
