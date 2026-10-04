from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

logger = logging.getLogger(__name__)

class BasePage: #это родительский класс над всеми страницами, технический слой.
                # И если нужны логи этих действий, то лучше через DEBUG (он показывает, как именно селениум выполняет эти действия),
                # а не через INFO (он показывает, что делает тест).
                # При этом метод find() не логируем, а то будет очень много техн. шума.
    def __init__(self,driver):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def click(self,locator):
        self.find(locator).click()

    def fill(self,locator,value):
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def get_alert_text(self):
        alert = WebDriverWait(self.driver,timeout=5).until(
            EC.alert_is_present()
            )
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()


