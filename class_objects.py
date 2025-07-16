class Car:
    wheel = 4


    def __init__(self, make, model):
        self.make = make 
        self.model = model
        self.__mileage = 0 #private attribute 

    # Instance method
    def drive(self, miles):
        self.__mileage += miles
        print(f"Driving {miles} miles")
    
    # Getter for private attribute
    def get_mileage(self):
        return self.__mileage
    
    def __str__(self):
        return f"{self.make} {self.model}"
    
my_car = Car("tata", "Toyota")
my_car.drive(150)     
print(my_car)
print(my_car.get_mileage())