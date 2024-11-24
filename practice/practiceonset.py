my_set1 = set() #this is how to create an empty set, by calling its functions "set"
my_turple = (1,2,3)


my_set = {"apple","banana", "orange"} #without the comma the set sees it as a single number
my_set.add(9)
print(my_set)

my_set1 = {"apple","banana", "orange"}
my_set2 = {"watermelon","date", "allfruit"}
my_set3 = my_set2.intersection(my_set1)
print(my_set2.union(my_set1))
print(my_set3)
student = { "name" : "Babatunde",
            "age" : 25,
            "gender" : 'f',
            "matric" : 2419,
            "scores" : [90,80,70,60,50],
            "count" : (1,2,3,4,5,6,7,8,9)
         }
print(student["name"])