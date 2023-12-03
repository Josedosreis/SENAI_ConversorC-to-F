# Sistema de importação e uso do PsGUI

from PySimpleGUI import PySimpleGUI as psg

import funcao

from funcao import c_f, f_c

# Layout --------------------------------------------

layout = [
    [psg.Text('Digite o valor da Temperatura:: '), psg.Input(key='valor', size=(15,1))],
    [psg.Text('Digite a Temperatura: '), psg.Input(key='temp', size=(15,1))],
    [psg.Text('Conversão: '), psg.Text(key='Resultado'), psg.Text(' <<<< ')],
    [psg.Button('Converter'), psg.Button('Limpar')]
]


# Janela ------------------------------------------
janela = psg.Window('Conversor de Temperatura', layout)

# Ler os Eventos ----------------------------------------
while True:
    eventos, valores = janela.read()
    if eventos == psg.WINDOW_CLOSED:
        break
    elif eventos == 'Limpar':
        janela['valor'].update('')
        janela['temp'].update('')
        janela['Resultado'].update('')
        janela['valor'].set_focus()
        
    elif eventos == 'valor':  
        valor = 'c'
        opcao1 = float(valores['valor'])
        janela['Resultado'].update(funcao.c_f(opcao1))
        
    else:
        valor = 'f'
        opcao2 = float(valores['valor'])
        janela['Resultado'].update(funcao.f_c(opcao2))
        
janela.close()
