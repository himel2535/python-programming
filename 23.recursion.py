
#recursive function
# a function that calls itself


#     recursive case

# def function():
#     print('hello')
#     function()
# function()

# def base_case(a):
#     print('we got',a)
#     if a==0:
#         return
#     base_case(a-1)
# base_case(100)
 

# def x(a):
#     print(a)
#     if a<0:
#         return
    
#     x(a-10)
# x(99)

# def x(a):
 
#     if a<0:
#         return
#     print(a)
#     x(a-10)
# x(99)

# def x(a):
 
#     if a>1000:
#         return
#     print(a)
#     x(a*10)
# x(5)


#xmple with factorial

# def factorial(n):
#     if n==0:
#         return 1
#     return n * factorial(n-1)
# result = factorial(5)
# print (result)
    

# def x(n):
#     if n==0:
#         return 1
#     return n * x(n-1)
# result = x(5)
# print (result)

# def sum(n) :
#     if n==0:
#         return 0
#     return n + sum(n-1)
# print(sum(5))

# def find_palindrome(input):
#     if len(input)<=1:
#         return True
#     if input[0]==input[-1]:
#         return find_palindrome(input[1:-1])
#     return False
# print(find_palindrome('radar'))


# fibonacci

# def  fibonacci(n):
#     if n==0:
#         return 0
    
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(9))



#reverse

# def reverse_string(s):
#     # Base case: if the string is empty or has only one character, return it as is
#     if len(s) <= 1:
#         return s
#     # Recursive case: return the last character + reverse of the remaining string
#     else:
#         return s[-1] + reverse_string(s[:-1])

# # Test the function
# print(reverse_string("hello"))  # Output: "olleh"



# def string(n):
#     if len(n)<=1:
#         return n
#     else:
#         return n[-1]+string(n[:-1])
# print(string('vallagena'))

# def reverse(n):
#     if len(n)<=1:
#         return n
   
#     n[0],n[-1]=n[-1],n[0]
#     return reverse(n[1:-1])

# print(reverse('hello'))