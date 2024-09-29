def print_pattern(input):
    for i in range(input):
        print(f"{i} ==val")
        s=''
        for j in range(i):
            print(f"{j} val")
            s = '*'+s
            # print(s)
        print(s)

def area_calculate(dimension1, dimension2, shape="triangle"):
    print(f"dimension1-{dimension1} and dimension2 - {dimension2} and shape - {shape}")
    if shape == "triangle":
        area = 1/2*dimension1*dimension2
    elif shape == "rectangle":
        area = dimension1*dimension2
    return area
# print_pattern(4)
print(area_calculate(4,4))