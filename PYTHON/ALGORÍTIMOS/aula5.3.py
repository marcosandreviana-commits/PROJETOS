cond1 = float(input("informe a quantidade de combustível:"))
cond2 = input("certifique-se se a atmosfera é respirável:")
cond3 = input("verifique se o traje está com 100% de integridade")

if cond1 <= 15 and (cond2 =="sim" or cond3 =="100%"):
    print("Iniciando protocolo de pouso")
else:
    print("Pouso abortado: risco de morte")
