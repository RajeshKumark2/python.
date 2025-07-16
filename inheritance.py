class ElectricCar(Car):  # Inherits from Car
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    
    # Method overriding
    def drive(self, miles):
        super().drive(miles)
        print(f"Using {miles / 5} kWh")
    
    # New method
    def charge(self):
        print("Charging battery")

# Usage
tesla = ElectricCar("Tesla", "Model S", 100)
tesla.drive(200)  
# Output: 
# Driving 200 miles
# Using 40.0 kWh

print(isinstance(tesla, Car))  # True (inheritance check)


