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
def arq_matriz(matriz):
    nome_arquivo = input("Digite o nome do arquivo que deseja abrir: ")
    try:
        # Tentar abrir o arquivo
       with open(nome_arquivo) as f:
          matriz = [[int(numero) for numero in linha.split()] for linha in f]
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
       print(f"Ocorreu um erro ao abrir o arquivo: {e}")
    return matriz

matriz1 = matriz2 = []
matriz1 = arq_matriz(matriz1)
matriz2 = arq_matriz(matriz2)


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