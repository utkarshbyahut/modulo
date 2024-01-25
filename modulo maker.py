a = int(input("Num 1 : "))
b = int(input("Num 2 : "))

while ((a>=b) or (a<=b)):

    if a >= b:
        a = a - b

    elif b >= a:
        b = b - a

print(f"Mod is {a}")
