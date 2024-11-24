# password="admin123"

# def checkpassword(password):
#     if len(password)<8 or len(password)>20:
#         return False
    
#     lowerace=0
#     upperache=0
#     digitache=0

#     for letter in password:
#         if letter.islower():
#             lowerache=1
#         if letter.isupper():
#             upperache=1
#         if letter.isdigit():
#             digitache=1

#     if lowerache==0 or upperache==0 or digitache==0:
#         return False
    
#     return True

# if checkpassword(password):
#     print("good password")
# else:
#     print("bad password") 




# p="admiN123"
try:
    while True:
        

        p=input(f"getting password:")

        if p=="x":
            raise KeyboardInterrupt
        
        def cp(p):
            if len(p)<8 or len(p)>20:
                return False
            f1=0
            f2=0
            f3=0
            for l in p:
                if l.islower():
                    f1=1
                if l.isupper():
                    f2=1
                if l.isdigit():
                    f3=1
            if f1==0 or f2==0 or f3==0:
                return False


            return True

        if cp(p):
            print("gd psswrd")
        else:
            print("bd psswrd")


except KeyboardInterrupt:
    print("\nthnks for ending")
    exit(0)