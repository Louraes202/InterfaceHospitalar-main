import os
def menu(nome):
    error = None
    resp = -1
    os.system("cls")
    print("✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙")
    print("{}".format(nome.center(50)))
    print("✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙ ✙")
    print("[1] Listar Utentes")
    print("[2] Adicionar Utentes")
    print("[3] Remover Utentes")
    print("[4] Interface de chamada de utentes")
    print("[0] Sair")
    while resp != 0 and resp != 1 and resp != 2 and resp != 3 and resp != 4:
        resp = input(">")
        try:
            resp = int(resp)
        except ValueError:
            print("Tipo de valor inválido, tente novamente.")

    return(resp)

resp = menu("Interface Hospital")