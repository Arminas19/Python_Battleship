class IceCream:
    print('IceCream Class Working')

    def __init__(self):
        self.scoops = 3

    def add(self, scoops):
        self.scoops += scoops

    def eat(self, scoops):
        if self.scoops > scoops:
            self.scoops -= scoops
        else:
            print("No More IceCream left! ")


# scoops = 3
# ice_cream = IceCream()
# ice_cream.eat(scoops)


