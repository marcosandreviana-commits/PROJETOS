#posso votar se eu tiver titulo e idade minima
cond1 = input("tenho titulo?")
idade = int(input("digite a sua idade:"))

if cond1 =="sim" and idade >="16":
    print("pode votar")
else:
    print("não pode votar")
