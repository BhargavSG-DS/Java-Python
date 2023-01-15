# Slip16_2A
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)

def main():
    newR = Rectangle(length=int(input("Length : ")), width=int(input("Width : ")))
    print("Area : ",newR.area())
    print("Perimeter : ",newR.perimeter())

if __name__=="__main__":
    main()