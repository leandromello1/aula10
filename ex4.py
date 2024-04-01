print("Programa para desenhar um retangulo utilizando numeros")

print("Voce quer quantas linhas?")
linha = int(input())

print("Voce quer quantas colunas?")
coluna = int(input())

for m in range(0, linha):
    for n in range(0, coluna):
        print(n + 1, end="")
    print("")