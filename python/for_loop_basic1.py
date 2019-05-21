for i in range(0, 151):
    print(i)

for i in range(5, 1005):
    if i % 5 == 0:
        print(i)

for i in range (1, 101):
    #Must be /5, Can't be /10.
    if (i % 5 == 0) and (i % 10 != 0):
        print("Coding")
    elif i % 10 == 0:
        print ("Coding Dojo")
    else:
        print(i)

x = 0
for i in range (0, 500001):
    if i % 2 != 0:
        x+= i
print(x)

for i in range(2018, -2, -4):
    print(i)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % 3 == 0:
        print(i)
