class tri():
    def __init__(self,bre,len,wid) :
        self.bre = bre
        self.len = len 
        self.wid = wid 

    def area(self):
        return self.bre*self.len*self.wid
    def per(self):
        return self.bre+self.len+self.wid
    
a = tri(3,5,4)

r = a.area()
s = a.per()
print(f"Area of triangle is {r}")
print(f"perimeter of triangle is {s}")
