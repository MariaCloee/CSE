class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def trade(self):
        if self.trade:
            self.value = True
        else:
            self.value = False
        print("%s traded with %s." % (self.name, self.name))

    def take(self):
        print("%s took %s." % (self.name, self.name))

    def drop(self):
        print("%s dropped %s." % (self.name, self.name))


class
