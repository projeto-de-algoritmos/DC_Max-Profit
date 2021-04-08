from tools import max_subarray

periodicidade = 0
while(periodicidade < 1 or periodicidade > 3):
    print("\n O lucro é\n 1 - mensal 2 - semestral 3 - anual")
    periodicidadeStr = input()
    try:
        periodicidade = int(periodicidadeStr)
    except:
        print("Só são permitidos números na entrada")

lucros = []

cont = 1
while True:
    print("Digite o lucro do "+str(cont) +
          "º período, ou digite \"fim\" para sair")
    lucro = input()
    if (lucro == "fim"):
        break
    try:
        lucros.append(float(lucro))
        cont += 1
    except:
        print("Valor inválido")

print(lucros)
size = len(lucros)
result = max_subarray.max_subarray(lucros, 0, size-1)
print("max sum: " + str(result[2]))
slicer = slice(result[0], result[1]+1, 1)
subArray = lucros[slicer]
print(subArray)
