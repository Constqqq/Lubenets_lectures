class Human:
    eyes : int = 2
    hands: int = 2
    legs:int 
    hair_color:str = "brown"
    name:str 
    
    def __init__(self, name: str = "Boris", legs:int = 2):
        self.name = name
        self.legs = legs
        
    def blink(self):
        print(f"{self.name} blinked")
    def walk(self):
        print(f"{self.name} walked away")
    def break_plank(self, plank_material: str = "wodden", quality: int = 2):
        print(f"{self.name} Breaks {quality} {plank_material} planks")

if __name__ == '__main__':
    human1 = Human()  
    
    human1.blink()
    human1.break_plank()
    human1.break_plank('plactic', 3)
    
    human2 = Human(name="Borik", legs=5)
    
    human2.blink()
class SmartHuman(Human):
    iq:int = 130
    glasses:bool = True
    def __init__(self, glasses = True, iq = 130):
        super().__init__()
        self.glasses = glasses
        self.iq = iq
    
    def blink (self):
        print(f"smart {self.name} blinked with {self.eyes} and with glasses {'on' if self.glasses is True else 'off'} ")
smart_human = SmartHuman(glasses=False)
smart_human.blink() 