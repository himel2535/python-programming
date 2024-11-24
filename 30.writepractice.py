# filename="pi.txt"

# with open(filename,"r") as file:
#     print(file.read())


filename="write_practice.txt"

with open(filename,"w") as file:
    file.write("this is bongodev\n")
    file.write("this is very cool today\n")

with open(filename,"a") as file:
    file.write("this is moja\n")