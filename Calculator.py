print("Dobrorošli!")
prvi_broj = int(input("Molim unesite prvi broj:"))
drugi_broj = int(input("Molim unesite drugi broj:"))
operacija = input("Molim unesite matematičku operaciju +, -, * ili /")

if operacija == "+":
    print(prvi_broj+drugi_broj)
elif operacija == "-":
    print(prvi_broj - drugi_broj)
elif operacija == "*":
    print(prvi_broj * drugi_broj)
elif operacija == "/":
    print(prvi_broj / drugi_broj)
else:
    print("Nepoznata operacija")