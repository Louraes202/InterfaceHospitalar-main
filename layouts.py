import PySimpleGUI as sg
from read import * 
# from main import utentes
logo = "Imagens/logo.ico"
loginbtnsstarting = False # p remover
## constantes
def menu(): # l_menu
    return [ 
        [sg.Text("Interface Hospital", font=("Comic 16 bold"))],
        [sg.Image(source="Imagens/hospital.png", expand_x=True, expand_y=True)],
        [sg.Button("Entrar"), sg.Button("Ajuda"), sg.Button("Interface", key="Interface", visible=loginbtnsstarting), sg.Button("Tools", key="Tools", visible=loginbtnsstarting), sg.Button("Pesquisar Utentes", key="Pesquisar Utente", visible=loginbtnsstarting), sg.Button("Settings", key="Settings"), sg.Button("Sair", key="Sair")]
        ]

## variáveis 

def entrar(): # l_entrar
    return [ 
        [sg.Text("Username:"), sg.Input("", key="UsernameValue", expand_x=True)],
        [sg.Text("Password:"), sg.Input("", key="PasswordValue", expand_x=True, password_char="⚫")],
        [sg.Button("Login"), sg.Button("Voltar")],
        [sg.Text("Atenção: Qualquer espaço antes e depois do Username e da Password será eliminado.")]
    ] 

def ajuda(): #l_ajuda
    return [
        [sg.Text("Ajuda", font=("Comic 16 bold"))],
        [sg.Text("Como utilizar o programa?")]
    ]

# valorestable = [] # utilizar uma database
def interface(): # l_interface
    return [
        [sg.Text("Interface Principal", font=("Comic 16 bold"))],
        [sg.Table(valorestable, ["N.ºUtente", "Utente", "Pulseira", "Caso"], expand_x=True, expand_y=True, auto_size_columns=True)],
        [sg.Button("Colocar Utente"), sg.Button("Chamar Utente"), sg.Button("Voltar")]
    ]

pulseiras = ("Verde", "Amarela", "Vermelha")
def colocarutente():
    return [
        [sg.Text("Nome"), sg.Input(key="utente", expand_x=True)],
        [sg.Text("N.ºUtente"), sg.Input(key="nutente", expand_x=True)],
        [sg.Text("Caso"), sg.Input(key="caso", expand_x=True)],
        [sg.Text("Pulseira"), sg.Combo(pulseiras, key="cpulseira", default_value="Verde", auto_size_text=True, change_submits=False)],
        [sg.Button("Colocar")]
    ]

def tools():
    return [ 
        [sg.Text("Tools", font=("Comic 16 bold"))]
    ]

def pesquisarutente():
    return [
        [sg.Text("Ficha de Utente", font=("Comic 16 bold"))], 
        [sg.Combo(values=utentes_read, key="utentes")],
        [sg.Text("Nome:"), sg.Text(key="nomeutente")],
        [sg.Text("Pulseira:"), sg.Text(key="cpulseira")],
        [sg.Text("Caso:"), sg.Text(key="caso")],
        [sg.Button("Pesquisar", key="Pesquisar"), sg.Button("Voltar")]
    ]

def settings():
    return [
        [sg.Text("Settings", font=("Comic 16 bold"))],
        [sg.Text("Tema"), sg.Combo(sg.theme_list()), sg.Button("Mudar")]
    ]