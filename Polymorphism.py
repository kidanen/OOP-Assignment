# Base class
class Vehicle:
    def move(self):
        pass   # placeholder (to be overridden)


# Child classes
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Bike(Vehicle):
    def move(self):
        print("🚲 Pedaling on the street...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water...")
# Create a list of different vehicles
vehicles = [Car(), Bike(), Plane(), Boat()]

# Loop through and call move() on each
for v in vehicles:
    v.move()
