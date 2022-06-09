import os
caminho = os.getcwd()

# código para atualizar as databases

# atualização da tabela
f = open("DB/table.txt", "r", encoding="UTF-8")
linhas = f.read().splitlines()
print(linhas)
linhas2 = []
for linha in linhas: # retirar a separação
    indexas = linhas.index(linha)
    linhas2.append(linha.split("|"))

for linha in linhas2:
    for e in linha:
        indexas = linha.index(e)
        x = e.strip()
        linha[indexas] = x

valorestable = linhas2
f.close()

# atualização dos utentes
futentes = open("DB/utentes.txt", "r", encoding="UTF-8")
utentes_read = futentes.read().splitlines()
futentes.close()