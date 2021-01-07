from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('LightBrown')
layout = [
    [sg.Text('Usuário',size=(6,1)), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha',size=(6,1)), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de Login', layout)

#Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Henrique' and valores['senha'] == '123456':
            print('Bem-Vindo ao meu primeira tela de login')
