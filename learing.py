# IceCream Class
# class IceCream:
#     print('IceCream Class Working')

#     def __init__(self):
#         self.scoops = 3

#     def add(self, scoops):
#         self.scoops += scoops

#     def eat(self, scoops):
#         if self.scoops > scoops:
#             self.scoops -= scoops
#         else:
#             print("No More IceCream left! ")


# scoops = 3
# ice_cream = IceCream()
# ice_cream.eat(scoops)

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


class Light:
    on = False


a = Light()
a.on = True
Light.on = True
b = Light()
print("b.on: ", b.on)
print("a.on: ", a.on)
print(Light.on)