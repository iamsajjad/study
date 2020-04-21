
#def cc(text, k): return ''.join([chr((ord(i) + k) % 97) if i.isupper() else chr((ord(i) + k) % 122) for i in text])

#cce = lambda text, k: ''.join([chr((ord(i) + k) % 97) if i.isupper() else chr((ord(i) + k) % 122) for i in text])

#ccd = lambda text, k: ''.join([chr((ord(i) - k) % 97) if i.isupper() else chr((ord(i) - k) % 122) for i in text])
  

text, key = "Security", 3 

def cce(text, k):
    out = ''
    print("C = (P + k) mode 26")
    for i in text:
        if i.isupper():
            out += chr((ord(i) + k - 65) % 26 + 65)
        else:
            out += chr((ord(i) + k - 97) % 26 + 97)
        print("{} = ({} + {}) mode 26 = {} = {}".format(i,ord(i.lower())-97, k, ord(out[-1].lower())-97, out[-1]))
    return out

def ccd(text, k):
    out = ''
    print("P = (C - k) mode 26")
    for i in text:
        if i.isupper():
            out += chr((ord(i) - k - 65) % 26 + 65)
        else:
            out += chr((ord(i) - k - 97) % 26 + 97)
        print("{} = ({} - {}) mode 26 = {} = {}".format(i,ord(i.lower())-97, k, ord(out[-1].lower())-97, out[-1]))
    return out


x = cce(text, key)
print(x)
print(ccd(x, key))

    
