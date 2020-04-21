
def multEncode(text, key, mod):
    out = ""
    print("C = (P * k) mode {}".format(26))
    for i in text:
        if i.isupper():
            out += chr((ord(i) - 65 ) * key % mod + 65)
        else:
            out += chr((ord(i) - 97 ) * key % mod + 97)
        print("{} = ({} * {}) mode 26 = {} = {}".format(i, ord(i.lower())-97, key, ord(out[-1].lower())-97, out[-1]))

    return out
    
def multDecode(text, key, mod):

    print("P = (C * ink) % mode {}".format(26))
    def modIn(k, mod):
        try:
            return [i for i in range(mod) if i * k % mod == 1][0]
        except:
            return None

    inkey = modIn(key, mod)
    out = ""
    for i in text:
        if i.isupper():
            out += chr((ord(i) - 65 ) * inkey % mod + 65)
        else:
            out += chr((ord(i) - 97 ) * inkey % mod + 97)
        print("{} = ({} * {}) mode 26 = {} = {}".format(i, ord(i.lower())-97, inkey, ord(out[-1].lower())-97, out[-1]))
    return out

text, key, mod = "Security", 19, 26

x = multEncode(text, key, mod)
print(x)
print(multDecode(x, key, 26))

