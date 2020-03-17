
def metadata(text: int) -> str: return text

def cc(text, k): return ''.join([chr((ord(i) + k) % 97) if i.isupper() else chr((ord(i) + k) % 122) for i in text])

cc = lambda text, k: ''.join([chr((ord(i) + k) % 97) if i.isupper() else chr((ord(i) + k) % 122) for i in text])

dcc = lambda text, k: ''.join([chr((ord(i) - k) % 97) if i.isupper() else chr((ord(i) - k) % 122) for i in text])
  

"""
def cc(text, k):
    out = ''
    for i in text:
        if i.isupper():
            out += chr((ord(i) + k) % 97)
        else:
            out += chr((ord(i) + k) % 122)

    return out
"""



print(cc('sajjad', 3))
print(cc('SAJJAD', 3))
print(dcc(cc('SAJJAD', 3), 3))
print(dcc('KhoorVlu', 3))
    
