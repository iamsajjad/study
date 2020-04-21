
def multInverse(k, mode):
    try:
        for i in range(mode):
            if i * k % mode == 1:
                print("{} * {} mode {} == 1".format(i, k, mode))
                return i
    except:
        return None

print("multInv : " + str(multInverse(15, 26)))
