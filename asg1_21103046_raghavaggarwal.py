
#question1

print(" question 1")
a=input("Enter first number:")
b=input("Enyter second number:")
c=input("Enter third number:")
d=(int(a)+int(b)+int(c))/3
print("Average of the three numbers is :" ,float(d))
print("\n")

#question2

print(" question 2")
standard_deduction=10000
depend_deduction=3000
gross=input("enter your gross income: ")
No_of_dependents=input("Enter your number of dependents: ")
taxable_income=int(gross)-int(standard_deduction)-(int(depend_deduction)+int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :" ,float(tax))
print("\n")

#question3

print(" question 3")
SID=input("Enter your SID:")
Name=input("Enter your name:")
Gender=input("Enter your Gender:")
Course_name=input("Enter your course name:")
CGPA=float(input("Enter your CGPA:"))
STUDENT=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT)
print(" \n")

#question4

print(" question 4")
marks=[]
for i in range(5):
 marks.append(input("Enter marks of students: "))
marks.sort()
print(marks)  
print(" \n")

#question5(A)

print(" question 5(a)")
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("Part a question : ",colour)
print(" \n")

#question5(b)

print(" question 5(b)")
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple']
print("Part b of question :",colour)
print("\n")