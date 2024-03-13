# Passo a passo do projeto

# 1º passo - Entrar no sistema da empresa
## https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time

# clicar - pyautogui.click
# escrever - pyautogui.write
# apertar uma tecla - pyautogui.press
# apertar - pyautogui.hotkey
pyautogui.PAUSE = 0.5

# apertar tecla do windows (comand + barra de espaço)
pyautogui.press("win")
# digitar o nome do programa (chrome)
pyautogui.write("chrome")
# apertar o enter
pyautogui.press("enter")
# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar o enter
pyautogui.press("enter")
# espera 5 segundos
time.sleep(3)


# 2º passo - Fazer login
pyautogui.click(x=514, y=406)
# digitar o email
pyautogui.write("python@gmail.com")
# passar para o campo senhapython@gmail.com minha senha
pyautogui.press("tab")
# digitar a senha
pyautogui.write("minha senha")
# clicar em logar
pyautogui.click(x=667, y=569)
time.sleep(2)

# 3º passo - Importar a base de dados
# pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 

    # 4º passo - Cadastrar um produto
    pyautogui.click(x=484, y=293)
    # código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # cadastrar produto
    pyautogui.press("enter")
    # rolar para cima
    pyautogui.scroll(1000)




# 5º passo - Repetir isso até acabar a base de dados