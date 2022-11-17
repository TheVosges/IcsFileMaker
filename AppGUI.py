import os

import PySimpleGUI as sg
import re
import csv
from textwrap import wrap
import QRCodeGeneration.QRCodeGenerator
from FileGeneration.createICSfile import createIcsFile
import random
import string
from FileGeneration.Data import dlpServer
from QRCodeGeneration import QRCodeGenerator as qr

# Colors
darkColor=('#004AAD')
lightColor=('#00C2CB')

# Fonts
font = ("ABeeZee", 11)
font2 = ("ABeeZee", 13)

# Theme
sg.theme("LightGrey1")

content = [
    ['Laroaks', '2.5 tabl. (2.5 mg)', '29.10.2021', '31.10.2021', '12:00:00']
    ,['Derundahl', '1 tabl. (10mg)', '01.11.2021', '14.11.2021', '19:00:00']
]
headers = ["nzwa_leku", "opis_dawki", "okres_od", "okres_do", "godzina_dawki"]
headings = ['Drug name', 'Dose desc.', 'Date from', 'Date to', 'Drug intake time']

layout = [
    [sg.Text(" ", size=(10, 1), key='-text-')],
    [sg.Image(filename="MedPlan.png")],
    [sg.Text(" ", size=(10, 1), key='-text-')],
    [sg.Text('Please enter your drug info:', font=font2)],
    [sg.Text('Drug name: ', size =(15, 1), font=font), sg.InputText("Paracetamol", key='name', font=font)],
    [sg.Text('Dose description: ', size =(15, 1), font=font), sg.InputText("1 tabsa", key='desc', font=font)],
    [sg.Text('Date from', size =(15, 1), font=font), sg.InputText("20.10.2022", key='date_from', font=font)],
    [sg.Text('Date to', size =(15, 1), font=font), sg.InputText("25.10.2022", key='date_to', font=font)],
    [sg.Text('Drug intake time: ', size =(15, 1), font=font), sg.InputText("19:00:00", key='intake_time', size =(34, 1), font=font), sg.Submit('Submit', button_color=darkColor, size =(8, 1), font=font)],
    [sg.Text(" ", size=(10, 1), key='-text-', font=font)],
    [sg.Table(values=content,
              font=font,
              headings=headings,
              max_col_width=35,
              auto_size_columns=True,
              display_row_numbers=True,
              justification='center',
              num_rows=7,
              key='-TABLE-',
              row_height=35)],
    [[sg.Button('Create events', button_color=darkColor, size =(12, 1), font=font), sg.Button('Remove', button_color=lightColor, size =(12, 1), font=font)]],
    [sg.Text(" ", size=(10, 1), key='-text-')],
]

window = sg.Window("Home", layout, element_justification='center')

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def popup(title, filename, message, width=70):

    lines = list(map(lambda line:wrap(line, width=width), message.split('\n')))
    height = sum(map(len, lines))
    message = '\n'.join(map('\n'.join, lines))

    layout = [
        [sg.Image(filename=filename, expand_x=True)],
        [sg.Text(message, size=(width, height), justification='center', expand_x=True)]
    ]

    sg.Window(title, layout, keep_on_top=True, modal=True).read(close=2000)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        date = re.compile('.{2}..{2}..{4}')
        time = re.compile('.{2}:.{2}:.{2}')
        if not date.match(str(values["date_from"])):
            sg.Popup('Wrong date from format! Should be dd.mm.yyyy')
        if not date.match(str(values["date_to"])):
            sg.Popup('Wrong date to format! Should be dd.mm.yyyy')
        if not time.match(str(values["intake_time"])):
            sg.Popup('Wrong time of intake format!  Should be hh:mm:ss')
        else:
            new_event = [values["name"], values["desc"], values["date_from"], values["date_to"], values["intake_time"]]
            content.append(new_event)
    if event == 'Remove':
        selected_rows = values['-TABLE-']
        selected_rows.sort(reverse=True)
        for row in selected_rows:
            del content[row]

    if event == "Create events":
        with open('FileGeneration/output.csv', 'w') as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(headings)
            writer.writerows(content)
        filename = get_random_string(8)
        createIcsFile(filename= filename)
        ftp = dlpServer.FTPServerConnection()
        ftp.upload_file(filename= filename + ".ics")
        ftp.list_files()
        qr.saveQRCode(filename)
        popup('QRCode', os.getcwd() + "/FileGeneration/Data/" + filename + ".png", "")



    window['-TABLE-'].update(content)

window.close()