# a = idade >= 18
# b = carteira de habilitação
cond1 = int(input("digite a sua idade"))
cond2 = int(input("você tem carteira de habilitação? digite 1 para sim ou 2 para não"))
if cond1 >= 18 and cond2 ==1:
    print("pode pilotar")
else:
    print("não pode pilotar")
