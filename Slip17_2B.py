# Slip17_2B
import dateutil.parser as dparser

class Date:
    def __init__(self):
        strDate = input()
        try:
            self.value = dparser.parse(strDate, fuzzy=True)
        except(ValueError):
            self.value = "invalid Date Exception."
    def _print(self):
        print(str(self.value))


def main():
    newDate = Date()
    newDate._print()

if __name__ == "__main__":
    main()