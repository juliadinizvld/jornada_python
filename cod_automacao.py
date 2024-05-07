# automação de tarefas 
# 1. abrir o sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
# para instalar: pip install pyautogui
import pyautogui # importando a biblioteca
pyautogui.PAUSE = 1 # tempo entre os comandos

# pyautogui.click -> clicar com o mouse 
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla

# 1. entrar no navegador (Chrome)  
pyautogui.press("win")
pyautogui.write("Chorme")
pyautogui.press("enter")
# 1.1 entrar no site 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# 1.2 fazer login 
pyautogui.press("tab")
pyautogui.write("juliadiniz@hotmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
# 2. cadastrar produtos 
pyautogui.press("tab")

# 3. Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl



