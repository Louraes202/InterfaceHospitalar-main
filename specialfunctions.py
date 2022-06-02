import PySimpleGUI as sg 
def closewindow(window, janelaatual, janelaposterior, event):
    if event == sg.WIN_CLOSED or event == "Voltar" and atualjanela == janelaatual:
            atualjanela = janelaposterior
            window.close()

## Exemplo:
            # closewindow(w_ajuda, entrar, menu, event)
            # break

## Nota: Este pedaço de código tem de estar no fim da condição da janela, porque vai terminar a execução do loop.