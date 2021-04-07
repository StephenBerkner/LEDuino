import socket
import configparser
import PySimpleGUI as sg
import sys
import time
from multiprocessing import Process

configPath = "client.cfg"

class Client():

    def __init__(self, ip, port):
        self.server_ip = ip
        self.server_port = int(port)

    def send_message(self, msg):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.server_ip, self.server_port))
            s.sendall((msg+'\n').encode("utf-8"))
            s.close()
    
    def schedule_message(self, reps, delay, msg):
        for i in range(0, reps):
            self.send_message(msg)
            time.sleep(delay)

if __name__ == "__main__":
    # read from config file
    config = configparser.ConfigParser()
    config.read(configPath)
    s = config["leduino"]
    
    # Create client object
    c = Client(s["ip"], s["port"])

    # create PySimpleGUI Layout
    layout = [[sg.Text("Repetitions: ")], [sg.Input(key='-repititions-')],
            [sg.Text("Time Between (seconds): ")], [sg.Input(key='-delay-')],
            [sg.Text("Message: ")], [sg.Input(key='-message-')],
            [sg.Text(size=(40,1), key='-status-')],
            [sg.Button('Send'), sg.Button('Quit')]]

    window = sg.Window('LEDuino Client v' + config["settings"]["ver"], layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == 'Send':
            p = Process(target=c.schedule_message, args=(int(values['-repititions-']), int(values['-delay-']), values['-message-']))
            p.start()
            window['-status-'].update("Message Sent!")


    window.close()