#Questões(1~4) = matrizes

'''
Recebe duas matrizes escritas em arquivos .txt, formatados na sseguinte maneira:
-
a00 a01 a02
a10 a11 a12
a20 a21 a22
-
Printa as duas matrizes;
Mostra quantas vezes cada termo repete;
'''

# Leitura de arquivo e conversão para matriz
with open('matriz1.txt') as f:
    matriz1 = [[int(numero) for numero in linha.split()] for linha in f]
with open('matriz2.txt') as f:
    matriz2 = [[int(numero) for numero in linha.split()] for linha in f]

# Conta a quantidade de elementos repetidos
def contar_repeticoes(matriz):
    contagem = {}  # Usando um dicionário para contar as repetições
    for linha in matriz:
        for elemento in linha:
            if elemento in contagem: 
                contagem[elemento] += 1
            else:
                contagem[elemento] = 1
    return contagem

#printar uma matriz
def print_matriz(matriz):
  for i in range(0, len(matriz), 1):
    print(matriz[i])



print_matriz(matriz1)
print('-----------')
print_matriz(matriz2)
print('-----------')

resultado1 = contar_repeticoes(matriz1)
resultado2 = contar_repeticoes(matriz2)

#Printa a quantidade de vezes que um termo repete na matriz
print('Elemento / Repetições')

print('Matriz 1:')
for elemento, contagem in resultado1.items():
  print(f'{elemento} = {contagem}')

print('Matriz 2:')
for elemento, contagem in resultado2.items():
  print(f'{elemento} = {contagem}')