# Slip13_2B
class queue:
    def __init__(self,L :list):
        self.L = L
    
    def _dQ(self):
        return self.L.pop(0)

    def _nQ(self,N):
        self.L.append(N)

def main():
    newQueue = queue(list(input()))
    newQueue._nQ(input("enqueue a number: "))
    print(newQueue.L)
    print(newQueue._dQ())
    print(newQueue.L)

if __name__=="__main__":
    main()