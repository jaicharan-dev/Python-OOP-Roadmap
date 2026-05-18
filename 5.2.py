from abc import ABC, abstractmethod
class CoffeeMakerBlueprint(ABC):
    
    @abstractmethod
    def press_start(self):
        pass
    
class EspressoMachine(CoffeeMakerBlueprint):
    def press_start(self):
        print("Pushing high pressure water through fine espresso grounds!")

class DripMachine(CoffeeMakerBlueprint):    
    def press_start(self):
        print("Slowly dripping hot water over a paper filter.")

my_espresso = EspressoMachine()
my_espresso.press_start()  

my_drip = DripMachine()
my_drip.press_start()

# catching error
class FrenchPress(CoffeeMakerBlueprint):
    def plunge(self):  
        print("Plunging the coffee grounds down.")

french_press = FrenchPress()