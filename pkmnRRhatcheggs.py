import pyautogui
import pydirectinput
import time


# Configuração de teclas (ajuste conforme a configuração do seu emulador)
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Exemplo de padrão de movimento (ajuste conforme necessário)
while True:
    pydirectinput.keyDown('left')
    time.sleep(1.5)
    pydirectinput.keyUp('left')
    
    pydirectinput.keyDown('right')
    time.sleep(1.5)
    pydirectinput.keyUp('right')
    
