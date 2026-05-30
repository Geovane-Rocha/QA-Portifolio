from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_login_valido(self, driver_logado):
        assert "inventory" in driver_logado.current_url
        print("✅ Login válido funcionando!")

    def test_login_invalido(self, driver):
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("senha_errada")
        driver.find_element(By.ID, "login-button").click()

        erro = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert erro.is_displayed()
        print("✅ Login inválido funcionando!")

class TestCarrinho:
    def test_adicionar_produto(self, driver_logado):
        driver_logado.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()

        carrinho = WebDriverWait(driver_logado, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
        )
        assert carrinho.text == "1"
        print("✅ Produto adicionado ao carrinho!")

    def test_remover_produto(self, driver_logado):
        driver_logado.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()

        WebDriverWait(driver_logado, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
        )

        driver_logado.find_element(By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']").click()

        WebDriverWait(driver_logado, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
        )
        print("✅ Produto removido do carrinho!")