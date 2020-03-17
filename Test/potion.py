
class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
        self.R, self.G, self.B = self.color

    def mix(self, other):
        mixv = [self.volume, other.volume]
        maxPercent = max(mixv) / sum(mixv)
        minPercent = min(mixv) / sum(mixv)
        R = int(max(self.R, other.R) * maxPercent) + int(min(self.R, other.R) * minPercent)
        G = int(max(self.G, other.G) * maxPercent) + int(min(self.G, other.G) * minPercent)
        B = int(max(self.B, other.B) * maxPercent) + int(min(self.B, other.B) * minPercent)
        potion = (R, G, B)
        #print(potion,'------>', mixv, '------>', maxPercent)
        return Potion(potion, sum(mixv))

x = Potion([255, 255, 0], 10)
z = Potion([0, 254, 0], 5)

new = x.mix(z)

potions = [
    Potion((153, 210, 199), 32),
    Potion((135,  34,   0), 17),
    #(147, 149, 130)
    Potion((18,   19,  20), 25),
    Potion((174, 211,  13),  4),
    Potion((255,  23, 148), 19),
    Potion((51,  102,  51),  6)
]
a = potions[0].mix(potions[1])
b = potions[0].mix(potions[2]).mix(potions[4])
c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])

print(a.color)
print((147, 149, 130))
