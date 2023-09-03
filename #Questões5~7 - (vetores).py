#Questões5~7 - (vetores)

# Terceiro maior

#quick sort
def quick_sort(v):
    if len(v) <= 1:
        return v
    p = v[len(v) // 2]
    e = [x for x in v if x < p]
    m = [x for x in v if x == p]
    d = [x for x in v if x > p]
    return quick_sort(e) + m + quick_sort(d)

print('--Terceiro maior elemento--')
v = list(map(int,input('Digite um vetor qualquer: ').split()))
v = quick_sort(v)
print(v)
x = v[len(v)-1] #maior elemento
n = 0
'''
  O contador 'n' indica se o número é menor, exemplo, se n = o então x = maior elemento,
  se n = 1, então o x = segundo maior elemento, 'n' basicamente conta quantos números existem nesse vetor e
  que são menores que o x.
'''
for i in range (len(v)-1, -1, -1):
  if v[i]< x: 
    n +=1
    x = v[i] 
    if n == 2:
      print('%d é o terceio maior número' % x)
      break
if n<2:
   print('O vetor não possui 3 ou mais elementos distintos.')


# Partição de dois vetores
print('--Partição de dois vetores--')
l1 = list(map(int,input('Digite um vetor qualquer: ').split()))
l2 = list(map(int,input('Digitr outro vetor de mesmo tamaho: ').split()))
l3 = l1 + l2
l3 = quick_sort(l3)

for i in range(0, len(l3), 1):
  if i<len(l1):
    l1[i] = l3[i]
  else:
    l2[i-len(l2)] = l3[i]


print(l3, l1, l2)
if l1[len(l1)-1] == l2[0]:
  print("Não existe solução que todos elementos de l2 sejam maior que de l1.")
'''
  Existe a possibilidade de quando separar o vetor não for possível manter elementos de l1<l2,
  exemplo, se todos elementos forem iguais.
'''



# Permutações de vetores
def contar_repeticoes(vetor):
    contagem = {} 
    for elemento in vetor:  # Percorrer cada elemento no vetor
        if elemento in contagem:  # Verificar se o elemento já está no dicionário
            contagem[elemento] += 1  # Se estiver, incrementar a contagem
        else:
            contagem[elemento] = 1  # Se não estiver, adicionar o elemento ao dicionário com contagem 1
    return contagem

print('--Permutação de vetores--')
v1 = list(map(int,input('Digite um vetor qualquer: ').split()))
v2 = list(map(int,input('Digite outro vetor de mesmo tamanho: ').split()))

if contar_repeticoes(v1) == contar_repeticoes(v2) and v1!= v2:
  print("O vetor v1 é uma permutação do vetor v2 e vice-versa.")
elif contar_repeticoes(v1) == contar_repeticoes(v2) and v1== v2:
  print("Os dois vetores são iguais.")
else:
  print("Os vetores não são permutações um do outro.")