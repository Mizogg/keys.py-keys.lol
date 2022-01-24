import os, webbrowser, datetime, smtplib, random, requests, time
import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path
from bit import *
from bit.format import bytes_to_wif
gmail_user = 'dave4london@gmail.com'
gmail_password = 'amftakvssuxsutcy'
start_time = datetime.datetime.now()


start_time = datetime.datetime.now()


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def create_main_window(settings):
    sg.theme(settings['theme'])

    menu_def = [['&Menu', ['&Settings', 'E&xit']]]
    layout = [[sg.Menu(menu_def)],
               [sg.Text('🐍 🐍 KEYS.lol using bit libary and BlockchainAPI Made by Mizogg in PySimpleGUI 🐍 🐍', size=(40,3), font=('Comic sans ms', 14)),
               sg.Button('', key='mizogg', size=(10,1), font=('Helvetica', 10), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename='mizogg.png', image_size=(400, 80), image_subsample=1, border_width=0)],
               [sg.Button('', key='face', size=(10,1), font=('Helvetica', 30), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename='MizoggFaceBW.png', image_size=(140, 80), image_subsample=1, border_width=0)],
               [sg.Text('Start range in BITs (Puzzle StartNumber) -> ', size=(38,1), font=('Comic sans ms', 13)),
               sg.Input(size=(6,1), key='bitx', background_color='green', text_color='white', font=('Comic sans ms', 13)), sg.Text('', size=(6,1))],
               [sg.Text('Stop range Max in BITs (Puzzle StopNumber) -> ', size=(38,1), font=('Comic sans ms', 13)),
               sg.Input(size=(6,1), key='bity', background_color='green', text_color='white', font=('Comic sans ms', 13)), sg.Text('', size=(6,1)),
              sg.Button('Start/Stop',  font=('Comic sans ms', 14))],
              [sg.Text('')],
              [sg.Output(size=(100, 20), font=('Comic sans ms', 11), key='out')]]

    return sg.Window('MIZOGG Keys_GUI.py',
                     layout=layout,
                     default_element_size=(8,1))

def get_all_key(data):
    key = Key.from_int(data[-1])
    wifu = bytes_to_wif(key.to_bytes(), compressed=False)
    wifc = bytes_to_wif(key.to_bytes(), compressed=True)
    keyu = Key(wifu)
    caddr = key.address
    uaddr = keyu.address
    result = {
        'key': key,
        'wifu': wifu,
        'wifc': wifc,
        'keyu': keyu,
        'caddr': caddr,
        'uaddr': uaddr
    }
    return result

def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    generator = False
    while True:
        if window is None:
            window = create_main_window(settings)
        event, values = window.Read(timeout=10)
        if event in (None, 'Exit'):
            break
        elif event == 'Start/Stop':
            generator = not generator            
            counter = 0
            total = 0
            pagenumber = 0

        if generator:
            x=int(values['bitx'])
            y=int(values['bity'])
            ran = random.randrange(2**x,2**y)
            seed = str(ran)
            data_wallet = map(get_all_key, [(i, ran + i) for i in range(128)])
            wallets = [wallet_ for wallet_ in data_wallet]
            query = [i['caddr'] for i in wallets]
            query1 = [i['uaddr'] for i in wallets]
            counter += 1
            total += 256
            pagenumber = (int(seed) // 128) + 1
            if len(query) == 128 or len(query1) == 128:

                try:
                    request = requests.get(
                        "https://blockchain.info/multiaddr?active=%s" % ','.join(query) + '&base=BCH&cors=true', timeout=10)
                    request = request.json()

                    def find_wallet():
                        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                        print('📋 Page Number : ' + str(pagenumber))
                        print('Matching Key ==== Found!!!\n PrivateKey: ' + wallets[0]['key'].to_hex())
                        print('⛔️WARNING !!!!  Any Winners found will be Within 128 Private Key range of this Scan !!!! WARNING !!!!⛔️')
                        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                        with open("winner.txt", "a") as f:
                            print("start write")
                            text = f"""\n=============Bitcoin Address with Balance Found=====================
                                    \nPage Number: {str(pagenumber)}
                                    \nPrivateKey (hex): {wallets[0]['key'].to_hex()}
                                    \nBitcoin Address Compressed : {wallets[0]['caddr']}
                                    \nBitcoin Address UnCompressed : {wallets[0]['uaddr']}
                                    \nPrivateKey (wif) Compressed :  {wallets[0]['wifc']}
                                    \nPrivateKey (wif) UnCompressed : {wallets[0]['wifu']}
                                    \nCheck All Addresses within 128 in this range to find wallet\n"""
                            f.write(text)

                    for row in request["addresses"]:
                        print(row)
                        if row["final_balance"] or row["total_received"] > 0:
                            find_wallet()
                            break
                    request1 = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query1), timeout=10)
                    request1 = request1.json()

                    for row in request1["addresses"]:
                        print(row)
                        if row["final_balance"] or row["total_received"] > 0:
                            find_wallet()
                            break
                except:
                    pass

                query = []
                print(str(counter) + ' ------------------------')
                print('🔁 Total Checked 👇' + str(total))
                print('Private Key (DEC) : ' + seed)
                print('Page Number : ' + str(pagenumber))
                print('Sleep For 10 Seconds')
                time.sleep(10)
            
        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)


        elif event == 'mizogg':
            webbrowser.open_new_tab("https://mizogg.co.uk")
        
        elif event == 'face':
            webbrowser.open_new_tab("https://github.com/Mizogg")

    
    window.Close()
    
main()

