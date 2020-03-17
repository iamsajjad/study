
class Person:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def fromfullname(cls, fullname):
        fname, lname = fullname.split(' ')
        return cls(fname, lname)
    
    @staticmethod
    def islongname(name):
        return True if len(name) > 5 else False

x = Person.fromfullname("sajjad jawad")
print(x.fname, x.lname)

print(Person.islongname("sajjad"))
print(Person.islongname("jawad"))
