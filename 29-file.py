# with open("example-moja.txt","w") as file:
#     print(file.write("shauya"))

# with open("example-moja.txt","r") as file:
#     print(file.read())


# with open("example-moja.txt","w") as file:
#     file.write("new ")





file = open("example-moja.txt","r")
for line in file:
    letters=[letter for letter in line]
    print(letters)
file.close()