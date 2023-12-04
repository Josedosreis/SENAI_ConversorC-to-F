import PySimpleGUI as sg

import funcao

from funcao import celsius_para_fahrenheit, fahrenheit_para_celsius

layout = [
    [sg.Text('Conversor de Temperatura')],
    [sg.Text('Digite a temperatura em Celsius:'), sg.InputText(key='input_celsius')],
    [sg.Button('Celsius para Fahrenheit'), sg.Button('Fahrenheit para Celsius')],
    [sg.Text(size=(30, 1), key='output')],
]

window = sg.Window('Conversor de Temperatura', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Celsius para Fahrenheit':
        try:
            celsius = float(values['input_celsius'])
            fahrenheit = celsius_para_fahrenheit(celsius)
            window['output'].update(f'Temperatura em Fahrenheit: {fahrenheit:.2f} °F')
        except ValueError:
            sg.popup_error('Digite um valor válido para a temperatura.')
    elif event == 'Fahrenheit para Celsius':
        try:
            fahrenheit = float(sg.popup_get_text('Digite a temperatura em Fahrenheit:'))
            celsius = fahrenheit_para_celsius(fahrenheit)
            window['output'].update(f'Temperatura em Celsius: {celsius:.2f} °C')
        except ValueError:
            sg.popup_error('Digite um valor válido para a temperatura.')

window.close()
