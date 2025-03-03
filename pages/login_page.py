# pages/login_page.py
from playwright.sync_api import Page, expect
import logging

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
        log.info(f"Navigated to login page: {url}")

    def fill_login_form(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        log.info(f"filled LoinForm: {username,password}")

    def submit_login(self,dashboard_text):
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_title(dashboard_text)