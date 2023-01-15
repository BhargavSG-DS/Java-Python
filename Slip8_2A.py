# Slip8_2A

def main():
    tup = tuple(sorted(input()))
    s = set(tup)
    dup = [i for i in s if tup.count(i)>1]
    print("list of duplicates : ",dup)

if __name__=="__main__":    
    main()