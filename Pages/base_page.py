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

    def click(self, locator):
        logger.debug(f"Click on  {locator}")
        self.wait_until_clicable(locator).click()

    def fill(self, locator, value):
        logger.debug(f"Fill{locator} with {value}")
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_alert_text(self):
        # alert = WebDriverWait(self.driver,timeout=5).until(
        #     EC.alert_is_present())
        return self.wait_until_alert_present().text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def wait_until_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_clicable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_url_matches(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(locator))

    def wait_until_alert_present(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())


