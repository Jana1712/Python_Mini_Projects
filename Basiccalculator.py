def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

sel = int(input("Select operation (1-4): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")




#OUTPUT

PS C:\Users\Janakiraman B\Downloads\Udemy Certificates\Projects\python mini projects> & "C:/Users/Janakiraman B/AppData/Local/Microsoft/WindowsApps/python3.13.exe" "c:/Users/Janakiraman B/Downloads/Udemy Certificates/Projects/python mini projects/Basiccalculator.py"
Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide

Select operation (1-4): 2
Enter first number: 45
Enter second number: 30
45 - 30 = 15
PS C:\Users\Janakiraman B\Downloads\Udemy Certificates\Projects\python mini projects> & "C:/Users/Janakiraman B/AppData/Local/Microsoft/WindowsApps/python3.13.exe" "c:/Users/Janakiraman B/Downloads/Udemy Certificates/Projects/python mini projects/Basiccalculator.py"
Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide

Select operation (1-4): 1
Enter first number: 30
Enter second number: 23
30 + 23 = 53
PS C:\Users\Janakiraman B\Downloads\Udemy Certificates\Projects\python mini projects> & "C:/Users/Janakiraman B/AppData/Local/Microsoft/WindowsApps/python3.13.exe" "c:/Users/Janakiraman B/Downloads/Udemy Certificates/Projects/python mini projects/Basiccalculator.py"    
Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide

Select operation (1-4): 3
Enter first number: 4
Enter second number: 5
4 * 5 = 20
