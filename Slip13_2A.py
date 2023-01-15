# Slip13_2A
def main():
    num = 1
    while num != -1:
        try:
            num = int(input("Enter -1 to exit: "))
        except(ValueError):
            print("Incorrect input, Not a integer.")

if __name__=="__main__":
    main()