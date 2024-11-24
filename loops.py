# output=[]
# for i in range(100):
#     print('befor break: ',i)
#     if i>10:
        
#         continue
#     print('after break',i)
#     # output.append(i)
# print(output)



# output=[]
# for i in range(100):
#     print('befor break: ',i)
#     if i>10:
        
#         break
#     print('after break',i)
#     # output.append(i)
# print(output)


# output=[]
# for i in range(30):
#     if i%10 !=0:
#         continue
#     print('moja',i)
#     output.append(i)
# print(output)

# output=[]
# for i in range(9,18):
#     print("office hour",i)
#     if i==14:
#         break
    
#     output.append(i)
# print(output)
# numbers=[2,3,6,3,8,5]
# added_nmbrs_oneline=[(i+3) for i in numbers]
# print(added_nmbrs_oneline)

# x=[2,5,3,6,7,8,11]
# print(x)
# y=[(i*2) for i in x]
# print(y)

# a=int(input("enter a number:"))
# b=int(input("enter another number:"))

# print("large number is:",a if a>b else b)


# a=int(input("enter a number:"))
# b=int(input("enter another number:"))

# print("they are same" if a==b else "they are not same")


# a=int(input("enter a number:"))
# b=int(input("enter another number:"))
# c=int(input("enter third number:"))
# print(a if a<b and a<c else b if b<c else c)


a=int(input("enter a number:"))
b=int(input("enter another number:"))

print((b,a) [a<b])