## read all files in directory
## get a list of rolls who has submitted
## check from input if they are submitted

# import os
# files=os.listdir("submissions")

# submitted_roll=[]

# for file in files:
#     divs=file.split("_")
#     if len(divs)>1:

#         roll=divs[1]
#         submitted_roll.append(roll)

# while True:

#     roll_in_check=input("plz enter which roll to check:")

#     if roll_in_check=="q":
#         print("exiting the prgrm")
#         exit(0)


#     if roll_in_check in submitted_roll:
#         print(f"roll {roll_in_check} has submitted their work!")
#     else:
#         print('backbencher')


# import os

# # List files in the "submissions" folder
# files = os.listdir("submissions")

# # Extract roll numbers from the filenames
# submitted_roll = []

# for file in files:
#     divs = file.split("_")
#     if len(divs) > 1:  # Ensure the filename has the expected format
#         roll = divs[1]
#         submitted_roll.append(roll)

# # Check if a specific roll number has submitted
# roll_in_check = input("Please enter the roll number to check: ").strip()

# if roll_in_check in submitted_roll:
#     print(f"Roll number {roll_in_check} has submitted their work!")
# else:
#     print("Backbencher!")


# import os
# files=os.listdir("submissions")

# submitted_roll=[]

# for file in files:
#     divs=file.split("_")
#     if len(divs)>1:
#         roll=divs[1] 
#         submitted_roll.append(roll)

# while True:
#     check_roll=input("enter the roll: ")

#     if check_roll=="x" :
#         print("completly exit")
#         exit(0)
    
#     if check_roll in submitted_roll:
#         print(f"this roll {check_roll} has been submitted")
#     else:
#         print("backbencher")






import os
files=os.listdir("submissions")

submitted_roll=[]

for file in files:
    divs=file.split("_")
    if len(divs)>1:
        roll=divs[1]
        submitted_roll.append(roll)

try:       
    while True:
        check_roll=input('enter the roll:')

        if check_roll=="x":
            raise KeyboardInterrupt
        

        if check_roll in submitted_roll:
            print(f"the roll {check_roll} has been submitted")
        else:
            print("backbancher")
except KeyboardInterrupt:
    print("\n thank u ")
    exit(0)