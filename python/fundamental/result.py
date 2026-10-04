marks = input("Enter your marks :")
marks=int(marks) #type casting
if marks >=90:
     grade = "A"
elif marks >=80:
     grade = "B"
elif marks >=70:
    grade = "C"
elif marks >=60:
    grade = "D"
else:
    grade = "F"
print("Your grade is ",grade)
