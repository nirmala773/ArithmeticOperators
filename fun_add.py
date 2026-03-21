#define adding function
def addition(inputValue1, inputValue2):
    add = int(inputValue1) + int(inputValue2)
    return add

#define substraction function  
def substraction(inputValue1, inputValue2):
    return int(inputValue1) - int(inputValue2)

#define multiplication function
def multiplication(inputValue1, inputValue2):
   return int(inputValue1) * int(inputValue2)

def devision(inputValue1, inputValue2):
    return int(inputValue1) / int(inputValue2)

#initializing inputs
inputValue1= input("Enter the input1 value: ")
inputValue2= input("Enter the input2 value: ")

#calling addition function
adding = addition(inputValue1,inputValue2)
print("Here is the addition result: ", adding)

#calling subtract function
subtract = substraction(inputValue1, inputValue2)
print("Here is the subtract result: ", subtract)

#calling multiply function
multiply = multiplication(inputValue1, inputValue2)
print("Here is the multiplication result: ", multiply)

#calling division function
divident = devision(inputValue1, inputValue2)
print("Here is the division value: ", divident)