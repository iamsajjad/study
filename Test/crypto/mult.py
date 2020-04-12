"""

C = (P + k) % 26
P = (C - k) % 26

C = (P * k) % 26
P = (C * ink) % 26

C = (P * K1 + k2) % 26
P = (C - k2 * ink1) % 26

"""
cce = lambda text, k: ''.join([chr((ord(i) + k) % 97) if i.isupper() else chr((ord(i) + k) % 122) for i in text])
ccd = lambda text, k: ''.join([chr((ord(i) - k) % 97) if i.isupper() else chr((ord(i) - k) % 122) for i in text])

x = cce("Sajjad", 1)
print(x)
print(ccd(x, 1))

#***************************************************************************************************************

def multEncode(text, key):
    return ''.join([chr((ord(i) - 65 ) * key % 26 + 65) if i.isupper() else chr((ord(i) - 97 ) * key % 26 + 97)  for i in text])
    
def multDecode(text, key, mod):

    def modIn(k, mod):
        try:
            return [i for i in range(mod) if i * k % mod == 1][0]
        except:
            return None

    inkey = modIn(key, mod)
    return ''.join([chr((ord(i) - 65) * inkey % 26 + 65) if i.isupper() else chr((ord(i) - 97) * inkey % 26 + 97) for i in text])

x = multEncode("Security", 11)
print(x)
print(multDecode(x, 11, 26))

#***************************************************************************************************************

def multInverse(k, mode):
    try:
        return [i for i in range(mode) if i * k % mode == 1][0]
    except:
        return None

print("multInv : " + str(multInverse(3, 26)))

