cond1 = float(input("qual o valor da compra? R$"))
cond2 = input("você é cliente VIP?")

if cond1 >=100 or cond2 =="sim":
    print("desconto de 10%")
    print("cond1 * 0.9")
else:
    print("sem desconto")
