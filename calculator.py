def calculator():
    op = input("Alege operația (+, -, *, /): ")
    a = float(input("Primul număr: "))
    b = float(input("Al doilea număr: "))
    
    if op == '+':
        print("Rezultat:", a + b)
    elif op == '-':
        print("Rezultat:", a - b)
    elif op == '*':
        print("Rezultat:", a * b)
    elif op == '/':
        print("Rezultat:", a / b)
    else:
        print("Operație invalidă!")

calculator()