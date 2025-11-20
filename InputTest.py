<<<<<<< HEAD
#Jennifer Guy
#InputTest.py
#This program gets user input and uses it to determine if they made the honor roll and or dean's list

print("Please give last name, or type 'ZZZ' to quit")
lastname = input()
if lastname == "ZZZ":
    quit()
print("Please give first name")
firstname = input()
print("Please give your GPA")
GPA = eval(input())
GPASS = str(GPA)

print(firstname + " " + lastname)
print("Your GPA is " + GPASS)

if GPA >= 3.25:
    print("You have made the honor roll!")
if GPA >= 3.5:
    print("You have made the dean's list!")    
=======
print("Please give last name, or type 'ZZZ' to quit")
lastname = input()
if lastname == "ZZZ":
    quit()
print("Please give first name")
firstname = input()
print("Please give your GPA")
GPA = eval(input())
GPASS = str(GPA)

print(firstname + " " + lastname)
print("Your GPA is " + GPASS)

if GPA >= 3.25:
    print("You have made the honor roll!")
if GPA >= 3.5:
    print("You have made the dean's list!")    
>>>>>>> 14974bdc50dd394cc8c3ece85d2669a586329022
