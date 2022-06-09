## ---- Head ----
import os
import PySimpleGUI as sg

## ---- Funções ----
def updatetable(): # função para atualizar a database da tabela
    f = open("DB/table.txt", "w", encoding="UTF-8")
    for linha in valorestable:
        for elemento in linha: 
            indexas = linha.index(elemento)
            if indexas != 3:
                f.write("{} | ".format(elemento))
            else:
                f.write(elemento)
        f.write("\n")

    f.close()

def addutente(utente): # função para atualizar os utentes
    futensa = open("DB/utentes.txt", "a", encoding="UTF-8")
    futensa.write(str(utente))
    futensa.close()
    utentes_read.append(utente)

def removeutente(utente): # função para remover utentes
    utentes.remove(utente)
    futentesa = open("DB/utentes.txt", "w", encoding="UTF-8")
    for e in utentes:
        futentesa.write(str(e))
        futentesa.write("\n")
    futentesa.close()
    utentes_read.remove(utente)

## ---- Layouts e assets ----
from layouts import *
sg.theme("Dark Purple 1") 

## ---- Var ----
from read import *
caminho = os.getcwd()
autologin = False

flogin = open("DB/login.txt", "r", encoding="UTF-8")
login = flogin.read().splitlines()
flogin.close()
islogged = False
utentes = []
utentesdict = {}

# ---- Var From File ----
updatetable()

for e in valorestable: # atualização dos valores da tabela para o dicionário dos utentes
    utentesdict[e[0]] = {"nomeutente": e[1], "cordapulseira": e[2], "caso": e[3]}
for e in utentesdict: # atualização dos valores do dicionário dos utentes para a lista dos utentes
    utentes.append(e)
futentesa = open("DB/utentes.txt", "w", encoding="UTF-8")
for e in utentes: # atualização da base de dados dos utentes
    futentesa.write(e)
    futentesa.write("\n")
futentesa.close()


## ---- Body ----
sg.popup_notify("Projeto Final de PSI - MOD7 Ficheiros", display_duration_in_ms=500) # notificação da abertura do projeto
window = sg.Window("IH - Menu", menu(), icon=logo, return_keyboard_events=True) # definição dos elementos da janela
running = True # variável que controla o ciclo que ativa/desativa o programa

while running == True: # loop da verificação e atualizaçáo de valores e eventos na janela
    print("-- REFRESH --") # é mostrado cada vez que o ciclo volta ao início
    atualjanela = "menu" # variáavel que controla a atualjanela
    event, values = window.read() # leitura dos eventos e valores da janela
    print("Evento: {}, Valores: {}".format(event, values))

    if event == sg.WIN_CLOSED or event == "Sair" or event == "Escape:27" and atualjanela == "menu": # quando a janela fechar
        running = False

    if event == "F2:113": # admin tools - autologin (REMOVE!)
        window["Entrar"].update(visible=False)
        window["Settings"].update(visible=False)
        window["Sair"].update(visible=False)
        window["Interface"].update(visible=True)
        window["Pesquisar Utente"].update(visible=True)
        window["Tools"].update(visible=True)
        window["Settings"].update(visible=True)
        window["Sair"].update(visible=True)
        islogged = True

    if event == "Entrar": # quando o respetivo botão for acionado
        atualjanela = "Entrar"
        w_entrar = sg.Window("Entrar", entrar(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Entrar":
            event, values = w_entrar.read()
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Entrar":
                atualjanela = "menu"
                w_entrar.close()

            if event == "Login": # quando o respetivo botão for acionado
                username = values["UsernameValue"].strip()
                password = values["PasswordValue"].strip()
                utilizador = username + " | " + password
                if utilizador not in login:
                    sg.Popup("Utilizador ou password incorretos!", title="ERRO!", icon=logo)
                elif autologin == True or utilizador in login:
                    sg.Popup("Logou com sucesso!\nAo fechar esta janela será redirecionado para o menu.", title="Login", icon=logo)
                    w_entrar.close()
                    # event = "Interface"
                    window["Entrar"].update(visible=False)
                    window["Settings"].update(visible=False)
                    window["Sair"].update(visible=False)
                    window["Interface"].update(visible=True)
                    window["Pesquisar Utente"].update(visible=True)
                    window["Tools"].update(visible=True)
                    window["Settings"].update(visible=True)
                    window["Sair"].update(visible=True)
                    islogged = True
                    break


    if event == "Ajuda": # quando o respetivo botão for acionado 
        atualjanela = "Ajuda"
        w_ajuda = sg.Window("Ajuda", ajuda(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Ajuda":
            event, values = w_ajuda.read()
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Ajuda": # closewindow(w_ajuda, entrar, menu)
                atualjanela = "menu"
                w_ajuda.close()
            



    if event == "Interface": # quando o respetivo botão for acionado
        atualjanela = "Interface"
        w_interface = sg.Window("Interface", interface(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Interface":
            event, values = w_interface.read()

            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Interface":
                atualjanela = "menu"
                w_interface.close()
            

            if event == "Colocar Utente": # quando o respetivo botão for acionado
                atualjanela = "Colocar Utente"
                w_colocarutente = sg.Window("Colocar Utente", colocarutente(), icon=logo, return_keyboard_events=True)
                while atualjanela == "Colocar Utente":
                    event, values = w_colocarutente.read()

                    if event == sg.WIN_CLOSED or event == "Escape:27" and atualjanela == "Colocar Utente":
                        atualjanela = "Interface"
                        w_colocarutente.close()
                    
                    if event == "Colocar": # quando o respetivo botão for acionado
                        nutente, nomeutente, cpulseira, caso = values["nutente"], values["utente"], values["cpulseira"], values["caso"]
                        try: # verificação do nutente
                            nutente = int(nutente)
                            nomeutente = str(nomeutente)
                            if len(nomeutente) != 0 and cpulseira in pulseiras:
                                valorestable.append([nutente, nomeutente, cpulseira, caso])
                                utentes.append(nutente)
                                addutente(nutente)
                                updatetable()
                                utentesdict[nutente] = {"nomeutente": nomeutente, "cordapulseira": cpulseira, "caso": caso}
                                atualjanela = "Interface"
                                w_colocarutente.close()
                                w_interface.close()
                                w_interface = sg.Window("Interface", interface(), icon=logo, return_keyboard_events=True)
                            else:
                                raise(ValueError)
                        except ValueError:
                            sg.Popup("Algum valor foi introduzido incorretamente.", title="ERRO!", icon=logo)



            if event == "Chamar Utente": # quando o respetivo botão for acionado
                selecionado = values[0]
                if len(selecionado) != 0:
                    posutente = selecionado[0]
                    sg.Popup("O utente {} acaba de ser chamado!".format(valorestable[posutente][1]), title="Chamar utente", icon=logo)
                    valorestable.pop(posutente)
                    utentesdict.pop(utentes[posutente])
                    removeutente(utentes[posutente])
                    updatetable()
                    w_interface.close()
                    w_interface = sg.Window("Interface", interface(), icon=logo)
                else:
                    sg.Popup("Não selecionou nenhum utente!", title="ERRO!", icon=logo)

    
    if event == "Tools": # quando o respetivo botão for acionado
        atualjanela = "Tools"
        w_tools = sg.Window("Tools", tools(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Tools":
            event, values = w_tools.read()

            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Tools":
                atualjanela = "menu"
                w_tools.close()
            
            if event == "Reset Utentes DB": # quando o respetivo botão for acionado
                futentesw = open("DB/utentes.txt", "w", encoding="UTF-8")
                futentesw.write(" ")
                futentesw.close()
                utentesdict.clear()
                utentes.clear()
                sg.Popup("Sucesso!", "A base de dados dos utentes foi restaurada! \nClique em OK para prosseguir.", icon=logo)
                atualjanela = "menu"
            
            if event == "Reset Utentes DB & Table DB": # quando o respetivo botão for acionado
                ftablew = open("DB/utentes.txt", "w", encoding="UTF-8")
                ftablew.write(" ")
                ftablew.close()
                utentesdict.clear()
                utentes.clear()
                sg.Popup("Sucesso!", "A base de dados da tabela foi restaurada! \nClique em OK para prosseguir.", icon=logo)
                atualjanela = "menu"
            

    if event == "Pesquisar Utente": # quando o respetivo botão for acionado
        atualjanela = "Pesquisar Utente"
        w_pesquisarutente = sg.Window("Pesquisar Utente", pesquisarutente(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Pesquisar Utente":
            event, values = w_pesquisarutente.read()
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Pesquisar Utente":
                atualjanela = "menu"
                w_pesquisarutente.close()
            
            if event == "Pesquisar": # quando o respetivo botão for acionado
                utente = values["utentes"]
                try:
                    w_pesquisarutente["nomeutente"].update(utentesdict[utente]["nomeutente"])
                    w_pesquisarutente["cpulseira"].update(utentesdict[utente]["cordapulseira"])
                    w_pesquisarutente["caso"].update(utentesdict[utente]["caso"])
                except KeyError:
                    sg.Popup("Esse utente não existe na base de dados!", title="ERRO!", icon=logo)

    if event == "Settings": # quando o respetivo botão for acionado
        atualjanela = "Settings"
        w_settings = sg.Window("Settings", settings(), icon=logo, return_keyboard_events=True)
        while atualjanela == "Settings":
            event, values = w_settings.read()
    
            if event == sg.WIN_CLOSED or event == "Voltar" or event == "Escape:27" and atualjanela == "Settings":
                atualjanela = "menu"
                w_settings.close()

            if event == "Mudar": # quando o respetivo botão for acionado
                sg.Popup("Esta funcionalidade está suspensa de momento para prevenir erros. [05/06]", title="Erro Temporário", icon=logo)
                
# Salvar os dados quando o programa termina
updatetable()

