# IceCream Class
# class IceCream:
#     max_scoops = 3

#     def __init__(self):
#         self.scoops = 3

#     def add(self, scoops):
#         self.scoops += scoops
#         if self.scoops > self.max_scoops:
#             self.scoops = 0
#             print("Too many scoops! Dropped ice cream.")

#     def eat(self, scoops):
#         if self.scoops > scoops:
#             self.scoops -= scoops
#         else:
#             print("No More IceCream left! ")


# ice_cream = IceCream()
# ice_cream.scoops += 2
# ice_cream.add(2)
# ice_cream.scoops -= 3
# ice_cream.eat(3)

# IceCreamTruck Class
# class IceCreamTruck:
#     def __init__(self):
#         self.sold = 0

#     def order(self, scoops):
#         ice_cream = IceCream()
#         self.add(ice_cream, scoops)
#         return ice_cream

#     def add(self, ice_cream, scoops):
#         ice_cream.add(scoops)
#         ice_cream.add(scoops)
#         self.sold += scoops

# truck = IceCreamTruck()
# ice_cream1 = truck.order(3)
# ice_cream1.eat(2)
# truck.add(ice_cream1, 1)
# print(truck.sold)

# Class Sub
# def sub(x, y):
#     return x - y

# def sub2(x, y=0):
#     return x - y

# print(sub2(7))

# Light Class
# class light:
#     def __init__(self, sync=None):
#         super().__init__()
#         print('creating light! ')
#         self.sync = sync
#         self.on = False
    
#     def toggle(self):
#         print('Toggle on and off!')
#         self.on = not self.on 
#         if self.sync is not None:
#             self.sync.toggle()
    
#     def is_on(self):
#         if self.on == True:
#             print("Light is on!")
#         else:
#             print("Light is off!")


# class OldLight(light):

#   def __init__(self, sync=None):
#     super().__init__(sync=sync)
#     self.on = False
#     self.sync = sync
#     self.flicker = False
  
#   def toggle(self):
#     super().toggle()
#     if self.on:
#       self.flicker = not self.flicker


# light = OldLight()
# print(light.flicker)
# light.toggle()
# print(light.flicker)
# light.toggle()
# print(light.flicker)
# light.toggle()
# print(light.flicker)
# Light = light()
# Light.is_on()
# print("Light on?: ", Light.on)
# Light.toggle()
# print("Light on?: ", Light.on)
# Light.is_on()


# class Light:
#     on = False


# a = Light()
# a.on = True
# Light.on = True
# b = Light()
# print("b.on: ", b.on)
# print("a.on: ", a.on)
# print(Light.on)

# Light1 = light()
# Light2 = light(sync=Light1)
# Light1.is_on()
# Light2.toggle()
# Light1.is_on()
# Light2.is_on()

# Inheritance concept
# class IceCream:

#   max_scoops = 3 # add a class attribute (introduced before)

#   def __init__(self):
#     super().__init__()
#     self.scoops = 0

#   def eat(self, scoops):
#     if self.scoops < scoops:
#       print("Not enough bites left!")
#     else:
#       self.scoops -= scoops

#   def add(self, scoops):
#     self.scoops += scoops
#     if self.scoops > self.max_scoops: # current step - add logic
#       print("Too many scoops! Dropped ice cream.")
#       self.scoops = 0


# class IceCreamTruck:  # current step - add IceCreamTruck class
  
#   def __init__(self):
#     super().__init__()
#     self.sold = 0

#   def order(self, scoops):
#     ice_cream = IceCream()
#     self.add(ice_cream, scoops)
#     return ice_cream

#   def add(self, ice_cream, scoops):
#     ice_cream.add(scoops)
#     self.sold += scoops


# class DeluxeIceCreamTruck(IceCreamTruck):
    
#     def order(self, scoops):
#         ice_cream = super().order(scoops)
#         ice_cream.add(1)
#         return ice_cream


# truck = IceCreamTruck()
# ice_cream1 = truck.order(3)
# ice_cream1.eat(2)
# truck.add(ice_cream1, 1)
# print(truck.sold)

# truck = DeluxeIceCreamTruck()
# ice_cream = truck.order(2)

# print('Deluxe IceCream truck scoops: ', ice_cream.scoops)
# print(truck.sold)

# 2 parent classes

class A:
  pass

class B(A):
  pass

class C(A, B):
  pass