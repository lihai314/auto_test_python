import logging
from playwright.sync_api import Page

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")  # 等待页面加载完成
        log.info(f"跳转至 {url}")

