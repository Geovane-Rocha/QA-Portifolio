from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_usuario_bloqueado():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://www.saucedemo.com")

        # Tenta login com usuário bloqueado
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verifica se apareceu mensagem de erro
        erro = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )

        assert "locked out" in erro.text.lower()
        print("✅ Teste passou — Usuário bloqueado não conseguiu logar!")

    finally:
        driver.quit()

################################################################################

def test_detalhes_produto():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        # Login
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Espera página de produtos
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )

        # Clica no primeiro produto
        driver.find_element(By.CLASS_NAME, "inventory_item_name").click()

        # Espera página de detalhes
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_details"))
        )

        # Verifica se tem nome do produto
        nome = driver.find_element(By.CLASS_NAME, "inventory_details_name")
        assert nome.text != ""

        # Verifica se tem preço
        preco = driver.find_element(By.CLASS_NAME, "inventory_details_price")
        assert preco.text != ""

        # Verifica se tem botão Add to cart
        botao = driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart']")
        assert botao.is_displayed()

        print(f"✅ Teste passou — Página de detalhes do produto '{nome.text}' carregada!")

    finally:
        driver.quit()