# try:
#     result=5+'ten'
# except:
#     print('error occured')
# else:
#     print(result)
# finally:
#     print('code finally finished')

# try:
#     result=10/0
# except (ZeroDivisionError,TypeError) as error:
#     print('error occured')
#     print('details error:',error)
# else:
#     print('addition succesfull')
# finally:
#     print('code finally finished')


# def check_age(age):
#     if age<0:
#         raise ValueError('age cannot be negative')
#     return 'welcome to the club'

# age_input=int(input('enter the age:'))

# try:
#     mssg=check_age(age_input)
# except ValueError as e:
#     print('error here:', e)
# else:
#     print(mssg)
# finally:
#     print('finally done')




