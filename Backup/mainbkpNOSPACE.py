## ---- Head ----
import os
import PySimpleGUI as sg
## ---- Funções ----
from Backup.specialfunctions import *
# basicamente ver onde o código é repetido e transformar as repetições em funcções
## ---- Layouts e assets ----
from layouts import *
## ---- Var ----
from read import *
caminho = os.getcwd()
print(caminho)
print("-------------------------------")
futentes = open("DB/utentes.txt", "r", encoding="UTF-8")
flogin = open("DB/login.txt", "r", encoding="UTF-8")
utentes = futentes.read().splitlines()
login = flogin.read().splitlines()
islogged = False
## ---- Body ----
# sg.popup_notify("Projeto Final de PSI - MOD7 Ficheiros", display_duration_in_ms=500)
window = sg.Window("IH - Menu", menu(), icon=logo) # definição dos elementos da janela
running = True
r_entrar, r_ajuda, r_interface = False, False, False
utentesdict = {}
utenteslist = []
# atualjanela = "menu"
while running == True: # loop da verificação e atualizaçáo de valores e eventos na janela
    print("-- REFRESH --")
    atualjanela = "menu"
    event, values = window.read()
    print("Evento: {}, Valores: {}".format(event, values))
    if event == sg.WIN_CLOSED or event == "Sair" and atualjanela == "menu":
        running = False

    if event == "Entrar":
        atualjanela = "Entrar"
        w_entrar = sg.Window("Entrar", entrar(), icon=logo)
        while atualjanela == "Entrar":
            event, values = w_entrar.read()
            if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "Entrar":
                atualjanela = "menu"
                w_entrar.close()

            if event == "Login":
                username = values["UsernameValue"].strip()
                password = values["PasswordValue"].strip()
                utilizador = username + " | " + password
                print(utilizador)
                if utilizador not in login:
                    sg.Popup("Utilizador ou password incorretos!", title="ERRO!", icon=logo)
                else:
                    sg.Popup("Logou com sucesso!\nAo fechar esta janela será redirecionado para a interface.", title="Login", icon=logo)
                    w_entrar.close()
                    # event = "Interface"
                    window["btnSair"].update(visible=False)
                    window["btnInterface"].update(visible=True)
                    window["btnSair"].update(visible=True)
                    islogged = True
                    break
                # w_entrar.close()

    if event == "Ajuda":
        atualjanela = "Ajuda"
        w_ajuda = sg.Window("Ajuda", ajuda(), icon=logo)
        while atualjanela == "Ajuda":
            event, values = w_ajuda.read()
            if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar": # closewindow(w_ajuda, entrar, menu)
                atualjanela = "menu"
                w_ajuda.close()
            
            # closewindow(w_ajuda, entrar, menu, event)
            # break


    if event == "Interface": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Interface"
        w_interface = sg.Window("Interface", interface(), icon=logo)
        while atualjanela == "Interface":
            event, values = w_interface.read()

            if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "Interface":
                atualjanela = "menu"
                w_interface.close()
            

            if event == "Colocar Utente":
                atualjanela = "Colocar Utente"
                w_colocarutente = sg.Window("Colocar Utente", colocarutente(), icon=logo)
                while atualjanela == "Colocar Utente":
                    event, values = w_colocarutente.read()

                    if event == sg.WIN_CLOSED and atualjanela == "Colocar Utente":
                        atualjanela = "Interface"
                        w_colocarutente.close()
                    
                    if event == "Colocar":
                        nutente, nomeutente, cpulseira, caso = values["nutente"], values["utente"], values["cpulseira"], values["caso"]
                        try: # verificação do nutente
                            nutente = int(nutente)
                            nomeutente = str(nomeutente)
                            if len(nomeutente) != 0 and cpulseira in pulseiras:
                                valorestable.append([nutente, nomeutente, cpulseira, caso])
                                print(valorestable)
                                utentesdict[nutente] = {"nomeutente": nomeutente, "cordapulseira": cpulseira, "caso": caso}
                                print(utentesdict)
                                atualjanela = "Interface"
                                w_colocarutente.close()
                                w_interface.close()
                                w_interface = sg.Window("Interface", interface(), icon=logo)
                            else:
                                raise(ValueError)
                        except ValueError:
                            sg.Popup("Algum valor foi introduzido incorretamente.", title="ERRO!", icon=logo)



            if event == "Chamar Utente":
                selecionado = values[0]
                if len(selecionado) != 0:
                    posutente = selecionado[0]
                    sg.Popup("O utente {} acaba de ser chamado!".format(valorestable[posutente][1]), title="Chamar utente", icon=logo)
                    valorestable.pop(posutente)
                    w_interface.close()
                    w_interface = sg.Window("Interface", interface(), icon=logo)
                else:
                    sg.Popup("Não selecionou nenhum utente!", title="ERRO!", icon=logo)

futentes.close()
flogin.close()

# Salvar os dados quando o programa termina

f = open("DB/table.txt", "w", encoding="UTF-8")
print(valorestable)
for linha in valorestable:
    for elemento in linha: 
        indexas = linha.index(elemento)
        if indexas != 3:
            f.write("{} | ".format(elemento))
        else:
            f.write(elemento)
    f.write("\n")

f.close()
