import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """
    所有 Page Object 的父类
    统一负责：
    - locator 获取
    - 显式等待
    - 元素操作
    - 日志打印
    """

    def __init__(self, driver, locator_loader, page_name, timeout=10):
        self.driver = driver
        self.locator_loader = locator_loader
        self.page_name = page_name
        self.wait = WebDriverWait(driver, timeout)
        self.log = logging.getLogger(self.__class__.__name__)

    # =========================
    # locator & element
    # =========================

    def _get_locator(self, name: str):
        """
        从 locator.yaml 中获取 locator
        """
        loc = self.locator_loader.get(self.page_name, name)
        return loc["by"], loc["value"]

    def _find(self, name: str):
        """
        查找元素（带等待）
        """
        by, value = self._get_locator(name)
        self.log.debug(f"Locate element [{self.page_name}.{name}] -> ({by}, {value})")
        try:
            return self.wait.until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            self.log.error(f"Element not found: {self.page_name}.{name}")
            raise

    # =========================
    # 基础动作封装（带日志）
    # =========================

    def click(self, name: str):
        """
        点击元素
        """
        self.log.info(f"Click [{self.page_name}.{name}]")
        element = self._find(name)
        element.click()

    def input(self, name: str, value: str, clear=True):
        """
        输入文本
        """
        self.log.info(f"Input [{self.page_name}.{name}] -> {value}")
        element = self._find(name)
        if clear:
            element.clear()
        element.send_keys(value)

    def get_text(self, name: str) -> str:
        """
        获取文本
        """
        element = self._find(name)
        text = element.text
        self.log.info(f"Get text [{self.page_name}.{name}] -> {text}")
        return text

    def is_visible(self, name: str) -> bool:
        """
        判断元素是否可见
        """
        by, value = self._get_locator(name)
        try:
            self.wait.until(EC.visibility_of_element_located((by, value)))
            self.log.info(f"Element visible [{self.page_name}.{name}]")
            return True
        except TimeoutException:
            self.log.warning(f"Element NOT visible [{self.page_name}.{name}]")
            return False
