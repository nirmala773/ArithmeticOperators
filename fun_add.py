#define adding function
def addition(a, b):
    return a + b 

#define substraction function  
def substraction(a, b):
    return a - b

#define multiplication function
def multiplication(a, b):
   return a * b

#define division function
def division(a, b):
    if b == 0:
        return "Cannot devided by zero"
    return a / b

#initializing inputs
try: 
    inputValue1 = int(input("Enter the input1 value: "))
    inputValue2 = int(input("Enter the input2 value: "))
except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

#calling addition function
adding = addition(inputValue1,inputValue2)
print("Addition result: ", adding)

#calling subtract function
subtract = substraction(inputValue1, inputValue2)
print("subtraction result: ", subtract)

#calling multiply function
multiply = multiplication(inputValue1, inputValue2)
print("multiplication result: ", multiply)

#calling division function
divident = division(inputValue1, inputValue2)
print("division value: ", divident)