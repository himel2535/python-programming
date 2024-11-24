# a= lambda x,y:x+y
# print(a(5,3))

people= [('monwar',1,4),('himel',3,100),('hossan',2,500)]
# people.sort(key=lamda pair: pair[2])
# print(people)
# print(sorted(people))

people.sort(key= lambda x: x[1]  )
print(people)