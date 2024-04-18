class Box:
    def __init__(self, name, rollNo, dbmsMarks, pythonMarks, cMarks, osMarks, cnMarks):
        self.name = name
        self.rollNo = rollNo
        self.dbmsMarks = dbmsMarks
        self.pythonMarks = pythonMarks
        self.cMarks = cMarks
        self.osMarks = osMarks
        self.cnMarks = cnMarks
        
    def alldetails(self):
        print(self.name,end=" ")
        print(self.rollNo,end=" ")
        print(self.dbmsMarks,end=" ")
        print(self.pythonMarks,end=" ")
        print(self.cMarks,end=" ")
        print(self.osMarks,end=" ")
        print(self.cnMarks,end=" ")
    


student1 = Box("Harika", "5A1", 78, 67, 77, 89, 46)
student1.alldetails()
print()
student2 = Box("Swapna", "5A2", 38, 65, 97, 59, 41)
student2.alldetails()
print()
student3 = Box("Sushma", "5A3", 88, 95, 47, 89, 31)
student3.alldetails()