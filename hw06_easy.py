# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
from math import fabs

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, point_A, point_В):
        self.point_A = point_A
        self.point_В = point_В
    def length(self):
        return sqrt((self.point_A.x - self.point_В.x)**2 + (self.point_A.y - self.point_В.y)**2)

class Triangle:
    def __init__(self, point_A, point_В, point_С):
        self.point_A = point_A
        self.point_В = point_В
        self.point_С = point_С

    def square(self):
        # AB = sqrt((self.point_A.x - self.point_В.x)**2 + (self.point_A.y - self.point_В.y)**2)
        AB = Segment(self.point_A, self.point_В).length()
        BC = Segment(self.point_В, self.point_С).length()
        AC = Segment(self.point_A, self.point_С).length()
        P = (AB + BC + AC) / 2
        S = sqrt((P - AB)*(P - AC)*(P - BC)*P)
        return S
    
    def perimeter(self):
        AB = Segment(self.point_A, self.point_В).length()
        BC = Segment(self.point_В, self.point_С).length()
        AC = Segment(self.point_A, self.point_С).length()
        P = AB + BC + AC
        return P
    
    def height_A(self):
        BC = Segment(self.point_В, self.point_С).length()
        distance = fabs((self.point_С.y - self.point_В.y)*self.point_A.x - (self.point_С.x - self.point_В.x)*self.point_A.y + self.point_С.x * self.point_В.y - self.point_С.y * self.point_В.x) / BC
        return distance
    def height_B(self):
        AC = Segment(self.point_A, self.point_С).length()
        distance = fabs((self.point_С.y - self.point_A.y)*self.point_В.x - (self.point_С.x - self.point_A.x)*self.point_В.y + self.point_С.x * self.point_A.y - self.point_С.y * self.point_A.x) / AC
        return distance
    def height_C(self):
        AB = Segment(self.point_A, self.point_В).length()
        distance = fabs((self.point_В.y - self.point_A.y)*self.point_С.x - (self.point_В.x - self.point_A.x)*self.point_С.y + self.point_В.x * self.point_A.y - self.point_В.y * self.point_A.x) / AB
        return distance

print(Triangle(Point(0,0),Point(1,0),Point(0,1)).square())   
print(Triangle(Point(0,0),Point(1,0),Point(0,1)).perimeter()) 
print(Triangle(Point(0,0),Point(1,0),Point(0,1)).height_A()) 
print(Triangle(Point(0,0),Point(1,0),Point(0,1)).height_B())
print(Triangle(Point(0,0),Point(1,0),Point(0,1)).height_C())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, point_A, point_В, point_С, point_D):
        self.point_A = point_A
        self.point_В = point_В
        self.point_С = point_С
        self.point_D = point_D

    def perimeter(self):
        AB = Segment(self.point_A, self.point_В).length()
        BC = Segment(self.point_В, self.point_С).length()
        CD = Segment(self.point_С, self.point_D).length()
        AD = Segment(self.point_A, self.point_D).length()
        P = AB + BC + CD + AD
        return P

    def isEqualSided(self):
        AB = Segment(self.point_A, self.point_В).length()
        BC = Segment(self.point_В, self.point_С).length()
        CD = Segment(self.point_С, self.point_D).length()
        AD = Segment(self.point_A, self.point_D).length()
        return (AB == CD) or (AD == BC)
    
    def square(self):
        c = Segment(self.point_A, self.point_В).length()
        a = Segment(self.point_В, self.point_С).length()
        d = Segment(self.point_С, self.point_D).length()
        b = Segment(self.point_A, self.point_D).length()
        return ((a + b) / 2) * sqrt(c**2 - (((b - a)**2 + c**2 - d**2)/(2*(b-a))) **2)

    def sideAB(self):
        return Segment(self.point_A, self.point_В).length()
    def sideBC(self):
        return Segment(self.point_В, self.point_С).length()  
    def sideCD(self):
        return Segment(self.point_С, self.point_D).length()
    def sideAD(self):
        return Segment(self.point_A, self.point_D).length()


print(Trapezium(Point(0,0), Point(2,2), Point(4,2), Point(6,0)).perimeter()) 
print(Trapezium(Point(0,0), Point(2,2), Point(4,2), Point(6,0)).isEqualSided()) 
print(Trapezium(Point(0,0), Point(2,2), Point(4,2), Point(6,0)).square()) 