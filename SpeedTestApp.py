#  ____                      _   _   _      _     _____         _   
# / ___| _ __   ___  ___  __| | | \ | | ___| |_  |_   _|__  ___| |_ 
# \___ \| '_ \ / _ \/ _ \/ _` | |  \| |/ _ \ __|   | |/ _ \/ __| __|
#  ___) | |_) |  __/  __/ (_| | | |\  |  __/ |_    | |  __/\__ \ |_ 
# |____/| .__/ \___|\___|\__,_| |_| \_|\___|\__|   |_|\___||___/\__|
#       |_|                                                         


import speedtest
import PySimpleGUI as sg
from random import choice

def medir_net():
    servers = []   

    threads = None

    print('INICIANDO OS TESTES...')
    s = speedtest.Speedtest()
    
    print('LOCALIZANDO SERVIDORES...')
    s.get_servers(servers)
    
    s.get_best_server()
    servidor = s.get_best_server()
    print(f'SERVIDOR: {(servidor["sponsor"]).upper()} LOCALIZADO...')
    print(f'ACESSANDO: {servidor["url"]}')
    print(f'LOCALIZA\u00c7\u00c3O DO SERVIDOR: {(servidor["name"]).upper()}/{(servidor["country"]).upper()}...')
    print('AGUARDE O RESULTADO...\n')
        
    s.download(threads=threads)
    s.upload(threads=threads)
    
    download_speed = (s.download(threads=threads))/(1024 ** 2)
    upload_speed = (s.upload(threads=threads))/(1024 ** 2)
     
    print(f'SPEED DOWNLOAD: {download_speed:.2f} Mbits')
    print(f'SPEED UPLOAD: {upload_speed:.2f} Mbits')
    
    ping = s.results.ping
    
    print(f'LAT\u00caNCIA: {ping:.2f} ms')
 
# Cada vez que abrir o software ele aparecer\u00e1 com um tema diferente
temas = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
tema = choice(temas)
sg.theme(f'{tema}')

layout = [ [sg.Stretch(), sg.T('Internet Speed Test', font=('Arial 24')), sg.Stretch()],
           [sg.Output(size=(80,7), font=('Arial 10'))],
           [sg.T('Desenvolvido por @elizeu.barbosa.abreu'), sg.Stretch(), sg.Button('Testar Velocidade')]
           ]

window = sg.Window('INTERNET SPEED TEST', layout, resizable=True)

while True:
    
    event, values = window.read()
        
    if event == sg.WIN_CLOSED:
        break
    
    medir_net()

window.close()
