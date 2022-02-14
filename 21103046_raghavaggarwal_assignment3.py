#Question 1
print("The solution of Question 1 is:\n")
string = input("Enter the string: ").lower().split()
if len(string) == 1:
    string =string [0]
occurences = {}
for i in string:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
print("The occurence(s) of:")
for i in occurences:
    print(f"{i} is/are {occurences[i]}")


#Question 2
print("\nThe solution of Question 2 is:\n")
def is_leap_year(year: int) -> bool:                                                                                #Function for checking if the given year is a leap year or not
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  #Condition for given constraints in the question
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          #Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 #Condition for no. of days in February
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      #Setting no. of days in the given month
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                                #Syntax for incrementing the date
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print(f"Next Date is:{date}/{month}/{year}")

# Question 3
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_with_tuples = []
for i in alist:
    list_with_tuples.append((i, i ** 2))
print(list_with_tuples)
print("Done!")

# Question 4
# we will create if else statements
print("\nThe solution of Question 4 is:\n")
marks = int(input("Give a number between 4 and 10 including them- \n"))
if 4 == marks:
    print("Performance=Poor\n")
    print("Letter Grade=D\n")
elif marks == 5:
    print("Performance=Below Average\n")
    print("Letter Grade=C\n")
elif marks == 6:
    print("Performance=Average\n")
    print("Letter Grade=C+\n")
elif marks == 7:
    print("Performance=Good\n")
    print("Letter Grade=B\n")
elif marks == 8:
    print("Performance=Very Good\n")
    print("Letter Grade=B+\n")
elif Grade_points == 9:
    print("Performance=Excellent\n")
    print("Letter Grade=A\n")
elif marks == 10:
    print("Performance==Outstanding\n")
    print("Letter Grade=A+\n")
else:
    print("error\n")

#Question 5
print("\nThe solution of Question 5 is:\n")
string = "ABCDEFGHIJK"
pattern = 0
while len(string) - pattern*2 >= 1:
    print(" "*pattern + string[0 : len(string) - pattern*2])
    pattern += 1


#Question 6
print("\nThe solution of Question 6 is:\n")
dict1 = {}
while True:                                                                                                         #Loop for inputting values
    name = input("Enter the name of the student: ")
    SID = int(input(f"Enter the SID of {name}:"))
    dict1[SID] = name
    x=len(dict1)
    print(f"You have entered {x} values till now")
    while True:
        more_data = input("Do you want to enter more data? ")
        if more_data in ("N","n","No","no","NO"):
            more_data = 0
            break
        elif more_data in ("Y","y","Yes","yes","YES"):
            more_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if more_data == 0:
        break
print("\na. Student Details:  ")                                                                                      #Q6(a)
for i in dict1:
    print(f"The SID of {dict1[i]} is  {i}")
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         #Sorting the dictionary using student names
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                                       #Q6(b)
for i in dict2:
    print(f"The SID of {dict2[i]} is {i}")
dict3 = {}
for sorted_key in sorted(dict1):                                                                                    #Sorting the dictionary using SIDs
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        #Q6(c)
for i in dict3:
    print(f"The SID of {dict3[i]} is {i}")
print("\nd. ", end="")                                                                                              #Q6(d)
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print(f"The name of student whose SID is {search_SID} is {dict1[search_SID]}")
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\n")
        continue

# q7
# fibonacci sequence
first_number = int(input("Give a number-"))
second_number = int(input("Give a number-"))
# now it will keep on printing the sequence till you say y and to stop it say n
sum = first_number + second_number
series = [first_number, second_number]
n = "y"
while n == "y":
    series.append(series[len(series) - 1] + series[len(series) - 2])
    print(series)
    n = input("Give y to continue and n to stop going further-")
print("Now we got a list having a fibonacci series-")
print(series)

# now lets find average of the resultant fibonacci series
sum = 0
for i in series:
    sum = sum + i
print("Average of the sequence-")
print(sum / len(series))
print("Done!")


# q8
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# (a)
prequired_Set = Set1 ^ Set2
print(prequired_Set)
print("Done!")

# (b)
required_Set = Set1 ^ (Set2 ^ Set3)
print(required_Set)
print("Done!")

# (c)
required_Set = (Set1 & Set2) | (Set2 & Set3) | (Set1 & Set3)
print(required_Set)
print("Done!")

# (d)

new_Set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
required_Set = new_Set - Set1
print(required_Set)
print("Done!")

# (e)

required_Set = new_Set - (Set1 | Set2 | Set3)
print(required_Set)
print("Done!")