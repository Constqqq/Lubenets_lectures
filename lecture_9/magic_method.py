from enum import StrEnum
from typing import Self
import random
class Names(StrEnum):
    JOHN = "John Lennon"
    Paul = "Paul McCartney"
    GEORGE = "George Harrison"
    RINGO = "Ringo Starr"

class Beatle:
    health_points:int 
    name: Names 
    
    
    def __init__(
        self,
        health_points = 100,
        name = Names.JOHN,
    ) ->None:
        self.health_points = health_points
        self.name = name
    def styling(self) ->str:
        if self.name is Names.JOHN:
            return("John's style")
        elif self.name is Names.Paul:
            return "Paul's style"
        elif self.name is Names.GEORGE: 
            return "George's style"
    
    def attack (self, other:Self) ->None:
        print(f"{self.name} attacks {other.name} {self.styling()}")
        other.health_points -= 10
    def __eq__(self, other:Self) ->bool:
        return self.health_points == other.health_points
    def __lt__(self, other:Self) ->bool:
        return self.health_points < other.health_points
    def __gt__( self, other:Self) ->bool:
        return self.health_points > other.health_points
    def __le__(self, other:Self) ->bool:
        return self.health_points <= other.health_points
    def __str__ (self) ->str:
        return f"{self.name} has {self.health_points} hp"
    
class BeetlesArmy:
    beetles_list: list[Beatle]
    beetles_name: Names
    beetles_max_health_points: int

    def __init__(self,
                 beetles_name: Names,
                 max_health_points: int = 100,
                 army_size: int = 20
                 ) -> None:
        self.beetles_name = beetles_name
        self.beetles_max_health_points = max_health_points
        self.beetles_list = []

        for i in range(army_size):
            beetle = Beatle(
                health_points=random.randint(
                    a=1,
                    b=self.beetles_max_health_points
                ),
                name=self.beetles_name
            )
            self.beetles_list.append(beetle)
                
            
    def army_listing(self) ->None:
        for beetle in self.beetles_list:
            print(beetle)
        




if __name__ == "__main__":
    ba1 = BeetlesArmy(beetles_name=Names.JOHN)
    ba2 = BeetlesArmy(beetles_name=Names.Paul)
    for beetle in ba1.beetles_list:
        print(beetle)
