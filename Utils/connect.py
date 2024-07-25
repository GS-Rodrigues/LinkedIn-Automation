import time
from selenium.webdriver.common.by import By
from random import uniform
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def remove_non_bmp_characters(text):
    # Remove caracteres não BMP do texto
    return ''.join(char for char in text if ord(char) <= 0xFFFF)

def conectar_pessoas(navegador):
    # Inicia o contador de páginas e uma pausa inicial
    contador = 0
    time.sleep(5)
    
    # Loop para iterar através de 10 páginas de contatos
    while contador < 10:
        contador += 1
        print(f"===\=======Carregando a {contador}º página de contato=======/===")
        time.sleep(5)

        # Seleciona todos os botões que permitem abrir perfis para conexão
        buttons = navegador.find_elements(By.XPATH, '//button[contains(@class, "artdeco-button") and .//span[text()="Connect"]]')
        
        # Se nenhum botão for encontrado, interrompe o loop
        if not buttons:
            print(f'===\======= NÃO ENCONTRADOS PERFIS CLICÁVEIS===/=======')
            break
        else:
            print(f'===\======= Buttons encontrados: {buttons}===/=======')
            
            # Itera através de cada botão para enviar solicitações de conexão
            for button in buttons:
                try:
                    # Clica no botão para enviar a solicitação de conexão
                    button.click()
                    time.sleep(uniform(1, 3))  # Pausa aleatória para evitar bloqueios

                    # Obtém o nome da pessoa a partir do perfil
                    name_object = navegador.find_element(By.XPATH, '//p[contains(@class, "display-flex")]//strong') 
                    name = name_object.text
                    name = remove_non_bmp_characters(name)

                    print(f"===\=======Nome: {name}=======/===")
                    
                    # Mensagem personalizada para a solicitação de conexão
                    mensagem = f"Olá {name},\n\nSou Guilherme, estudante de Ciência da Computação e iniciante na área de tecnologia. Gostaria de me conectar com você para compartilharmos nossa rede de contatos. \nObrigado e espero que possamos nos conectar! \n\nAtenciosamente,\nGuilherme."
                    print(mensagem)

                    # Adiciona uma nota personalizada na solicitação de conexão
                    note_button = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "artdeco-button") and contains(@class, "artdeco-button--secondary") and .//span[text()="Add a note"]]')))
                    note_button.click()

                    # Envia a mensagem personalizada
                    textbox = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="custom-message"]')))
                    textbox.send_keys(mensagem)
                    time.sleep(2)
                    send_button = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "artdeco-button--primary") and .//span[text()="Send"]]')))
                    send_button.click()

                    # Pausa para garantir que a ação seja registrada
                    time.sleep(3)
                except Exception as e:
                    # Captura e imprime qualquer erro que ocorra durante a conexão
                    print(f"===\=======Erro ao conectar ao usuário=======/===: {e}")
                    break

            # Navega para a próxima página de resultados de pesquisa
            next_button = navegador.find_element(By.XPATH, '//button[contains(@class, "artdeco-pagination__button--next") and .//span[text()="Next"]]')
            next_button.click()
            print(f"===\=======Indo para a próxima página de pesquisa=======/===: {e}")
