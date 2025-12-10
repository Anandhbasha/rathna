# # car1Milage = 18
# # noofWheels = 4
# # airbags = 6
# # mirror = 2
# # varient = "diesel"
# # carName = "swift"

# # def acc():
# #     print(carName,"Moves")

# # def brake():
# #     print(carName,"stops")


# # class cars:
# #     car1Milage = 18
# #     noofWheels = 4
# #     airbags = 6
# #     mirror = 2
# #     varient = "diesel"
# #     carName = "swift"

# #     def acc(self):
# #         print(self.carName,"Moves")

# #     def brake(self):
# #         print(self.carName,"stops")


# # c1= cars()
# # c1.carName = "dzire"
# # c1.car1Milage = 22

# # print(c1.car1Milage)
# # c1.acc()

# # c2 = cars()  #instence object create 
# # c2.carName = "ALTO"
# # c2.car1Milage = 21
# # print(c2.car1Milage)
# # c2.brake()




# # encapsulation
#     #protected
#     #_
#     #public
#     #private
#     # __
# class bankaccount:
#     __balance = 0
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdrar(self,amount):
#         if self.__balance>amount and amount>0:
#             self.__balance-=amount
#         else:
#             print("Insufficient Balance")

#     def balance(self):
#         return self.__balance
    
# bal = bankaccount()
# bal.withdrar(500)
# print(bal.balance())
# # bal.__balance = 1000
# # print(bal.__balance)
# print(bal.balance())
# # abstraction
# # inheritence
# # polymorphism


# abstraction
# from abc import ABC,abstractmethod

# class abstraction(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class gpay(abstraction):
#     def pay(self):
#         print("Payment succesfull via Gpay")
# class Phonepe(abstraction):
#     def pay(self):
#         print("Payment succesfull via PhonePay")

# googlepay = gpay()
# googlepay.pay()


# inheritence
# simple
# class Restaraunt:
#     def order(self):
#         print("You have ordered from res")
# class vegRes(Restaraunt):
#     def orders(self):
#         print("Ordered from Res")

# r = vegRes()
# r.order()


# # multilevel
# class grandpa:
#     def a(self):
#         print("This is GrandPa")
# class father(grandpa):
#     def b(self):
#         print("This is father")
# class son(father):
#     def c(self,gender):
#         print("This is son his gender is:",gender)

# s = son()
# s.a()
# s.b()
# s.c("male")



# multiple
# class dad:
#     def money(self):
#         print("Money from dad")
# class mom:
#     def love(self):
#         print("love from dad")
# class son (dad,mom):
#     pass

# s = son()
# s.love()
# s.money()


# # hierarchical 

# class vehicle:
#     def acc(self):
#         print("Vehicle moves")
# class bike(vehicle):
#     pass
# class car(vehicle):
#     pass

# c = car()
# b=bike()
# c.acc()
# b.acc()



# hybrid
class vehicle:
    def start(self):
        print("Vehicle started")
class bike(vehicle):
    def bike_info(self):
        print("This Bike")
class Evehicle(vehicle):
    def battery(self):
        print("Battery vehicle")
class Ecar(Evehicle):
    def ecars(self):
        print("Ecars moving")


