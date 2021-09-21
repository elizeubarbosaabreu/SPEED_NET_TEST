#  ____                      _   _   _      _     _____         _   
# / ___| _ __   ___  ___  __| | | \ | | ___| |_  |_   _|__  ___| |_ 
# \___ \| '_ \ / _ \/ _ \/ _` | |  \| |/ _ \ __|   | |/ _ \/ __| __|
#  ___) | |_) |  __/  __/ (_| | | |\  |  __/ |_    | |  __/\__ \ |_ 
# |____/| .__/ \___|\___|\__,_| |_| \_|\___|\__|   |_|\___||___/\__|
#       |_|                                                         
# Testador de Internet
import speedtest
from time import sleep
import PySimpleGUI as sg
from os import system

sg.theme('Topanga')

layout = [ [sg.Stretch(), sg.T('Speed Net Speed', font=('Arial 24')), sg.Stretch()],
           [sg.Output(size=(80,7), font=('Arial 10'))],
           [sg.Button('Testar Velocidade'), sg.Stretch(), sg.T('Desenvolvido por @elizeu.barbosa.abreu')]
           ]

window = sg.Window('Testador de Velocidade da Intertnet', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break    
    
    
    print('\n\n\n\n\n\nPaciência!!! Estamos testando a velocidade de sua internet...')
    sleep(5)
    
    print('\n\n\n\n\n\nDescobrindo um caminho na velocidade da luz...')
    sleep(5)
    
    print('\n\n\n\n\n\nEncontramos um servidor que parece ser rápido...')
    sleep(5)
    
    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    threads = None
    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    
    print('\n\n\n\n\n\nAnálise em execução...')
    sleep(5)   
    
    print('\n\n\n\n\n\nAguarde mais um pouco...')
    sleep(3)
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)


    servidor = s.get_best_server()
    download_speed = (s.download(threads=threads))/1000000
    upload_speed = (s.upload(threads=threads))/1000000
    
    
    print('\n')
    print(f'SERVIDOR: {servidor["sponsor"]} ({servidor["url"]})')
    print(f'LOCALIDADE: {servidor["name"]}/{servidor["country"]}')
    print(f'SPEED DOWNLOAD: {download_speed:.2f} m/s')
    print(f'SPEED UPLOAD: {upload_speed:.2f} m/s')
    print(f'LATÊNCIA: {(servidor["latency"]):.2f} m/s')

window.close()