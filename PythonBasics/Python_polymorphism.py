######################### METHOD POLYMORPHISM #########################
# Python function that can be used on different objects is the len() function.

#For strings len() returns the number of characters:
msg = "hello world"
print(len(msg))

msg_tuple = ("hello", "hi", "HRU")
print(f"len from tuple {len(msg_tuple)}")

######################## CLASS POLYMORPHISM #############################
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Rotates")

class Car(Vehicle):
    pass

class Flight(Vehicle):
    def move(self):
        print("fly")

class Boat(Vehicle):
    def move(self):
        print("sail")

def main():
    print("---------------------------POLYMORPHISM DEMO----------------------------------------")
    car_obj = Car("Mazda", "Cx-50")
    flight_obj = Flight("Boing", "741")
    boat_obj = Boat("Titanic", "0")

    car_obj.move()
    flight_obj.move()
    boat_obj.move()
    

if __name__ == '__main__':
    main()
    




