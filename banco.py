import webbrowser,pyautogui

from time import sleep

webbrowser.open('https://api.whatsapp.com/send?phone=51955516189')

sleep(5)
pyautogui.typewrite('______________________________________________________________')
pyautogui.press('enter')
pyautogui.typewrite('Hola le hablamos del banco xxxxxxxxxxx, para recordarle que debe pagar su deuda por un monto de xxxxxxxx\nSaludos :)')
pyautogui.press('enter')
