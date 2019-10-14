#base class
class Polygon(object):
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
#derived class
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findAreaPerimeter(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        p=(a+b+c)
        print('the perimeter of a triangle is',p)
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.4f' %area)
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    def findAreaPerimeter(self):
        a,b=self.sides
        print("area of Rectange is",a*b)
        print("Perimeter of Rectangle is",2*(a+b))
class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,1)
    def findAreaPerimeter(self):
        a=self.sides
        #b=self.sides
        a[0]=int(a[0]*a[0])
        print("area of square is ",a[0])
        print("perimeter of square",4*a[0])

t = Triangle()
r=Rectangle()
s=Square()
#print('1:triangle 2.rectangle 3.square 4 quit')
while True:
    print('1:Triangle 2.Rectangle 3.Square 4.Quit  :')
    choice=int(input('enter choice 1 or 2 or 3 or 4'))
    if choice == 1:
        t.inputSides()
        t.dispSides()
        t.findAreaPerimeter()
    elif choice==2:
        r.inputSides()
        r.dispSides()
        r.findAreaPerimeter()
    elif choice==3:
        s.inputSides()
        s.dispSides()
        s.findAreaPerimeter()
    elif choice == 4:
        break
