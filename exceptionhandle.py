# try:
#     a=int(input("enter :"))
#     print(a)
# except ValueError as e:
#     print(e)
# except TypeError as e1:
#     print("type_error",e1)
# except :
#     print("error")
# finally:
#     print("done ")
# else can used in for  ,try also and  if exception execute then else not execute 
# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else: 
#     print("done")
# with open("file.txt","w") as f:
#   f.write("hello world")
# with open("file.txt","r") as f:
#    print(f.read())
# with open("file.txt","a")as f:
#     f.write("\n vamsi ")
# x=int(input("enter a number:"))
# if x<0:
#     raise ValueError("number should be positive")
# print(x)
# class hello():
#     def __init__(self,name,age,city):
#         self.nam=name
#         self._age=age
#         self.__city=city
#     def get(self):
#         return self.__city
#     def set(self,city):
#         self.__city=city
# d=hello("aakesh",55,"Chicken in Alaska")
# print(d.get())
# print(d._age)
# print(d.nam)
# class Animal():
#     def sound1(self):
#         print("animal  makes noise")
# class cat(Animal):
#     def sound(self):
#         print("meow "*5)
# class dog(Animal):
#     def sound(self):
#         print("bark"*6)
# d=Animal()
# d2=cat()
# d2.sound1()
# d2.sound()
# d.sound1()
# from abc import abstractmethod,ABC
# class BankAccount(ABC):
#     def __init__(self,balance):
#         self.__balance=balance
#     def withdraw(self,amount):
#         self.balance -=amount
#     def deposit(self,amount):
#         self.balance +=amount
#     def getbalance(self):
#         return self.__balance
#     def setbalance(self,balance):
#         self.__balance=balance
# @abstractmethod
# def interestcal(self):
#     pass
# class SavingAccount(BankAccount):
#     def interestcal(self):
#         return 0.03*self.__balance
# s=SavingAccount(100)
