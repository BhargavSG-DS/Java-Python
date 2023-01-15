# Slip2_2A
def main():
    Istring = input()
    u = len([i for i in Istring if i.isupper()])
    l = len([i for i in Istring if i.islower()])

    print("No. of Upper case characters: ",u)
    print("No. of Lower case characters: ",l)
    return

if __name__ == "__main__":
    main()