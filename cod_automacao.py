# automação de tarefas 
# 1. abrir o sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
# pip install pyautogui
# pip install pandas numpy openpyxl
import pyautogui # importando a biblioteca
pyautogui.PAUSE = 1.2 # tempo entre os comandos

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
# 2. Cadastrar produtos
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 3: Repetir o processo de cadastro até o fim