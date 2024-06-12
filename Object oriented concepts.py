class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Creating an instance of the Car class
my_car = Car('Toyota', 'Corolla', 2020)

# Accessing attributes and calling methods
print(my_car.get_descriptive_name())
my_car.read_odometer()

# Modifying attribute value directly
my_car.odometer_reading = 10000
my_car.read_odometer()

# Using method to update attribute value
my_car.update_odometer(15000)
my_car.read_odometer()

# Using method to increment attribute value
my_car.increment_odometer(100)
my_car.read_odometer()
