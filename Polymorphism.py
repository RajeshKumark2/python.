class GasCar(Car):
    def drive(self, miles):
        super().drive(miles) 
        print(f"Burned {miles / 25} galions")
def test_drive(car): 
    car.drive(100)

class Bicycle:
    def drive(self, miles):
        print(f"Cycling {miles} miles")

for vechicle in [ElecticalCar("Niisan", "Leaf", 40),
                 GasCar("Ford", "F-150"),
                 Bicycle()]:
    vechicle.drive(30)
    