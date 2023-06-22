class person():
    passper = 40 
    def __init__(self,name,per) :
        self.name = name 
        self.per = per

    def info(self):
        print (f"{self.name} with {self.per} percentage is ",end=" ")
        if self.per >= person.passper:
            print("Passed")
        else:
            print('Not Passed')
a = person("Sheenam",60)
b = person('Yash',30)
a.info()
b.info()
