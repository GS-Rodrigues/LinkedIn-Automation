from config import username_user, password_user
from selenium.webdriver.common.by import By

def fazer_login(navegador):
    # Faz o login no LinkedIn usando as credenciais fornecidas
    username = navegador.find_element(By.ID, 'username') # Campo para escrever o e-mail
    password = navegador.find_element(By.ID, 'password') # Campo para escrever a senha
    login_button = navegador.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button') # Botão para entrar no login

    username.send_keys(username_user) # E-mail de login no LinkedIn (config.py)
    password.send_keys(password_user) # Senha do LinkedIn (config.py)
    login_button.click()
    print("===\=======Linkedin Logado=======/===")
    