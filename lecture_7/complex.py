from abc import abstractmethod
from typing import override



class MixinWalkable:
    legs:int = 2
    def walk(self):
        print(f"Walked away on {self.legs} feets")
    
class MixinNoisable:
    @abstractmethod
    @override
    def make_noise(self, volume_db:int ) -> None:
        raise NotImplementedError

class MixinDustable:
    def get_dusty(self) ->None: ... 
class BaseToy:
    material: str = "plastic"
    
    
    
class BaseDuck:
    wings:int = 2
    
    
    
    
class Duck(BaseDuck):
        def make_noise(self, volume_db:int ) -> None:
            print(f"quack {volume_db}")

class ToyDuck(BaseDuck, BaseToy, MixinDustable):
        def make_noise(self, volume_db:int ) -> None:
            print(f"pppppp {volume_db}")















if __name__ == "__main__":
    d = Duck()
    d.make_noise(12)







#SOLID

#DRY don`t repeat uself`

#KISS keep it simple, stupid