class Student:

    school = 'IUBAT'

    def __init__(self,m1,m2,m3):
        self.m1 =  m1
        self.m2 = m2
        self.m3 = m3

    def avarage(self):   #instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):  #class method
        return cls.school

    @staticmethod
    def info():    #static method
        print("This is student class!")

obj1 = Student(2,44,56)
print(obj1.avarage())
print(Student.getSchool())
Student.info()