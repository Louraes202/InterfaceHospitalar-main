## ---- Head ----
import os
import PySimpleGUI as sg
from layouts import *
## ---- Funções ----

## ---- Layouts ----
sg.theme("DarkPurple1")
logo = "Imagens/logo.ico"
# constantes
l_menu = [
    [sg.Text("Interface Hospital", font=("Comic 16 bold"))],
    [sg.Image(source="Imagens/hospital.png", expand_x=True, expand_y=True)],
    [sg.Button("Entrar"), sg.Button("Ajuda"), sg.Button("Shortcut"), sg.Button("Sair")]
]
# variáveis
l_entrar = [[sg.Text("Username:"), sg.Input("", key="UsernameValue", expand_x=True)],[sg.Text("Password:"), sg.Input("", key="PasswordValue", expand_x=True, password_char="⚫")],[sg.Button("Login"), sg.Button("Voltar")]]
l_interface = [[sg.Text("e")]]
## ---- Var ----
caminho = os.getcwd()
f = open("DB/utentes.txt", "r", encoding="UTF-8")
utentes = f.read().splitlines()

## ---- Body ----
# sg.popup_notify("Projeto Final de PSI - MOD7 Ficheiros", display_duration_in_ms=500)
window = sg.Window("IH - Menu", l_menu, icon=logo) # definição dos elementos da janela
running = True
# atualjanela = "menu"
while running == True: # loop da verificação e atualizaçáo de valores e eventos na janela
    atualjanela = "menu"
    event, values = window.read()
    print(atualjanela)
    if event == sg.WIN_CLOSED or event == "Sair" and atualjanela == "menu":
        running = False
    if event == "Entrar":
        atualjanela = "entrar"
        w_entrar = sg.Window("Entrar", l_entrar, icon=logo)
        event, values = w_entrar.read()

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar":
            atualjanela = "menu"
            l_entrar = [[sg.Text("Username:"), sg.Input("", key="UsernameValue", expand_x=True)], [sg.Text("Password:"), sg.Input("", key="PasswordValue", expand_x=True)], [sg.Button("Login"), sg.Button("Voltar")]]
            w_entrar.close()

        if event == "Login":
            username = values["UsernameValue"]
            password = values["PasswordValue"]
            utilizador = username + " " + password
            print(utilizador)
            w_entrar.close()
            l_entrar = [[sg.Text("Username:"), sg.Input("", key="UsernameValue", expand_x=True)], [sg.Text("Password:"), sg.Input("", key="PasswordValue", expand_x=True, password_char="⚫")], [sg.Button("Login"), sg.Button("Voltar")]]

    if event == "Shortcut": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Interface"
        w_interface = sg.Window("Interface", l_interface, icon=logo)
        event, values = w_interface.read()

        if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == "entrar":
            atualjanela = "menu"
            l_interface = [[sg.Text("e")]]
            w_interface.close()

f.close()