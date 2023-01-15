# Slip5_2B
def fibonacciGenerator():
    a=0
    b=1
    for i in range(6):
        yield b
        a,b= b,a+b

def main():
    obj = fibonacciGenerator()
    n = int(input())
    for i in range(n):
        try:
            print(next(obj))
        except Exception as e:
            print(e)
    return

if __name__=="__main__":
    main()