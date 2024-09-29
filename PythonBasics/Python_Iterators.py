# Reference : https://www.w3schools.com/python/python_iterators.asp

mytuple = ("apple", "plum", "pineapple")
itr = iter(mytuple)

print(f"fruit is {next(itr)}")
print(f"fruit is {next(itr)}")
print(f"fruit is {next(itr)}")


######################  CREATING AN ITERATOR ############################# 
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNum():
    def __iter__(self):
        self.a = 1
        return self
    
    # performing iteration operation with __next__()
    def __next__(self):
        # x = self.a #x = 1
        self.a+=1
        return self.a

    def iterate_next_till_range(self):
        for i in range(5):
            print(f"Next val is {self.__next__()}")

num_obj = MyNum()
print(f"num ob is {num_obj.__iter__().a}")
num_obj.iterate_next_till_range()



