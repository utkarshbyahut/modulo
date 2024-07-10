# Computing the modulo of 2 Integers

# Input the 2 integers into the console 
intInput1 = int(input("Number 1 : "))
intInput2 = int(input("Number 2 : "))

# Running a while loop to check when intInput1 is not equal to intInput2
while (intInput2 != intInput2):

    if (intInput2 < intInput1):
        intInput1 -= intInput2

    if (intInput1 < intInput2):
        intInput2 -= intInput1

print(f"Mod is {intInput1}")
