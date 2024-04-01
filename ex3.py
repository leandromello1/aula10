print("Programa para desenhar um retangulo utilizando (#)")

print("Voce quer quantas linhas?")
linha = int(input())

print("Voce quer quantas colunas?")
coluna = int(input())

for n in range(0, linha):
    print("#"*coluna)