

# Slip3_2A
def main():
    d={'A':1,'B':2,'C':3}
    while True:
        key=input("Enter key to check:")
        if key != "exit":
            if key in d.keys():
                print("Key is present and value of the key is:")
                print(d[key])
            else:
                print("Key isn't present!")
        else:
            exit()

if __name__=="__main__":
    main()