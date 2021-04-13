def period_conversion(periodoEntrada, periodoSaida, vetor):
    if(periodoEntrada == 2):
        periodoEntrada = 6
    elif(periodoEntrada == 3):
        periodoEntrada = 12
    if(periodoSaida == 2):
        periodoSaida = 6
    elif(periodoSaida == 3):
        periodoSaida = 12
    conversion = periodoSaida/periodoEntrada
    conversion = int(conversion)
    newVetor = []
    count = 0
    for i in range(0, int(len(vetor)/conversion)):
        newVetor.append(0)
        for j in range(i*conversion, i*conversion+conversion):
            newVetor[count] += vetor[j]
        count += 1
    if(len(vetor) % conversion != 0):
        newVetor.append(0)
        for i in range(count*conversion, len(vetor)):
            newVetor[count] += vetor[count*conversion+(i-conversion)]
    return newVetor
