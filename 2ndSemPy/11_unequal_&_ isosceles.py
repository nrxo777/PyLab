import math

a = int(input("Enter Your First Value: "))
b = int(input("Enter Your Second Value: "))
c = int(input("Enter Your Third Value: "))

if a < (b + c) and b < (a + c) and c < (a + b):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print('The Area is: ', area)
else:
    print('The triangle is impossible')