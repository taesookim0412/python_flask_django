x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1
x[1][0] = 15
#print(x)

#2
students[0]['last_name'] = "Bryant"
#print(students)

#3
sports_directory['soccer'][0] = "Andres"
#print(sports_directory)

z[0]['y'] = 30
#print(z)



def iterateDictionary(list):
    for stud in list:
        for key in stud.keys():
            print(key + " " + stud[key])

def iterateDictionary2(key_name, list):
    for stud in list:
        print (stud[key_name])
            

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

iterateDictionary2('last_name', students)


def printInfo(some_dict):
    numlocations = len(some_dict['locations'])
    numinstructors = len(some_dict['instructors'])
    print(numlocations, "LOCATIONS")
    for value in some_dict['locations']:
        print (value)
    print("")
    print (numinstructors, "INSTRUCTORS")
    for value in some_dict['instructors']:
        print(value)



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
