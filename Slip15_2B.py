# Slip15_2B

def KO_ODD_INDICES(s : str):
    newS = "".join([s[i] for i in range(len(s)) if i%2==0])
    return newS

def main():
    print(KO_ODD_INDICES(input()))

if __name__=="__main__":
    main()