# Slip8_2B
class String:
    def get_String(self):
        self.string = input()
    def print_String(self):
        print(self.string.upper())
    def lowerReverse(self):
        print("".join(reversed([i for i in self.string])).lower())


def main():
    newStr = String()
    newStr.get_String()
    newStr.print_String()
    newStr.lowerReverse()
    return

if __name__=="__main__":
    main()