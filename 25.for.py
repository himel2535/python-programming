# fruits=['apple','banana','cherry']
# for fruit in fruits:
#     print(fruit)
# fruits=['apple','banana','cherry']
# another=[]
# for fruit in fruits:
#     # print(fruits)
#     fruit=fruit.upper()
#     another.append(fruit)
# print(another)


# fruits=['apple','banana','cherry']
# another=[]
# for x in fruits:
#     # print(fruits)
#     x=x.upper()
#     another.append(x)
# print(another)


# fruits=['apple','banana','cherry']
# # another=[]
# for x in fruits:
#     # print(fruits)
#     x=x.upper()
#     print(x)

# for i in range(10,1,-2):
#     print(i)

# input= "bongodev"
# reversed=""
# for i in range(7,0,-1):
#     reversed=reversed+input[i]

# print(reversed)

# input= "bongodev"
# reversed=""
# for i in range(len(input)-1,-1,-1):
#     reversed=reversed+input[i]

# print(reversed)


# building = [
#     ['g1','g2','g3','g4'],
#     ['a1','a2','a3','a4'],       
#     ['b1','b2','b3','b4'],
# ]        # 4*3 matrix

# floors = 3
# appartments = 4

# for i in range(floors):
#     print("now in floor: ", i)
#     for j in range (appartments):
#         print(f"knocking on appartments {j}")


building = [
    ['g1','g2','g3','g4'],
    ['a1','a2','a3','a4'],       
    ['b1','b2','b3','b4'],
]        # 4*3 matrix

# floors = 3
# appartments = 4

# for floor in range(floors):
#     print("now in floor: ", floor)
#     for appartment in range (appartments):
#         print(f"knocking on appartments {appartment}")

# building = [
#     ['g1','g2','g3','g4'],
#     ['a1','a2','a3','a4'],       
#     ['b1','b2','b3','b4'],
# ]        # 4*3 matrix

# floors = 3
# appartments = 4

# for i in range(floors):
#     print("now in floor: ", i)
#     for j in range (appartments):
#         print(f"knocking on appartments:",building[i][j])


building = [
    ['g1','g2','g3','g4'],
    ['a1','a2','a3','a4'],       
    ['b1','b2','b3','b4']
]

for floor in building:
    print(floor)
    for appartment in floor:
        print("knocking on appartment: ", appartment)