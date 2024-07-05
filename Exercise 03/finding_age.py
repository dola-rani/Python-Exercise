'''03: Write a function that takes 2 numbers as arguments (age of two brothers)
and find who is elder
Hints: Use condition inside the function'''

def find_elder_brother(age1, age2):
    if age1 > age2:
        return "First brother is elder"
    elif age2 > age1:
        return "Second brother is elder"
    else:
        return "Both brothers are of the same age"


age1 = int(input("Enter age of the first brother: "))
age2 = int(input("Enter age of the second brother: "))

result = find_elder_brother(age1, age2)
print(result)
