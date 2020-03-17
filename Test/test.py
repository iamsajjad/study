
cc = lambda text, k: ''.join([chr((ord(i) + k) % 97) if i.isupper() else chr((ord(i) + k) % 122) for i in text])

print(cc('Hello', 3))

dcc = lambda text, k: ''.join([chr((ord(i) - k) % 97) if i.isupper() else chr((ord(i) - k) % 122) for i in text])

