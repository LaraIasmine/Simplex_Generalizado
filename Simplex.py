#####################################################################################
#                                   ALUNOS                                          #
# Gustavo Lino Barbosa - 9656506                                                    #
# Lara Iasmine Fabiano - 7986907                                                    #
# Lucas Paraiso Pereira - 6296471                                                   #
# Matheus Dalmaso Matsubara - 4045063                                               #
# Matheus La Scala - 6846008                                                        #
# Vitor Tuler Anizio - 4736500                                                      #
#####################################################################################

#################################### DEF FUNCOES ####################################

# Divisão da linha pivo pelo elemento pivo
def divideLinhaPivo(linhaPivo, pivo):
    for i in range(0, len(linhaPivo) - 1):
        if linhaPivo[i] != 0 and pivo != 0:
            linhaPivo[i] /= pivo

# Procurar o menor valor da linha Z e retorna a posicao da coluna
def procurar_menor(quadros):
    aux_menor = 0
    aux_valor = 0
    aux_cont = 0
    for i in range(0, len(quadros[0]) - 2):
        aux_valor = quadros[0][i]
        if aux_valor < aux_menor:
            aux_menor = aux_valor
            aux_cont = i
    return aux_cont

# Procurar o menor valor da linha retorna a posicao da coluna
def indiceMenorValor(lista):
    menor = min(lista)
    for i in range(0, len(lista)):
        if (lista[i] == menor):
            return i

# Funcao que monta a tabela
def exibeBonito(dados):
    a = ""
    for i in range(0, len(quadros[0]) - 2):
        a = a + "\tx{0}".format(i)

    print("Base" + a + "\tSolução")

    for i in range(0, len(quadros)):
        if i != 0:
            print(f'x{quadros[i][len(quadros[1]) - 1]}', end="")
        else:
            print('z', end="")

        for j in range(0, len(quadros[i]) - 1):
            aux = "{:.2f}".format(quadros[i][j])
            print(f"\t{aux}", end="")
        print()

# Encontra o valor negativo da solução e retorna posição
def LineSolutionNegative(matriz):
    colunaSolucao = len(matriz[0]) - 2

    resultado = []
    for i in range(0, len(quadros)):
        listaAux = []
        if (quadros[i][colunaSolucao] < 0):
            listaAux.append(quadros[i][colunaSolucao])
            listaAux.append(i)
            resultado.append(listaAux)

    if (resultado != []):
        menor = resultado[0]
        for i in range(1, len(resultado)):
            if (resultado[i][0] > menor):
                menor = resultado[i]
        return menor[1]
    return False

# Verifica se tem algum valor negativo na linha Z retorna True se encontrar
def isLineBaseNegative(matriz):
    for i in range(0, len(quadros)):
        if (quadros[0][i] < 0):
            return True
    return False

# Verifica o valor da menor divisão
def indiceMenorValor(lista):
    neg = True
    for i in range(0, len(lista)):
        lista[i] = abs(lista[i])

    for i in range(0, len(lista)):
        if lista[i] > 0:
            neg = False
    if neg:
        menor = max(lista)
    else:
        menor = min(lista)
    return menor

# Faz o calculo das colunas por linhas e pa
def atualiza_quadros(quadros, indiceCol, indiceLin):
    for i in range(0, len(quadros)):  # Linha 5 - 4 indices
        aux_col = quadros[i][indiceCol]
        if i != indiceLin:
            for j in range(0, col+1):  # Colunas 7 - 6
                quadros[i][j] = quadros[i][j] - \
                    (quadros[indiceLin][j] * aux_col)

# Resolve o porblema por otimização (Solucão NAO tem valor negativo)
def otimizacao(quadros):
    coluna_pivo = procurar_menor(quadros)
    menor = 999999
    linha_pivo = 0

    for i in range(1, len(quadros)):
        if (quadros[i][col] != 0 and quadros[i][coluna_pivo] != 0):
            aux_div = quadros[i][col] / quadros[i][coluna_pivo]
            if aux_div < menor and aux_div > 0:
                menor = aux_div
                linha_pivo = i

    divideLinhaPivo(quadros[linha_pivo], quadros[linha_pivo][coluna_pivo])
    atualiza_quadros(quadros, coluna_pivo, linha_pivo)
    print(f'sai x{quadros[linha_pivo][len(quadros[1]) - 1]}, entra x{coluna_pivo}')
    quadros[linha_pivo][len(quadros[1]) - 1] = coluna_pivo

# Resolve o porblema por otimização (Solucão tem valor negativo)
def viabilizacao(quadros):
    linha_pivo = LineSolutionNegative(quadros)
    valores = []
    valores_2 = []

    for i in range(0, len(quadros[0]) - 2):
        if (quadros[0][i] != 0 and quadros[linha_pivo][i] != 0):
            valores.append(quadros[0][i] / quadros[linha_pivo][i])
        else:
            valores.append(0)

    for i in range(0, len(valores)):
        if valores[i] != 0:
            valores_2.append(valores[i])

    menor = indiceMenorValor(valores_2)
    indicePivo = 0
    for i in range(0,len(valores)):
        if abs(valores[i]) == menor:
            indicePivo = i

    divideLinhaPivo(quadros[linha_pivo], quadros[linha_pivo][indicePivo])
    atualiza_quadros(quadros, indicePivo, linha_pivo)
    print(f'sai x{quadros[linha_pivo][len(quadros[1]) - 1]}, entra x{indicePivo}')
    quadros[linha_pivo][len(quadros[1]) - 1] = indicePivo

#################################### INIT ENTRADA DE DADOS ####################################
quant_variaves = int(input("Digite a quantidade de variaves (maximo 20): "))
while quant_variaves > 20:
    quant_variaves = int(
        input("Digite a quantidade de variaves com um valor ate` 20: "))

quant_resticoes = int(input("Digite a quantidade de restricoes (maximo 20): "))
while quant_resticoes > 20:
    quant_resticoes = int(
        input("Digite a quantidade de restricoes com um valor ate` 20: "))

tipo_problema = str(input("Escolha o tipo de problema (mAx/mIn): "))
while tipo_problema != "A" and tipo_problema != "a" and tipo_problema != "I" and tipo_problema != "i":
    print("Por gentileza, digite uma opcão valida!")
    tipo_problema = str(input("Escolha o tipo de problema (mAx/mIn): "))

# Faz a linha Z
print("\nFuncao Objetivo")
quadros = []
aux_list_FO = []
colunas = quant_resticoes

for i in range(0, quant_variaves):
    aux_valor_FO = int(input("Coeficiente da variavel x{0}: ".format(i)))
    if (tipo_problema == 'A' or tipo_problema == 'a'):
        aux_valor_FO = aux_valor_FO * -1
    aux_list_FO.append(aux_valor_FO)

quadros.append(aux_list_FO)

for i in range(0, quant_resticoes):
    print("\nRestricao {0}".format(i+1))
    aux_list = []
    for i in range(0, quant_variaves):
        aux_valor = int(input("Coeficiente da variavel x{0}: ".format(i)))
        aux_list.append(aux_valor)

    tipo_restricao = input("Tipo de Restrição: ")

    termo_ind = int(input("Termo independente: "))
    aux_list.append(termo_ind)

    if tipo_restricao == ">=":
        for i in range(0, quant_variaves+1):
            aux_list[i] = aux_list[i] * -1
        quadros.append(aux_list)
    elif tipo_restricao == "<=":
        quadros.append(aux_list)
    elif tipo_restricao == "==":
        colunas += 1
        quadros.append(aux_list)
        aux_list_neg = []
        for i in range(0, quant_variaves+1):
            aux_list_neg.append(aux_list[i] * -1)
        quadros.append(aux_list_neg)
    else:
        print("Erro na restrição")

#################################### FIM ENTRADA DE DADOS ####################################

################################### INIT MONTANDO PRIMEIRO QUADRO ###################################
for i in range(0, colunas + 1):
    quadros[0].append(0)

for i in range(0, colunas):
    aux_list = []
    aux_list = quadros[i + 1]
    termo_ind = aux_list[2]
    aux_list[2] = 0

    for j in range(0, colunas - 1):
        aux_list.append(0)

    aux_list.append(termo_ind)
    quadros[i + 1] = aux_list

col = 2
for i in range(1, len(quadros)):
    quadros[i][col] = 1
    col += 1

#################################### FIM MONTANDO PRIMEIRO QUADRO ####################################

for i in range(0, len(quadros)):
    quadros[i].append(i + 1)

# PRIMEIRO QUADRO
print('\n=====================================================================================')
print("Quadro inicial")  # Quadro inicial OK
exibeBonito(quadros)

i = 1
while LineSolutionNegative(quadros) != False or isLineBaseNegative(quadros):
    print('\n=====================================================================================')
    print(f'Interacao {i}: ', end="")
    i += 1
    if (LineSolutionNegative(quadros) == False):
        otimizacao(quadros)
        exibeBonito(quadros)
    else:
      viabilizacao(quadros)
      exibeBonito(quadros)

print()
print('Solucao: {:.2f}'.format(quadros[0][col]))
for i in range(1, len(quadros)):
    if (quadros[i][len(quadros[1]) - 1] == 0):
        print("x0: {:.2f}".format(quadros[i][len(quadros[1]) - 2]))

    if (quadros[i][len(quadros[1]) - 1] == 1):
        print("x1: {:.2f}".format(quadros[i][len(quadros[1]) - 2]))