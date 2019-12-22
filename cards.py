###   Cards Module defining card behavior for the model
###   created by Avynn Donage (12/21/19)

class cost:
    def __init__(self, red, green, blue, brown, white):
        self.red = red
        self.green = green
        self.blue = blue
        self.brown = brown
        self.white = white

class card:
    def __init__(self, tier, prestige, bonus, cost):
        self.tier = tier
        self.prestige = prestige
        self.bonus = bonus
        self.cost = cost

    def encode(self):
        dictionary = self.__dict__
        dictionary['cost'] = self.cost.__dict__
        
        return dictionary
