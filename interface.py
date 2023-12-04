import PySimpleGUI as sg

from funcao import celsius_para_fahrenheit, fahrenheit_para_celsius

layout = [
    [sg.Text('Conversor de Temperatura')],
    [sg.Text('Digite a temperatura em Celsius:'), sg.InputText(key='input_celsius')],
    [sg.Button('Celsius para Fahrenheit'), sg.Button('Fahrenheit para Celsius')],
    [sg.Text(size=(30, 1), key='output')],
]

janela = sg.Window('Conversor de Temperatura', layout)

while True:
    eventos, valores = janela.read()

    if eventos in (sg.WIN_CLOSED, 'Exit'):
        break
    elif eventos == 'Celsius para Fahrenheit':
        try:
            celsius = float(valores['input_celsius'])
            fahrenheit = celsius_para_fahrenheit(celsius)
            janela['output'].update(f'Temperatura em Fahrenheit: {fahrenheit:.2f} °F')
        except ValueError:
            sg.popup_error('Digite um valor válido para a temperatura.')
    elif eventos == 'Fahrenheit para Celsius':
        try:
            fahrenheit = float(sg.popup_get_text('Digite a temperatura em Fahrenheit:'))
            celsius = fahrenheit_para_celsius(fahrenheit)
            janela['output'].update(f'Temperatura em Celsius: {celsius:.2f} °C')
        except ValueError:
            sg.popup_error('Digite um valor válido para a temperatura.')

janela.close()
