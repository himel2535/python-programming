# input_list=[1,2,3,4,5,6,7,8,9,10]
# def function_for_apply(x):
#     return x*x
# output_list=map(function_for_apply,input_list)
# print(list(output_list))




# def function_for_apply(x):
#     return x * x

# # Taking input as a space-separated string and splitting it to create a list
# input_list = list(map(int, input('Enter the list elements separated by spaces: ').split()))

# # Applying the function to each element in the input list using map
# output_list = map(function_for_apply, input_list)

# # Converting the output to a list and printing it
# print(list(output_list))




# def sqr(x):
#     return x*x
# input_list=list(map(int,input('enter:').split()))
# output_list=map(sqr,input_list)
# print(list(output_list))



temperature_c=[0,25,30,35]

def c2f(c):
    return (c*9/5)+32

temperature_f=list(map(c2f,temperature_c))
print(list(temperature_f))



# def c2f(c):
#     return (c*9/5)+32

# t_in_c=list(map(int,input('enter the list of celcius:').split()))
# t_in_f=list(map(c2f,t_in_c))
# print("temperature in farenhite:",t_in_f)


#same thing by loop:

# tempc=[0,25,30,35]
# def c2f(c):
#     return (c*9/5)+32

# tempf=[]

# for i in tempc:
#     f=c2f(i)
#     tempf.append(f)
# print(tempf)