import webbrowser,pyautogui

from time import sleep

webbrowser.open('https://api.whatsapp.com/send?phone=51955516189')

sleep(5)

with open('texto.txt') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        sleep(1)

