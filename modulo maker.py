# Computing the modulo (%) (Remainder) of 2 Integers

# Input the 2 integers into the console assuming inputs are not 0
intInput1 = int(input("Number 1 : "))
intInput2 = int(input("Number 2 : "))

def modulo(input1, input2):
    marker = 0 # Flag to check case, set to default for Case 2

    # Case 1 : Input1 > Input 2
    while (input2 < input1):
        input1 -= input2 
        marker = 1 # Flag to mark as case 1, so case 2 gets ommited
        modulus = input1

    # Case 2 : Input1 < Input 2
    while ((input1 < input2) and (marker == 0)):
        input2 -= input1
        modulus = input2

    print("Mod is 0") if (input1 == input2) else print(f"Mod is {modulus}")

modulo(intInput1, intInput2)