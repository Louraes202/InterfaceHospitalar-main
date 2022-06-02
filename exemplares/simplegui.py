import PySimpleGUI as sg
sg.theme("Dark") # tema
sg.popup_notify("Projeto de PSI - MOD7 Ficheiros", display_duration_in_ms=1000)

layout_entrada = [
    [sg.Text("Caminho do ficheiro:"), sg.Input(key="caminho")],
    [sg.Button("Ok"), sg.Button("Sair"), sg.Text("Não podes introduzir um caminho vazio!", text_color="white", key="erro_caminhovazio", visible=False)]
]

menu = [
    [sg.Text("Menu")],
    [sg.Button("Listar os alunos ou as disciplinas")],
    [sg.Button("Acrescentar disciplinas")],
    [sg.Button("Acrescentar alunos")],
    [sg.Button("Retirar um aluno do dicionário")],
    [sg.Button("Eliminar uma disciplina")],
    [sg.Button("Ler o ficheiro")]
]

listaralunos = [
    [sg.Text("Listar")]
]

window = sg.Window("Pesquisa Escolar", layout_entrada)
menuapp = False
while True:
    event, values = window.read()
    print("-- REFRESH --")
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    if event == "Ok":
        caminho = values["caminho"]
        if caminho == "":
            window["erro_caminhovazio"].Update(visible=True)
        else:
            window["erro_caminhovazio"].Update(visible=False)
            print(caminho)
            window.close()
            menu = sg.Window("Pesquisa Escolar - MENU", menu)
            event, values = menu.read()
            
            if event == "Listar os alunos ou as disciplinas":
                listar = sg.Window("Listar alunos.", listaralunos)
                event, values = listar.read()
                f = open(caminho, "r")
                

window.close()