# a=[1,2,3,4,5]
# def do_sqr(x):
#     return x*x
# sqrded= list(map(do_sqr,a))
# print(sqrded)

# any_liiiist=[1,2,3,4,5]
# def function(x):
#     return x*x
# newliiiist= list(map(function,any_liiiist))
# print(newliiiist)

# myList= ["apple","bannana","moja"]
# def fnctn(x):
#     return len(x)
# newList=list(map(fnctn,myList))
# print(newList)

# a=[2,3,4,-5]
# b=[5,6,8,5]

# def fnctn(x,y):
#     return x+y
# c=list(map(fnctn,a,b))
# print(c)

a=[2,4,5,6,8,1]
b=[1,4,5,2,7,4]
c=list(map(lambda x,y : x+y ,a,b))
print(c)