# First step creating base class 
class Device: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")
    
    def power_off(self):
        print(f"{self.brand} {self.model} is shutting down...")

 # Second step creating child class
class Smartphone(Device):
    def __init__(self, brand, model, storage, ram, battery):
        super().__init__(brand, model)   # call parent constructor
        self.storage = storage
        self.ram = ram
        self.__battery = battery   # private attribute
    
    # Method: make a call
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")
    
    # Method: install an app
    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model}.")
    
    # Encapsulation: getter & setter for battery
    def get_battery(self):
        return self.__battery
    
    def set_battery(self, new_level):
        if 0 <= new_level <= 100:
            self.__battery = new_level
            print(f"Battery updated to {self.__battery}%.")
        else:
            print("Invalid battery level!")

# Third step creating  smartphone objects
phone1 = Smartphone("Apple", "iPhone 15", "256GB", "8GB", 100)
phone2 = Smartphone("Samsung", "Galaxy S24", "512GB", "12GB", 80)

# Use methods
phone1.power_on()
phone1.make_call("+251911000000")
phone1.install_app("WhatsApp")
print("Battery Level:", phone1.get_battery())

# Update battery safely
phone1.set_battery(75)
phone1.set_battery(150)  # Invalid
