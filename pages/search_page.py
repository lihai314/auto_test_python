# pages/search_page.py
from playwright.sync_api import Page, expect
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("#kw")
        self.search_button = page.locator("#su")
        self.search_results = page.locator(".result")  # 使用更准确的百度搜索结果选择器

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")  # 等待页面加载完成
        log.info(f"跳转至 {url}")

    def search(self, input_value: str):
        self.search_input.fill(input_value)
        log.info(f"输入：{input_value}")

    def click_search_button(self):
        self.search_button.click()
        log.info(f"点击搜索按钮")
        self.page.wait_for_load_state("networkidle")  # 等待搜索完成

    def assert_search_results_visible(self):
        expect(self.search_results.first).to_be_visible()  # 验证第一个结果可见
        log.info("搜索结果可见")
