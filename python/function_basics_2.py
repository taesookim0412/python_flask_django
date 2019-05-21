def countdown(a):
    b = 0
    list = [ ]
    for i in range(a, 0, -1):
        list.append(i)
    print(list)
countdown(5)

def print_and_return(a, b):
    print(a)
    return b
a = print_and_return(1, 2)
print(a)

def first_plus_length(list):
    return (list[0] + len(list))
a = first_plus_length([1, 2, 3, 4, 5])
print(a)

def values_greater_than_second(list):
    newlist = [ ]
    if len(list) < 2:
        return false
    for i in range(0, len(list)):
        if list[i] > list[1]:
            newlist.append(list[i])
    print(len(newlist))
    return newlist
a = values_greater_than_second([5,2,3,2,1,4])
print(a)

def this_length_that_value(size, value):
    newlist = []
    for i in range(0, size):
        newlist.append(value)
    return newlist
a = this_length_that_value(4, 7)
print(a)