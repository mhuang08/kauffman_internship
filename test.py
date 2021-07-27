# CSDojo Python Tutorial #1
v1 = "first string"
v2 = " second string"
temp = v1
v1 = v2
v2 = temp
print(v1)
print(v2)

# CSDojo Python Tutorial #2
e = 20
f = 8
if e < f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")

g = 10
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        if g > h+4:
            print("g is greater than h plus 4")
        else:
            print("g is greater than h")

name = "mei"
height_m = 1.524
weight_kg = 49.9

bmi = weight_kg / (height_m ** 2)
print(name)
print("bmi")
print(bmi)

if bmi < 25:
    print("not overweight")
else:
    print("overweight")