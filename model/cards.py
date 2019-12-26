###   Cards Module defining card behavior for the model
###   created by Avynn Donage (12/21/19)

class cost:
    def __init__(self, red, green, blue, brown, white):
        self.red = red
        self.green = green
        self.blue = blue
        self.brown = brown
        self.white = white

    @staticmethod
    def decode(dictionaryObject):
        return cost(dictionaryObject["red"], dictionaryObject["green"], dictionaryObject["blue"], dictionaryObject["brown"], dictionaryObject["white"])

class card:
    def __init__(self, tier, prestige, bonus, cost):
        self.tier = tier
        self.prestige = prestige
        self.bonus = bonus
        self.cost = cost

    @staticmethod
    def encode(self):
        dictionary = self.__dict__
        dictionary['cost'] = self.cost.__dict__
        
        return dictionary

    @staticmethod
    def decode(dictionaryObject):
        return card(dictionaryObject["tier"], dictionaryObject["prestige"], dictionaryObject["bonus"], cost.decode(dictionaryObject["cost"]))

    
class tile:
    def __init__(self, prestige, cost):
        self.prestige = prestige
        self.cost = cost

    @staticmethod
    def encode(self):
        dictionary = self.__dict__
        dictionary['cost'] = self.cost.__dict__

        return dictionary

    @staticmethod
    def decode(dictionaryObject):
        return tile(dictionaryObject["prestige"], cost.decode(dictionaryObject["cost"]))
