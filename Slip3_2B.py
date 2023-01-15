# Slip3_2B
class Student():
    def __init__(self,roll_no,name,age,gender):
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.gender=gender

class Test(Student):
    def __init__(self,roll_no,name,age,gender,sub1mark,sub2mark,sub3mark,):
        super().__init__(roll_no,name,age,gender)
        self.mark1=sub1mark
        self.mark2=sub2mark
        self.mark3=sub3mark
    
    def get_marks(self):
        self.total=self.mark1+self.mark2+self.mark3
        print(self.name , "\b's marks:", self.total)
        print("sub1 marks :",self.mark1)
        print("sub2 marks :",self.mark2)
        print("sub3 marks :",self.mark3)
        
p1=Test(1,"Barry",19,'male',82,89,76)
p2=Test(2,'Shreya',20,'female',94,91,84)
p1.get_marks()
p2.get_marks()