class CoffeeMachine:
    
    def _boil_water(self):
        print("Heating water to exactly 205 degrees")
    def _grind_beans(self):
        print("Grinding beans for 15 seconds")
    def _pump_water(self):
        print("Pumping pressurized water through the coffee filter...")
    
    def press_start(self):
        print("Starting the coffee making process...")
        self._boil_water()
        self._grind_beans()
        self._pump_water()
        print("Coffee is ready!")

my_machine = CoffeeMachine()
my_machine.press_start()
    