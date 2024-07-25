from selenium import webdriver

def iniciar_navegador():
    navegador = webdriver.Edge()
    navegador.get("https://www.linkedin.com/login")
    navegador.maximize_window()
    print("===\=======Navegador aberto=======/===")
    return navegador
