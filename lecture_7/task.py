# Создать BaseCharacter, BaseInActionCharacter BaseFunkoPop, BaseCosplayer
# Составить из них и из Mixin,,able логику наследований
# так, чтобы можно было минимум 6-7 Mxin'ов (созданных, а не у каждого класса)
# С помощью этих интерфейсов (мексинов) и наследования создать:
#   Shrek, PussInBoots, Donkey, JackHorner
# На каждого должен быть и персонаж, и BaeFunkoPop, и BaseCosplayer


class BaseHuman:
    pass
class BaseCharacter:
    name:str 
    def speak(self):
        print(f"я {self.name}" )

class BaseinActionCharacter(BaseCharacter):
    def perform_action(self):
        print(f"{self.name} сделал {self.action}")
    action:str
class BaseFunkoCharacter(BaseCharacter):
    his_display:str
    def display(self):
        print(f"у {self.name}`а {self.his_display} дисплей")
class BaseCosplayerCharacter(BaseCharacter, BaseHuman):
    def pose(self):
        print(f"косплеер жоска встал в позу {self.name}`а")


class BaseShrek(BaseCharacter):
    def __init__(self, name: str = "Shrek"):
        self.name = name
    can_nadyt_zmeu:bool = True
class BasePussInBoots(BaseCharacter):
    def __init__(self, name: str = "PussInBoots"):
        self.name = name
class BaseDonkey(BaseCharacter):
    def __init__(self, name: str = "Donkey"):
        self.name = name
class BaseJackHorner(BaseCharacter):
    def __init__(self, name: str = "JackHorner"):
        self.name = name

class ShrekInAction(BaseShrek, BaseinActionCharacter):
    def __init__(self, action: str = "Salto"):
        self.action = action
class PussInBootsInAction(BasePussInBoots, BaseinActionCharacter):
    def __init__(self, action: str = "NeSalto"):
        self.action = action
class DonkeyInAction(BaseDonkey, BaseinActionCharacter):
    def __init__(self, action: str = "DvoinoeSalto"):
        self.action = action
class JackHornerInAction(BaseJackHorner, BaseinActionCharacter):
    def __init__(self, action: str = "w v chatik"):
        self.action = action


class ShrekFunko(BaseShrek,BaseFunkoCharacter):
    pass
class PussInBootsFunko(BasePussInBoots, BaseFunkoCharacter):
    pass
class DonkeyFunko(BaseDonkey, BaseFunkoCharacter):
    pass
class JackHornerFunko(BaseJackHorner, BaseFunkoCharacter):
    pass


class ShrekCosplay(BaseShrek, BaseCosplayerCharacter):
    pass
class PussInBootsCosplay(BasePussInBoots, BaseCosplayerCharacter):
    pass
class DonkeyCosplay(BaseDonkey, BaseCosplayerCharacter):
    pass
class JackHornerCosplay(BaseJackHorner, BaseCosplayerCharacter):
    pass

puss = PussInBootsCosplay()
if __name__ == "__main__":
    puss.pose()