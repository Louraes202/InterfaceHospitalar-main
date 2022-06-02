import PySimpleGUI as sg 
sg.theme("DarkPurple1") # LightBlue
logo = "Imagens/logo.ico"

## constantes
def menu(): # l_menu
    return [ 
        [sg.Text("Interface Hospital", font=("Comic 16 bold"))],
        [sg.Image(source="Imagens/hospital.png", expand_x=True, expand_y=True)],
        [sg.Button("Entrar"), sg.Button("Ajuda"), sg.Button("Interface"), sg.Button("Sair")]
        ]

## variáveis 

def entrar(): # l_entrar
    return [ 
        [sg.Text("Username:"), sg.Input("", key="UsernameValue", expand_x=True)],
        [sg.Text("Password:"), sg.Input("", key="PasswordValue", expand_x=True, password_char="⚫")],
        [sg.Button("Login"), sg.Button("Voltar")]
    ] 

def ajuda(): #l_ajuda
    return [
        [sg.Text("Ajuda", font=("Comic 16 bold"))],
        [sg.Text("Como utilizar o programa?")]
    ]

valorestable = []
def interface(): # l_interface
    return [
        [sg.Text("Interface Principal", font=("Comic 16 bold"))],
        [sg.Table(valorestable, ["N.ºUtente", "Utente", "Pulseira", "Caso"], expand_x=True, expand_y=True, auto_size_columns=True)],
        [sg.Button("Colocar Utente"), sg.Button("Chamar Utente"), sg.Button("Voltar")]
    ]

pulseiras = ("Verde", "Amarela", "Vermelha")
def colocarutente():
    return [
        [sg.Text("N.ºUtente"), sg.Input(key="nutente", expand_x=True)],
        [sg.Text("Nome"), sg.Input(key="utente", expand_x=True)],
        [sg.Text("Pulseira"), sg.Combo(pulseiras, key="cpulseira", default_value="Verde", auto_size_text=True, change_submits=False)],
        [sg.Text("Caso"), sg.Input(key="caso", expand_x=True)],
        [sg.Button("Colocar")]
    ]