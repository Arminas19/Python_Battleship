# IceCream Class
class IceCream:
    max_scoops = 3

    def __init__(self):
        self.scoops = 3

    def add(self, scoops):
        self.scoops += scoops
        if self.scoops > self.max_scoops:
            self.scoops = 0
            print("Too many scoops! Dropped ice cream.")

    def eat(self, scoops):
        if self.scoops > scoops:
            self.scoops -= scoops
        else:
            print("No More IceCream left! ")


# ice_cream = IceCream()
# ice_cream.scoops += 2
# ice_cream.add(2)
# ice_cream.scoops -= 3
# ice_cream.eat(3)

# IceCreamTruck Class
class IceCreamTruck:
    def __init__(self):
        self.sold = 0

    def order(self, scoops):
        ice_cream = IceCream()
        self.add(ice_cream, scoops)
        return ice_cream

    def add(self, ice_cream, scoops):
        ice_cream.add(scoops)
        ice_cream.add(scoops)
        self.sold += scoops

truck = IceCreamTruck()
ice_cream1 = truck.order(3)
ice_cream1.eat(2)
truck.add(ice_cream1, 1)
print(truck.sold)



# Light Class
# class light:
#     def __init__(self):
#         print('creating light! ')
#         self.on = False
    
#     def toggle(self):
#         print('Toggle on and off!')
#         self.on = not self.on 
    
#     def is_on(self):
#         if self.on == True:
#             print("Light is on!")
#         else:
#             print("Light is off!")

# Light = light()
# Light.is_on()
# # print("Light on?: ", Light.on)
# Light.toggle()
# # print("Light on?: ", Light.on)
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