from model import board, player

class manager:

    validColors = ["red", "white", "blue", "green", "brown", "joker"]
    
    def getThreeCoins(self, player, board, choice):
        ### DESC:
        # This function takes in a player board and a choice,
        # the choice is a 3 tuple representing the three colors
        # that the player has chosen for their turn, there must be
        # three unique choices for each color, if there is not then
        # this function should raise an exception.  Otherwise the
        # player recieves all three colors.

        if len(choice) != 3:
            raise Exception("There must be three choices")

        for color in choice:
            if not (color in self.validColors):
                raise Exception("Color is invalid")
            
        # it's ugly but N will always be 3 so meh        
        if choice[1] == choice[2] or choice[1] == choice[0] or choice[0] == choice[2]: 
            raise Exception("colors must be unique")
            
        for color in choices:
            player.wallet[choice] = player.wallet[choice] + 1
            

    
    def getNames(self):
        #THIS SHOULD BE CHANGED WHEN ADDING A CONTROLLER
        
        playerNo = 0
        
        for i in range(0, self.numCPU):
            self.players.append(player.player("player %d" % i)) 
            playerNo = playerNo + 1

        for i in range(playerNo, self.numPlayers):
            self.players.append(player.player(input("What's your prefered name? ")))
    
    def __init__(self, numPlayers, numCPU, *resourceOverride):

        if(numCPU > numPlayers):
            raise Exception("cannot have more AI than players")

        try:
            self.board = board.board(numPlayers)
        except Exception as err:
            print("cannot init board: ", err)

        self.numPlayers = numPlayers
        self.numCPU = numCPU
        self.players = []

        self.board = board.board() if len(resourceOverride) == 0 else board.board(resourceOverride[0])
        self.getNames()
        
        

if __name__ == "__main__":
    numPlayers = int(input("How many players? "))
    numAI = int(input("How many computers? "))

    manager(numPlayers, numAI)
