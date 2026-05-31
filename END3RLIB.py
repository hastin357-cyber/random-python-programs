from pynput.mouse import Button, Controller
import pygetwindow
def move_in_window(windowTitle:str, x:float, y:float):
    m = Controller()

    window = pygetwindow.getWindowsWithTitle(windowTitle)

    window:pygetwindow.Win32Window = window[0]

    m.position = (x + window.topleft.x, y + window.topleft.y)

move_in_window("Calculator", 50, 50)