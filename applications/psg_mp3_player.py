import PySimpleGUI as sg
import vlc


controls = [sg.Button("Play"), sg.Button("Pause"), sg.Button("Stop")]

layout = [[sg.FileBrowse(key="-MP3-", enable_events=True)], controls]
player = None

# Create the window
window = sg.Window("MP3 Player", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    if event == "-MP3-":
        player = vlc.MediaPlayer(values['-MP3-'])
    if event == "Play" and player is not None:
        player.play()
    if event == "Pause" and player is not None:
        player.pause()
    if event == "Stop" and player is not None:
        player.stop()

window.close()