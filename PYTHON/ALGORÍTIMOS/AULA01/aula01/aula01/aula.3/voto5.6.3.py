idade = int(input("digite a sua idade:"))

if idade <16:
    print("não pode votar")
elif idade <18:
    print(" voto facultativo")
elif idade <70:
    print("voto obrigatorio")
else: 
    print("voto facultativo")