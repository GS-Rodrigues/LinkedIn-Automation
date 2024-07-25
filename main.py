from selenium.webdriver.support.ui import WebDriverWait
from Utils.search import  pesquisar_keyword, filtrar_pessoas
from Utils.browser import iniciar_navegador
from Utils.connect import conectar_pessoas
from Utils.login import fazer_login
from config import people_interest
import time

def main():
    # Função principal que executa todas as outras funções
    navegador = iniciar_navegador()
    fazer_login(navegador)
    wait = WebDriverWait(navegador, 60)
    pesquisar_keyword(wait, people_interest)
    filtrar_pessoas(wait)
    conectar_pessoas(navegador)
    time.sleep(120)

if __name__ == "__main__":
    main()
