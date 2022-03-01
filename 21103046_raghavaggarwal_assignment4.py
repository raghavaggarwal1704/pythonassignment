
print('Question number 1')
print(" the tower of Hanoi with three disks.")
def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)
hanoi(3, 'U', 'V', 'W')
print("")

#question 2
print("Question number 2")
#input rows
n = int(input('Enter the size of pascals triangle you want: '))

#using recursions
print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #makin 1 as first number
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops
print("\n Using loops:")
for line in range(1, n+1):

    #everything else is same from above
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")


#question 3
print("Question number 3")

a=int(input("input  first integer: "))
b=int(input("input second integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

#question 4
print("Question number 4")

class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object has been destroyed")

#creating object
student1 = Student("Raghav", 21103046)
print("Object has been created")

#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

#deleting object
del student1
print("")

#question 5
print("Question number 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")


employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part a
print("part a")
employee1.salary = 70000
print( f"The updated salary of the employee {employee1.name} is {employee1.salary}")

#part b
print("part b")
print( end='')
del employee3
print("")

#question 6
print("Question number 6")
#input first word
word = input("Enter the first word: ")

#input a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word with the exact same letters : ")

#defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

# verifing the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input to verify the word
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test?\n")
    elif ans == 'n':
        print("The word doesn't have a meaning,i.e. friendship is fake..\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()     
