from dataclasses import dataclass

@dataclass
class Player:
    firstName:str = ""
    lastName:str = ""
    position:str = ""

    points:int = 0
    rebounds:int = 0
    assists:int = 0
    blocks:int = 0
    steals:int = 0
    turnovers:int = 0
    threePointersMade:int = 0
    freeThrowsMade:int = 0
    
    startingOrder:int = 0
    playerID:int = 0

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

class Lineup:
    def __init__(self):
        self.__list = []

    @property
    def count(self):
        return len(self.__list)

    def add(self, player):
        return self.__list.append(player)
    
    def remove(self, number):
        return self.__list.pop(number-1)
    
    def get(self, number):
        return self.__list[number-1]
    
    def set(self, number, player):
        self.__list[number-1] = player
        
    def move(self, oldNumber, newNumber):
        player = self.__list.pop(oldNumber-1)
        self.__list.insert(newNumber-1, player)

    def __iter__(self):
        for player in self.__list:
            yield player
            
        
def main():
    lineup = Lineup()
    lineup.add(Player(1, "Kobe", "Bryant", "SF", 100, 100, 100, 100, 100, 1, 100, 100))
    lineup.add(Player(2, "Steve", "Nash", "RF", 100, 100, 100, 100, 100, 1, 100, 100))
    
    for player in lineup:
        print(player.staringOrder, player.fullName, player.position,
              player.points, player.rebounds, player.assists, player.blocks,
              player.steals, player.turnovers, player.threePointersMade, player.freeThrowsMade)
        
    print("Bye!")

if __name__ == "__main__":
    main()
