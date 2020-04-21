
class Affine:

    def __init__(self, text, k1=7, k2=2, mod=26):

        self.text = text
        self.mod = mod
        self.k1 = k1
        self.k2 = k2
    
    def multInverse(self):
        try:
            return [i for i in range(self.mod) if i * self.k1 % self.mod == 1][0]
        except:
            return None

    def encode(self):
        """ C = (P * k1 + k2) % 26 """
        print("C = (P * K1 + k2) % {}".format(self.mod))
        out = ""
        for i in self.text:
            if i.isupper():
                out += chr(((ord(i) - 65) * self.k1 + self.k2) % self.mod + 65) 
            else:
                out += chr(((ord(i) - 97) * self.k1 + self.k2) % self.mod + 97) 
            print("{} = ({} * {} + {}) mode 26 = {} = {}".format(i, ord(i.lower())-97, self.k1, self.k2, ord(out[-1].lower())-97, out[-1]))
        return out

    def decode(self):
        """ P = ((C - k2) * ink1) % 26 """
        print("P = (C - k2 * ink1) % {}".format(self.mod))    
        self.ink1 = self.multInverse()
        if self.ink1 == None: raise BaseException("{} (k1) has no multiplicative inverse in mod {}".format(self.k1, self.mod))

        out = ""
        for i in self.text:
            if i.isupper():
                out += chr((((ord(i) - 65) - self.k2) * self.ink1) % self.mod + 65) 
            else:
                out += chr((((ord(i) - 97) - self.k2) * self.ink1) % self.mod + 97)
            print("{} = ({} - {} * {}) mode 26 = {} = {}".format(i, ord(i.lower())-97, self.k2, self.ink1, ord(out[-1].lower())-97, out[-1]))
        return out

e = Affine(str(input("Enter Your Text: ")), int(input("Enter Key 1 : ")), int(input("Enter Key 2 : ")), int(input("Mod : ")))
c = e.encode()
print("Encode : " + c)

d = Affine(c, e.k1, e.k2, e.mod)
print("Decode : " + d.decode())

