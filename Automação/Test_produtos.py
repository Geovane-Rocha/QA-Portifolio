from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )

def test_filtro_preco_menor_maior():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login(driver)

        # Seleciona filtro de menor para maior preço
        filtro = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        filtro.select_by_value("lohi")

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # Pega todos os preços
        precos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        valores = [float(p.text.replace("$", "")) for p in precos]

        # Verifica se está em ordem crescente
        assert valores == sorted(valores)
        print("✅ Teste passou — Filtro de menor para maior preço funcionando!")

    finally:
        driver.quit()
        
#########################################################################

def test_filtro_nome_z_a():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login(driver)

        # Seleciona filtro Z-A
        filtro = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        filtro.select_by_value("za")

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # Pega todos os nomes
        nomes = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        lista_nomes = [n.text for n in nomes]

        # Verifica se está em ordem decrescente
        assert lista_nomes == sorted(lista_nomes, reverse=True)
        print("✅ Teste passou — Filtro Z-A funcionando!")

    finally:
        driver.quit()
        
############################################################################

def test_remover_produto_carrinho():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login(driver)

        # Adiciona produto ao carrinho
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()

        # Verifica se carrinho tem 1 item
        carrinho = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
        )
        assert carrinho.text == "1"

        # Remove o produto
        driver.find_element(By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']").click()

        # Verifica se o badge do carrinho sumiu
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
        )

        print("✅ Teste passou — Produto removido do carrinho!")

    finally:
        driver.quit()
        

