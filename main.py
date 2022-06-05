## ---- Head ----
import os
import PySimpleGUI as sg
# import keyboard
## ---- Funções ----
## ---- Layouts e assets ----
from layouts import *
sg.theme("Dark Purple 1") # fazer o tema mudar e registar a mudança em um ficheiro!
## ---- Var ----
from read import *
caminho = os.getcwd()
autologin = False
# futentes = open("DB/utentes.txt", "r", encoding="UTF-8")
flogin = open("DB/login.txt", "r", encoding="UTF-8")
# utentes = futentes.read().splitlines()
login = flogin.read().splitlines()
islogged = False
utentes = []
utentesdict = {}
# ---- Var From File ----
for e in valorestable:
    utentesdict[e[0]] = {"nomeutente": e[1], "cordapulseira": e[2], "caso": e[3]}
print(utentesdict)
for e in utentesdict:
    utentes.append(e)

futentesa = open("DB/utentes.txt", "w", encoding="UTF-8")
for e in utentes:
    futentesa.write(e)
    futentesa.write("\n")
futentesa.close()


## ---- Body ----
# sg.popup_notify("Projeto Final de PSI - MOD7 Ficheiros", display_duration_in_ms=500)
window = sg.Window("IH - Menu", menu(), icon=logo, return_keyboard_events=True) # definição dos elementos da janela
running = True

# atualjanela = "menu"
while running == True: # loop da verificação e atualizaçáo de valores e eventos na janela
    print("-- REFRESH --")
    atualjanela = "menu"
    event, values = window.read()
    print("Evento: {}, Valores: {}".format(event, values))
    if event == sg.WIN_CLOSED or event == "Sair" or event == "Escape:27" and atualjanela == "menu":
        running = False

    if event == "F2:113": # admin tools - autologin (REMOVE!)
        window["Settings"].update(visible=False)
        window["Sair"].update(visible=False)
        window["Interface"].update(visible=True)
        window["Tools"].update(visible=True)
        window["Pesquisar Utente"].update(visible=True)
        window["Settings"].update(visible=True)
        window["Sair"].update(visible=True)
        islogged = True

    if event == "Entrar":
        atualjanela = "Entrar"
        w_entrar = sg.Window("Entrar", entrar(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Entrar":
            event, values = w_entrar.read()
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Entrar":
                atualjanela = "menu"
                w_entrar.close()

            if event == "Login":
                username = values["UsernameValue"].strip()
                password = values["PasswordValue"].strip()
                utilizador = username + " | " + password
                print(utilizador)
                if utilizador not in login:
                    sg.Popup("Utilizador ou password incorretos!", title="ERRO!", icon=logo)
                elif autologin == True or utilizador in login:
                    sg.Popup("Logou com sucesso!\nAo fechar esta janela será redirecionado para o menu.", title="Login", icon=logo)
                    w_entrar.close()
                    # event = "Interface"
                    window["Settings"].update(visible=False)
                    window["Sair"].update(visible=False)
                    window["Interface"].update(visible=True)
                    window["Tools"].update(visible=True)
                    window["Pesquisar Utente"].update(visible=True)
                    window["Settings"].update(visible=True)
                    window["Sair"].update(visible=True)
                    islogged = True
                    break
                # w_entrar.close()

    if event == "Ajuda":
        atualjanela = "Ajuda"
        w_ajuda = sg.Window("Ajuda", ajuda(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Ajuda":
            event, values = w_ajuda.read()
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Ajuda": # closewindow(w_ajuda, entrar, menu)
                atualjanela = "menu"
                w_ajuda.close()
            
            # closewindow(w_ajuda, entrar, menu, event)
            # break


    if event == "Interface": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Interface"
        w_interface = sg.Window("Interface", interface(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Interface":
            event, values = w_interface.read()

            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Interface":
                atualjanela = "menu"
                w_interface.close()
            

            if event == "Colocar Utente":
                atualjanela = "Colocar Utente"
                w_colocarutente = sg.Window("Colocar Utente", colocarutente(), icon=logo, return_keyboard_events=True)
                while atualjanela == "Colocar Utente":
                    event, values = w_colocarutente.read()

                    if event == sg.WIN_CLOSED or event == "Escape:27" and atualjanela == "Colocar Utente":
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
                                print(utentesdict)
                                atualjanela = "Interface"
                                w_colocarutente.close()
                                w_interface.close()
                                w_interface = sg.Window("Interface", interface(), icon=logo, return_keyboard_events=True)
                            else:
                                raise(ValueError)
                        except ValueError:
                            sg.Popup("Algum valor foi introduzido incorretamente.", title="ERRO!", icon=logo)



            if event == "Chamar Utente":
                selecionado = values[0]
                if len(selecionado) != 0:
                    posutente = selecionado[0]
                    sg.Popup("O utente {} acaba de ser chamado!".format(valorestable[posutente][1]), title="Chamar utente", icon=logo, )
                    valorestable.pop(posutente)
                    w_interface.close()
                    w_interface = sg.Window("Interface", interface(), icon=logo)
                else:
                    sg.Popup("Não selecionou nenhum utente!", title="ERRO!", icon=logo)

    
    if event == "Tools": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Tools"
        w_tools = sg.Window("Tools", tools(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Tools":
            event, values = w_tools.read()

            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Tools":
                atualjanela = "menu"
                w_tools.close()
            

    if event == "Pesquisar Utente": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Pesquisar Utente"
        w_pesquisarutente = sg.Window("Pesquisar Utente", pesquisarutente(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Pesquisar Utente":
            event, values = w_pesquisarutente.read()
    
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Pesquisar Utente":
                atualjanela = "menu"
                w_pesquisarutente.close()
            
            if event == "Pesquisar":
                utente = values["utentes"]
                try:
                    w_pesquisarutente["nomeutente"].update(utentesdict[utente]["nomeutente"])
                    w_pesquisarutente["cpulseira"].update(utentesdict[utente]["cordapulseira"])
                    w_pesquisarutente["caso"].update(utentesdict[utente]["caso"])
                except KeyError:
                    sg.Popup("Esse utente não existe na base de dados!", title="ERRO!", icon=logo)

    if event == "Settings": #_# mudar shortcut para nova janela constante (que fecha o menu)
        atualjanela = "Settings"
        w_settings = sg.Window("Settings", settings(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Settings":
            event, values = w_settings.read()
    
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Settings":
                atualjanela = "menu"
                w_settings.close()
            
            
            
# futentes.close()
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


