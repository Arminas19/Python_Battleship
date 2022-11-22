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
class light:
    def __init__(self, sync=None):
        super().__init__()
        print('creating light! ')
        self.sync = sync
        self.on = False
    
    def toggle(self):
        print('Toggle on and off!')
        self.on = not self.on 
        if self.sync is not None:
            self.sync.toggle()
    
    def is_on(self):
        if self.on == True:
            print("Light is on!")
        else:
            print("Light is off!")


class OldLight(light):

  def __init__(self, sync=None):
    super().__init__(sync=sync)
    self.on = False
    self.sync = sync
    self.flicker = False
  
  def toggle(self):
    super().toggle()
    if self.on:
      self.flicker = not self.flicker


class Timer:

  def __init__(self):
    self.left = 0

  def set(self, left):
    self.left = left

  def ring(self):
    print("Timer is up!")

  def elapse(self, t):
    if self.left > 0:
      self.left = max(self.left - t, 0)
      if self.left == 0:
        self.ring()


class TimerLight(light, Timer):

  def set(self, left):
    super().set(left)
    if self.left > 0:
      self.on = True

  def ring(self):
    super().ring()
    self.on = False


# timer = Timer()
# timer.set(5)
# timer.elapse(3)
# timer.elapse(3)
# print(timer.left)

timer_light = TimerLight()
timer_light.set(5)
timer_light.is_on()
timer_light.elapse(3)
timer_light.is_on()
timer_light.elapse(3)
timer_light.is_on()

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
class IceCream:

  max_scoops = 3 # add a class attribute (introduced before)

  def __init__(self):
    super().__init__()
    self.scoops = 0

  def eat(self, scoops):
    if self.scoops < scoops:
      print("Not enough bites left!")
    else:
      self.scoops -= scoops

  def add(self, scoops):
    self.scoops += scoops
    if self.scoops > self.max_scoops: # current step - add logic
      print("Too many scoops! Dropped ice cream.")
      self.scoops = 0


class IceCreamTruck:  # current step - add IceCreamTruck class
  
  def __init__(self):
    super().__init__()
    self.sold = 0

  def order(self, scoops):
    ice_cream = IceCream()
    self.add(ice_cream, scoops)
    return ice_cream

  def add(self, ice_cream, scoops):
    ice_cream.add(scoops)
    self.sold += scoops


class DeluxeIceCreamTruck(IceCreamTruck):
    
    def order(self, scoops):
        ice_cream = super().order(scoops)
        ice_cream.add(1)
        return ice_cream


class Drinkable:

  def __init__(self):
    self.cups = 0

  def add(self, cups):
    self.cups += cups

  def drink(self, cups):
    self.cups -= cups


class Lemonade(Drinkable):
  pass
    

class MeltingIceCream(IceCream, Drinkable):
  
  def elapse(self, t):
    melted = min(t, self.scoops)
    self.scoops -= melted
    self.cups += melted


# ice_cream = MeltingIceCream()
# ice_cream.add(3)
# ice_cream.elapse(2)
# print('Ice_cream scoops: ', ice_cream.scoops)
# print('iceCream cups: ', ice_cream.cups)
# ice_cream.drink(1)
# print('drank 1 ice cream, how many iceCream cups left?:', ice_cream.cups)

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

# MRO example
# class A:
#   pass

# class B(A):
#   pass

# class C(A, B):
#   pass