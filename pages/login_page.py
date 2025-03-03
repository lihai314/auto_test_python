# pages/login_page.py
import logging

from playwright.sync_api import Page, expect

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("请输入登录的手机号")
        self.password_input = page.get_by_placeholder("请输入登录密码")
        self.submit_button = page.get_by_role("button", name="立即登录")

    def navigate_to_login(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
        log.info(f"导航到: {url}")

    def fill_login_form(self, username: str, password: str):
        self.username_input.fill(username)
        log.info(f"输入登录账户：{username}")
        self.password_input.fill(password)
        log.info(f"输入密码: {password}")

    def submit_login(self):
        self.submit_button.click()
        log.info(f"点击登录按钮成功")

    def assert_logged(self):
        assert "dashboard" in self.page.url, "登录后未跳转到 Dashboard 页面"
