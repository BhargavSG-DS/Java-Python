# Slip7_2A
class Complex:
    def __init__(self, r, ir):
        self.real = r
        self.imaginary = ir
    def __str__(self) -> str:
        return str(self.real) + " + " + str(self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

def main():
    i = Complex(2, -10j)
    k = Complex(3, 5j)
    add = i + k
    print(add)

if __name__=="__main__":
    main()