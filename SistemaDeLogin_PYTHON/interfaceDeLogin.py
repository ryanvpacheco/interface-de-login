import PySimpleGUI as sg
sg.theme("Dark Grey 13")
layout = [
    [sg.Text("Usuário"), sg.Input(key="usuario", size=(30, 1))],
    [sg.Text("  Senha"), sg.Input(key="senha", password_char='*', size=(30, 1))],
    [sg.Checkbox("Salvar o Login")],
    [sg.Button("Entrar")]
]
janela = sg.Window("Login" , layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == "Entrar":
        if valores["usuario"] == "Ryan" and valores["senha"] == "123456":
            print("BEM-VINDO AO SISTEMA")
            break
        else:
            print("Usuario ou senha incorretos. Tente novamente!")
