# def moja(n):
#     if len(n)==len(n+1) and len(n+1)==len(n+2):
   
#     return  print(moja.pop(len(n+2)))



# string = "aaaabbbbbcccccddddd"

# def remove_triples(s):
#     result = ""
#     i = 0
#     for i in range(len(s)):
        
#         if i + 2 < len(s) and s[i] == s[i + 1] == s[i + 2]:
            
#             while i + 1 < len(s) and s[i] == s[i + 1]:
#                 i += 1
#         else:
            
#             result += s[i]
#     return result

# new_string = remove_triples(string)
# print(new_string)



# string="aaaabbbbbccccddddddd"

# def triples(s):
#     result= ""
#     i=0
#     for i in range (len(s)):
#         if i+2 < len(s) and s[i]==s[i+1]==s[i+2]:
#             while i+1 < len(s) and s[i]==s[i+1]:
#                 i+=1
#         else:
#             result+=s[i]
#     return result
# update=triples(string)
# print(update)



# result={}
# for i in range(1,5):
#     result[i]=i*i
# print(result)

## list comphension

# result=[]
# for i in range(1,11):
    
#     result.append(i*i)
    
# print(result)


## actual list comprehension:

# result=[i*i for i in range(1,11)]
# print(result)



# in_string="bongodev"
# result=[letter*2 for letter in in_string]
# print(result)
    

## prime number:
   


# def is_prime(n):
#     if n<2:
#         return False

#     for i in range (2,n-1):
       
#         if n%i==0:
#             return False
#     return True


# def printPrimeInRange(mn,mx):
#     for i in range(mn,mx+1):
#         if is_prime(i):
#             print(i)
# print(printPrimeInRange(1,14))

#### making set with union:


# def make_set():

#     n=int(input("enter the nmbr of digit:"))
#     in_array=[]

#     for i in range(n):
#         number=int(input("enter the array value number:"))
#         in_array.append(number)

#     print(in_array)
#     in_set=set(in_array)
#     return in_set
    
# one=make_set()
# two=make_set()

# print("union:", one.union(two))
# print("intersection",one.intersection(two))
# print("difference",one.difference(two))


##find max value



# def max(n):
#     if len(n)<2:
#         return n[0]
    
#     a=n[0]
#     b=n[1]
#     bigger= a if a>b else b
#     p=n[2:]
#     p.append(bigger)
    
#     print(p)

#     return max(p)

# result= max([2,6,9,33])
# print("result:",result)




def max(n):

    if len(n)<2:
        return n[0]
    
    a=n[0]
    b=n[1]
    bigger=a if a>b else b
    p=n[2:]
    p.append(bigger)
    print(p)
    return max(p)
result=max([44,3,6,9,2,1,11,33])
print ("result",result)


