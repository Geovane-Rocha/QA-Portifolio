from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_valido():
    # Abre o navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Acessa o site
    driver.get("https://www.saucedemo.com")
    
    # Digita o usuário
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # Digita a senha
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Clica no botão login
    driver.find_element(By.ID, "login-button").click()
    
    # Aguarda 2 segundos
    time.sleep(2)
    
    # Verifica se foi para página de produtos
    assert "inventory" in driver.current_url
    
    print("✅ Teste passou — Login realizado com sucesso!")
    
    # Fecha o navegador
    driver.quit()

def test_login_invalido():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.saucedemo.com")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(2)
    
    # Verifica se apareceu mensagem de erro
    erro = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert erro.is_displayed()
    
    print("✅ Teste passou — Mensagem de erro exibida corretamente!")
    
    driver.quit()