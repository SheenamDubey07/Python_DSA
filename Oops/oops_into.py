class Person():
    name = "Sheenam"
    occupation = "Software developer"
    networth = 10
    def info(self):
        print (f"{self.name} is a {self.occupation}")

a = Person()
b = Person()

a.name = "Yash"
a.networth = 15

b.name = "Somil"
b.occupation = "HR"
a.info()
b.info()
