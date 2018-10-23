dados = []
notas = []

while True:
    nome = input("Nome: ")
    nota1= float(input("Primeira nota: "))
    nota2= float(input("Segunda nota: "))
    cont = input("Você deseja continuar? [S/N] ").upper()
    dados.append(nome)
    notas.append((nota1, nota2))
    if cont == 'N':
        break

for x in range(len(notas)):
    print(dados[x], end=' ')
    print((notas[x][0] + notas[x][1])/2)
