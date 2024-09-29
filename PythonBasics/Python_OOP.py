class Person():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def person_details(self):
        # print(f"firstname {self.fname} lastname {self.lname}")
        return f"firstname {self.fname} lastname {self.lname}"
        
person = Person("Raviteja","Poosala") 
print(person.person_details())

# Modify Object Properties
person.fname = "Rocky"
print(person.person_details())

# deleting person object :: Expected error : NameError: name 'person' is not defined. Did you mean: 'Person'?
del person
# print(person.person_details())



################### PYTHON INHERITANCE ###################

# considering above class as parent , creating child class now

# Use the pass keyword when you do not want to add any other properties or methods to the class.
# class Student(Person):
#     pass


class Student(Person):
    def __init__(self, gender, fname, lname):
        super().__init__(fname=fname,lname=lname)
        self.gender = gender
    
    def welcome_note(self):
        print(f"student bio is {self.person_details()} and gender is {self.gender}")


std = Student("Female", "Anusha", "Poosala")
# print(f"student bio is {std.person_details()} and gender is {std.gender}")
std.welcome_note()

