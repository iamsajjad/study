
class Crypto:
    
    def __init__(self, text='Hello There !!', key=5, exp=False):
        self.text = text
        self.key = key
        self.exp = exp
    
    def toggle(self, bins):
        return ''.format([ '1' if i == '0' else '0' for i in bins])

    def encode(self):
        binText = [format(ord(i), 'b') for i in self.text]
        binText = [str(int(8-len(i)) * '0') + i for i in binText]
        
        if self.exp == True:
            for i,j in enumerate(binText):
                print("'{}' is '{}'".format(self.text[i], j))
        
        binTable = [str(int(8-len(str(bin(i))[2:])) * '0') + str(bin(i + self.key))[2:] for i in range(len(binText))]
        binTable = [bin(int(i, 2))[2:] for i in binTable]
        
        if self.exp == True:
            for i,j in enumerate(binTable):
                print('{} + {} = {}'.format(self.key, i, j))

        cryptoText = []
        
        for i in range(len(binText)):
            cryptoText.append('{0:b}'.format(int(binText[i], 2) + int(binTable[i], 2)))

        if self.exp == True:
            for i in range(len(self.text)):
                print('{} + {} = {}'.format(binText[i], binTable[i], cryptoText[i]))

        return ''.join([chr(int(i, 2) % 1_114_112) for i in cryptoText])

    def decode(self):
        binText = [format(ord(i), 'b') for i in self.text]
        binText = [str(int(8-len(i)) * '0') + i for i in binText]
        
        if self.exp == True:
            for i,j in enumerate(binText):
                print("'{}' is '{}'".format(self.text[i], j))

        binTable = [str(bin(i + self.key))[2:] for i in range(len(binText))]
        binTable = [bin(int(i, 2))[2:] for i in binTable] 
        if self.exp == True:
            for i,j in enumerate(binTable):
                print('{} + {} = {}'.format(self.key, i, j))

        cryptoText = []
        
        for i in range(len(binText)):
            cryptoText.append('{0:b}'.format(int(binText[i], 2) - int(binTable[i], 2)))

        if self.exp == True:
            for i in range(len(self.text)):
                print('{} - {} = {}'.format(binText[i], binTable[i], cryptoText[i]))

        return ''.join([chr(int(i, 2) % 1_114_112) for i in cryptoText])



text = 'here !!'
print(text)
print(Crypto(text, key=23, exp=True).encode())
code = Crypto(text, key=23).encode()
print(Crypto(code, key=32, exp=True).decode())
