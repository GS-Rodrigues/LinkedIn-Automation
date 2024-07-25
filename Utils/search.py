from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def pesquisar_keyword(wait, keyword):
    # Realiza uma pesquisa no LinkedIn usando a palavra-chave fornecida
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav-typeahead"]/input')))
    search_button.click()
    search_button.send_keys(keyword)
    search_button.send_keys(Keys.RETURN)
    print(f"===\=======Pesquisado: {keyword}=======/===")

def filtrar_pessoas(driver_wait):
    # Filtra os resultados da pesquisa para mostrar apenas pessoas
    peoplefilter_button = driver_wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'search-reusables__filter-pill-button') and text()='People']")))
    peoplefilter_button.click()
    print(f"===\=======Filtrado por pessoas=======/===")
