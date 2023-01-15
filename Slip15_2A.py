# Slip15_2A
class Student:
    def __init__(self, Student_name, marks):
        self.Student_name=Student_name
        self.marks=marks
    
    def get_marks(self):
        print("\nOriginal name and values")
        print(self.Student_name,'marks : ',self.marks)
        
    def modify_marks(self):
        self.Student_name1=input('Enter modified name : ')
        self.marks1=int(input('Enter modified marks : '))
        print(self.Student_name1,'modified marks',self.marks)
        
    def modified_marks(self):
        print("\nmodified name and values")
        print(self.Student_name1,'marks : ',self.marks1)
        
def main():
    x=Student('Barry',81)
    x.get_marks()
    x.modify_marks()

    x.get_marks()
    x.modified_marks()

if __name__=="__main__":
    main()