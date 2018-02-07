class Car:
    color = ""
    def description(self):
        description_string = "This is a %s car de marca %s." % (self.color, self.marca)
        return description_string

car1 = Car()
car2 = Car()

car1.color = "Blue"
car2.color = "Red"

car1.marca = "Toyota"
car2.marca = "Suzuki"

print(car1.description())
print(car2.description())
