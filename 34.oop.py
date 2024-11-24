
######     practice

# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age 
    
#     def eat(self,menu):
#         print(f"{self.name} is now eating {menu}" )
#     def sleep(self):
#         print(f"{self.name} is now sleeping")

# my_cat=Cat("surprise",4)     
# print("here the name:", my_cat.name) 
# print("this is age: ",my_cat.age)
# my_cat.eat("fish")
# my_cat.sleep()


####       practice

# class Dog:

#     def __init__(self, name, age):  
#         self.nm = name
#         self.boyosh = age

#     def bark(self):
#         print("bark bark!")

#     def doginfo(self):
#         print(self.nm + " is " + str(self.boyosh) + " year(s) old.")

# ozzy = Dog("Ozzy", 2)
# skippy = Dog("Skippy", 12)
# filou = Dog("Filou", 8)

# ozzy.doginfo()
# skippy.doginfo()
# filou.doginfo()

#####     practice

# class religion:

#     def __init__ (self,name,rasul,location):
#         self.nm=name
#         self.nobi=rasul
#         self.lctn=location

#     def procar(self):
#         print(f"this religion {self.nm} follow the great {self.nobi} and his location is:{self.lctn}")

    


# muslim=religion("islam","hazrat_mohammad_saw","arab")
# muslim.procar()

# cristiani=religion("cristian","jasus aws","jarujalem")
# cristiani.procar()

# bouddist=religion("Bouddhaw","gautam bouddhaw","china,srilanka")
# bouddist.procar()

# jionist=religion("ihudi","musa aws","mishor")
# jionist.procar()



#####    encapsulation:

##       public-private:


# class Car:

#     def __init__(self,colour,brand):
#         self.clr=colour   ##public
#         self.__brand=brand ##private
#         ###   getter fnctn
#     def get_brand(self):
#         return self.__brand
#         ###   setter fnctn
#     def set_brand(self,brand):
#         self.__brand=brand

# moja=Car("red","ferrary")

# print(moja.clr)
# ############  print(moja.__brand)-> ti's never will be work bcz of its private fnctn
# print(moja.get_brand())

# moja.__brand="marchedes"
# print(moja.get_brand())

# moja.set_brand("tesla")
# print(moja.get_brand())

##                                              inheritance::


# class Persion:
    
#     def __init__(self,fname,lname,age):
#         self.firstname=fname
#         self.lastname=lname
#         self.age=age
#     def printname(self):
#         print(self.firstname,self.lastname)
#     def age(self):
#         print(self.age)

# class Student(Persion):

#     def __init__(self,fname,lname,age,id):
#         super().__init__(fname, lname,age)
#         self.id=id

#     def wlcm(self):
#         print("the man", self.firstname, self.lastname,"id is:",self.id , "who is",self.age, "years old")


# x=Student("monwar","hossan",26,2535)
# y=Student("tamanna","rahman",25,121090)
# x.wlcm()
# y.wlcm()


                               ## polymorphism


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()