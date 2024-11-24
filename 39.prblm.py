##  find a common elements between two list


# a=[1,3,5,8,2,11]
# b=[3,5,6,7,11,5]

# a_set=set(a)
# b_set=set(b)
# result=a_set.intersection(b_set)
# r=sorted(result)
# print(r)



# a=[3,5,8,11,3,11]
# b=[3,6,11,11,5]
# r=[]

# for i in a:
#    #flag=0
#     for j in b:
#         if i==j:
#             flag=1
#         print(f"checking i={i} and j={j} flag={flag}")
#     if flag==1 :
#         r.append(i)
# print(r)


## [here i got a prblm that if 1st list i got duplicat nmbr than its take duplicate]



a=[3,5,8,11,3,11]
b=[3,6,11,11,5]
r=[]

for i in a:
    if i in b:
        r.append(i)
print(r)

# word ="bangladesh"
# print("a" in word)

