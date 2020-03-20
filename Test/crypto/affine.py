
class Affine:

    def __init__(self, text, k1=7, k2=2):

        self.text = text
        self.k1 = k1
        self.k2 = k2
    
    def multInverse(self):
        try:
            return [i for i in range(26) if i * self.k1 % 26 == 1][0]
        except:
            return None

    def encode(self):
        """ C = (P * k1 + k2) % 26 """
        return ''.join([ chr(((ord(i) - 65) * self.k1 + self.k2) % 26 + 65) if i.isupper() else 
                         chr(((ord(i) - 97) * self.k1 + self.k2) % 26 + 97) for i in self.text])

    def decode(self):
        """ P = ((C - k2) * ink1) % 26 """
        self.ink1 = self.multInverse()
        if self.ink1 == None: raise BaseException("{} (k1) has no multiplicative inverse in mod 26".format(self.k1))
        return ''.join([ chr((((ord(i) - 65) - self.k2) * self.ink1) % 26 + 65) if i.isupper() else 
                         chr((((ord(i) - 97) - self.k2) * self.ink1) % 26 + 97) for i in self.text])

e = Affine(str(input("Enter Your Text: ")), int(input("Enter Key 1 : ")), int(input("Enter Key 2 : ")))
print("Encode : " + e.encode())

d = Affine(e.encode(), e.k1, e.k2)
print("Decode : " + d.decode())

