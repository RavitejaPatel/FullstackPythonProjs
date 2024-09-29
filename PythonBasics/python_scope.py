####################################PYTHON SCOPES#####################################

######LOCAL SCOPES###########
def outer():
    outer_val = 10
    def inner():
        print(f"local variable is from Inner method {outer_val}")
    inner()
    return outer_val

outer_obj = outer()
print(f"outer obj is {outer_obj}")


#########GLOBAL SCOPES###########
global_var = 20

def method_a():
    a=21
    print(f"val is {global_var} and local is {a}")

def method_b():
    print(f"val from method_bis {global_var} ")

method_a()
method_b()


##########USE OF GLOBAL KEYWORD###############
## Also, use the global keyword if you want to make a change to a global variable inside a function.
x=4
def funA():
    global x
    x=5
    print(f"x val is from funA {x}")

def funB():
    x=20
    print(f"x val is {x}")

funA()
funB()


############USE OF NON-LOCAL KEYWORD###############
def outerA():
    a="raviteja"
    def innerA():
        nonlocal a
        a="Raviteja Poosala"
    innerA()
    a="Santhoshini pendyala"
    return a

print(f"outre fun is {outerA()}")