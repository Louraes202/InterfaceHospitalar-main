import PySimpleGUI as sg
sg.theme("BlueMono") # tema
sg.popup_notify("Projeto de PSI - MOD7 Ficheiros", display_duration_in_ms=1000)

menu = [ # janela do menu
    [sg.Text("Menu")],
    [sg.Button("Listar os alunos")], # janela 1
    [sg.Button("Listar as disciplinas")], # janela 2
    [sg.Button("Acrescentar alunos")], # janela 3
    [sg.Button("Acrescentar disciplinas")], # janela 4
    [sg.Button("Remover alunos")], # janela 5
    [sg.Button("Remover disciplinas")], # janela 6
    [sg.Button("Inscrever um aluno numa disciplina")], # janela 7
    [sg.Button("Sair")] # janela 8
]

listaralunos = [ # janela 1
    [sg.Text("Listar Alunos", text_color="white")]
]

listardisciplinas = [ # janela 2
    [sg.Text("Listar Disciplinas", text_color="white")]
]

addalunos = [ # janela 3
    [sg.Text("Acrescentar aluno(s)", text_color="white")],
    [sg.InputText(key="aluno")],
    [sg.Button("Add")]
]

adddisciplinas = [ # janela 4
    [sg.Text("Acrescentar disciplina(s)", text_color="white")],
    [sg.InputText(key="disciplina")],
    [sg.Button("Add")]
]

rmalunos = [ # janela 4
    [sg.Text("Remover aluno(s)", text_color="white")],
    [sg.InputText(key="disciplina")],
    [sg.Button("Remove")]
]

stopmenu = None # variáveal booleana que determina quando as janelas vão estar ativas
window = sg.Window("Pesquisa Escolar", menu) # variável com o conteúdo da janela
atualjanela = ""

while stopmenu != True: # execução da interface gráfica e leitura constante de eventos e valores (refresh)
    event, values = window.read()
    print(event, values, atualjanela)
    print("-- REFRESH --")
    if event == sg.WIN_CLOSED or event == "Sair" and atualjanela == "menu":
        stopmenu = True

    if event == "Listar os alunos" and atualjanela != "listaralunos": # 1. Listar Alunos
        alunosdb = open("alunos.txt", "r", encoding="utf8") # database dos alunos
        alunos = alunosdb.read().splitlines()
        atualjanela = "listaralunos"
        print(alunos)
        for e in alunos:
            listaralunos.append([sg.Text(e)])
        listara = sg.Window("Listar Alunos", listaralunos)
        event, values = listara.read()

        if event == sg.WIN_CLOSED:
            atualjanela = "menu"
            listaralunos = [[sg.Text("Listar Alunos", text_color="white")]]
            alunosdb.close()



    if event == "Listar as disciplinas" and atualjanela != "listardisciplinas": # 2. Listar Disciplinas
        disciplinasdb = open("disciplinas.txt", "r", encoding="utf8") # database das disciplinas
        disciplinas = disciplinasdb.read().splitlines()
        atualjanela = "listardisciplinas"
        print(disciplinas)
        for e in disciplinas:
            listardisciplinas.append([sg.Text(e)])
        listard = sg.Window("Listar Disciplinas", listardisciplinas)
        event, values = listard.read()

        if event == sg.WIN_CLOSED:
            atualjanela = "menu"
            listardisciplinas = [[sg.Text("Listar Disciplinas", text_color="white")]]
            disciplinasdb.close()

    if event == "Acrescentar alunos" and atualjanela != "acrescentaralunos": # 3. Acrescentar alunos
        atualjanela = "acrescentaralunos"
        addalunos = sg.Window("Acrescentar Alunos", addalunos)
        event, values = addalunos.read()

        if event == sg.WIN_CLOSED:
            atualjanela = "menu"
            addalunos = [sg.Text("Acrescentar aluno(s)", text_color="white")], [sg.InputText(key="aluno")], [sg.Button("Add")]
        if event == "Add":
            aluno = values["aluno"].split(" ")
            fw = open("alunos.txt", "a")
            for e in aluno: fw.write("\n{}".format(e))
            fw.close()
            addalunos.close()
            atualjanela = "menu"
            addalunos = [sg.Text("Acrescentar aluno(s)", text_color="white")], [sg.InputText(key="aluno")], [sg.Button("Add")]

    if event == "Acrescentar disciplinas" and atualjanela != "acrescentardisciplinas": # 4. Acrescentar disciplinas
        atualjanela = "acrescentardisciplinas"
        adddisciplinas = sg.Window("Acrescentar Disciplinas", adddisciplinas)
        event, values = adddisciplinas.read()

        if event == sg.WIN_CLOSED:
            atualjanela = "menu"
            adddisciplinas = [[sg.Text("Acrescentar disciplina(s)", text_color="white")],[sg.InputText(key="disciplina")],[sg.Button("Add")]]
        if event == "Add":
            disciplina = values["disciplina"].split(" ")
            fw = open("disciplinas.txt", "a")
            for e in disciplina: fw.write("\n{}".format(e))
            fw.close()
            adddisciplinas.close()
            atualjanela = "menu"
            adddisciplinas = [sg.Text("Acrescentar aluno(s)", text_color="white")], [sg.InputText(key="aluno")], [sg.Button("Add")]

    if event == "Remover alunos" and atualjanela != "removeralunos": # 5. Remover alunos
        atualjanela = "removeralunos"
        rmalunos = sg.Window("Remover alunos", rmalunos)
        event, values = rmalunos.read()

        if event == sg.WIN_CLOSED:
            atualjanela = "menu" 
            rmalunos = [[sg.Text("Remover aluno(s)", text_color="white")], [sg.InputText(key="disciplina")], [sg.Button("Remove")]]
        if event == "Remove":

            rmalunos.close()
            atualjanela = "menu"
            rmalunos = [[sg.Text("Remover aluno(s)", text_color="white")], [sg.InputText(key="disciplina")], [sg.Button("Remove")]]

    

window.close()
