from tools import max_subarray
from tools import period_conversion

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
        print("Valor inválido, digite apenas números")

periodicidadeRes = 0
while(periodicidadeRes < 1 or periodicidadeRes > 3 or (periodicidadeRes < periodicidade)):
    print("Você deseja receber o resultado em um perído\n1 - mensal 2 - semestral 3 - anual")
    if (periodicidadeRes < 1 or periodicidadeRes > 3):
        print("Você deve digitar um valor entre 1 e 3")
    if ((periodicidadeRes < periodicidade)):
        print("A periodicidade do resultado deve ser igual ou maior a periodicidade da entrada")
    periodicidadeStr = input()
    try:
        periodicidadeRes = int(periodicidadeStr)
    except:
        print("Só são permitidos números na entrada")

print("\nDados de lucro inseridos:")
print(lucros)
lucros = period_conversion.period_conversion(
    periodicidade, periodicidadeRes, lucros)
print("\nDados de lucro convertidos na periodicidade desejada")
print(lucros)

size = len(lucros)
result = max_subarray.max_subarray(lucros, 0, size-1)
if(periodicidadeRes == 1):
    periodicidadeStr = "Mês"
elif(periodicidadeRes == 2):
    periodicidadeStr = "Semestre"
elif(periodicidadeRes == 3):
    periodicidadeStr = "Ano"
print("\nO período de maior lucro vai do " +
      str(result[0]+1) + "º " + periodicidadeStr + " até o "+str(result[1]+1)+"º " + periodicidadeStr)
print("Lucro do período de maior lucro: " + str(result[2]))
""" slicer = slice(result[0], result[1]+1, 1)
subArray = lucros[slicer]
print(subArray) """
