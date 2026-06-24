a = float(input("digite o seu altura:"))
b = input("digite 1 para feminino ou 2 para masculino:")

if b == 1:
    print(("o seu peso ideal é:"), (62.1 * a)-44.7)
else:
    print(("o seu peso ideal é:"), (72.7 * a)-58)