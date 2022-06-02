## ---- Head ----
import os
import PySimpleGUI as sg
## ---- Funções ----
# fazer função de fechar as janelas 
# basicamente ver onde o código é repetido e transformar as repetições em funcções
## ---- Layouts e assets ----
from layouts import *
## ---- Var ----
caminho = os.getcwd()
print(caminho)
print("-------------------------------")
f = open("DB/utentes.txt", "r", encoding="UTF-8")
utentes = f.read().splitlines()


## ---- Body ----
# sg.popup_notify("Projeto Final de PSI - MOD7 Ficheiros", display_duration_in_ms=500)
window = sg.Window("IH - Menu", menu(), icon=logo) # definição dos elementos da janela
running = True
tabela = {}
# atualjanela = "menu"
while running == True: # loop da verificação e atualizaçáo de valores e eventos na janela
    print("-- REFRESH --")
    atualjanela = "menu"
    event, values = window.read()
    print("Evento: {}, Valores: {}".format(event, values))
    if event == sg.WIN_CLOSED or event == "Sair" and atualjanela == "menu":
        running = False

    if event == "Entrar":
        atualjanela = "entrar"
        w_entrar = sg.Window("Entrar", entrar(), icon=logo)
        event, values = w_entrar.read()

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar":
            atualjanela = "menu"
            w_entrar.close()

        if event == "Login":
            username = values["UsernameValue"]
            password = values["PasswordValue"]
            utilizador = username + " " + password
            print(utilizador)
            w_entrar.close()

    if event == "Ajuda":
        atualjanela = "Ajuda"
        w_ajuda = sg.Window("Ajuda", ajuda(), icon=logo)
        event, values = w_ajuda.read()

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar":
            atualjanela = "menu"
            w_ajuda.close()


    if event == "Interface": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Interface"
        w_interface = sg.Window("Interface", interface(), icon=logo)
        event, values = w_interface.read()
        print(event, "Interface")

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "Interface":
            print(event)
            atualjanela = "menu"
            w_interface.close()
        

        if event == "Colocar Utente":
            print(event)
            atualjanela = "Colocar Utente"
            w_colocarutente = sg.Window("Colocar Utente", colocarutente(), icon=logo)
            event, values = w_colocarutente.read()

            if event == sg.WIN_CLOSED and atualjanela == "Colocar Utente":
                atualjanela = "Interface"
                w_colocarutente.close()
                print(event)
            
            if event == "Colocar":
                nutente, nomeutente, cpulseira, caso = values["nutente"], values["utente"], values["cpulseira"], values["caso"]
                valorestable.append([nutente, nomeutente, cpulseira, caso])
                tabela[nutente] = {"nomeutente": nomeutente, "cordapulseira": cpulseira, "caso": caso}
                print(tabela)
                atualjanela = "Interface"
                w_colocarutente.close()
                w_interface.close()
                event = "Interface"

        if event == "Chamar Utente":
            print(event)
            continue


f.close()