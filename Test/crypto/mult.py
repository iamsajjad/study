
cce = lambda text, k: ''.join([chr((ord(i) + k) % 97) if i.isupper() else chr((ord(i) + k) % 122) for i in text])
ccd = lambda text, k: ''.join([chr((ord(i) - k) % 97) if i.isupper() else chr((ord(i) - k) % 122) for i in text])

x = cce("Sajjad", 3)
print(x)
print(ccd(x, 3))

#***************************************************************************************************************

print("Mult ","*" * 80)

def multEncode(text, key):
    return ''.join([chr((ord(i) * key - 65) % 26 + 65) if i.isupper() else chr((ord(i) * key - 97) % 26 + 97) for i in text])
    
def multDecode(text, key, mod):

    def modIn(key, mod):

        key = key % mod
        for i in range(1, mod):
            if (key * i) % mod == 1:  return i
        return 1

    inkey = modIn(key, mod)
    return ''.join([chr((ord(i) * inkey - 65) % 26 + 65) if i.isupper() else chr((ord(i) * inkey - 97) % 26 + 97) for i in text])

x = multEncode("HelloGroupB", 7)
print(x)
print(multDecode(x, 7, 26))

#***************************************************************************************************************
