# Slip5_2A
class String:
    def get_String(self):
        self.string= input()
    def put_String(self):
        print(self.string.upper())


def main():
    newStr = String()
    newStr.get_String()
    newStr.put_String()
    return

if __name__=="__main__":
    main()