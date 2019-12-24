import board
import cards
import player

class manager:

    def getNames(self):
        #THIS SHOULD BE CHANGED WHEN ADDING A CONTROLLER
        
        playerNo = 0
        
        for i in range(0, self.numCPU):
            self.players.append(player.player("player %d" % i)) 
            playerNo = playerNo + 1

        for i in range(playerNo, self.numPlayers):
            self.players.append(player.player(input("What's your prefered name? ")))
    
    def __init__(self, numPlayers, numCPU):

        if(numCPU > numPlayers):
            raise Exception("cannot have more AI than players")

        try:
            self.board = board.board(numPlayers)
        except Exception as err:
            print("cannot init board: ", err)

        self.numPlayers = numPlayers
        self.numCPU = numCPU
        self.players = []

        self.getNames()
        
        

if __name__ == "__main__":
    numPlayers = int(input("How many players? "))
    numAI = int(input("How many computers? "))

    manager(numPlayers, numAI)
