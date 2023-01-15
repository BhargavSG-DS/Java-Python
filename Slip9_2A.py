# Slip9_2A
class String:
    def get_String(self):
        self.string = input()
    def print_String(self):
        print(" ".join(reversed([i for i in self.string.split(" ")])).lower())


def main():
    newStr = String()
    newStr.get_String()
    newStr.print_String()
    return

if __name__=="__main__":
    main()