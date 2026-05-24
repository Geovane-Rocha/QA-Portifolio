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
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_adicionar_produto_carrinho():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Espera página carregar
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )

        # Adiciona produto
        botao = driver.find_element(
            By.CSS_SELECTOR,
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )

        botao.click()

        # Espera carrinho aparecer
        carrinho = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
            )
        )

        assert carrinho.text == "1"

        print("✅ Teste passou — Produto adicionado ao carrinho!")

    finally:
        driver.quit()
        
def test_checkout_completo():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )

        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()

        driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )

        driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        driver.find_element(By.ID, "first-name").send_keys("Geovane")
        driver.find_element(By.ID, "last-name").send_keys("Rocha")
        driver.find_element(By.ID, "postal-code").send_keys("12345")

        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='finish']"))
        )

        driver.find_element(By.CSS_SELECTOR, "[data-test='finish']").click()

        mensagem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='complete-header']"))
        )

        assert mensagem.text == "Thank you for your order!"
        print("✅ Teste passou — Checkout completo com sucesso!")

    finally:
        driver.quit()