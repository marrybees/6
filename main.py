# class Currency:
#
#         def __init__(self,value, unit = None):
#             self.value = value
#             if unit is not None:
#               self.unit = "Gel"
#         def __str__(self):
#            return   f" {self.value}.00 {self.uni} "
#         def changeTo(self,eur = None):
#             if eur is not None:
#                 self.eur = self.unit * 3
#         def
#
#




#2
class Person:
    def __init__(self,name,deposit = 1000,loan =0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
    def __str__(self):
         return f" saxeli {self.name}, deposit {self.deposit}, loania {self.loan}"

mepatrone = Person("joni")
myidveli = Person("petre")
class House:
    def __init__(self,id,price,owner,status):
        self.id = id
        self.price = price
        self.owner = owner
        self.status = status
    def sell_house(self, myidveli = None,ricxvi = 100):
        self.loan = ricxvi
        self.myidveli = myidveli
    if myidveli is not None:
        self.deposit += self.price
        self.status = "gayidulaia"
    def funqcia(self):
        print(f" {self.loan},{self.myidveli},{self.deposit},{self.status}")

# #3
# class Plane:
#     def move(self):
#         print("plane can fly")
#     def speed(self):
#         print("its speed is up to 900km/h")
# class Bus:
#     def move(self):
#         print("bus can move on roads")
#     def speed(self):
#         print("its speed is up to 180km/h")
#
# def movement(obj):
#     obj.move()
#     obj.speed()
# x = Plane()
# y = Bus()
# movement(x)
# movement(y)
#



