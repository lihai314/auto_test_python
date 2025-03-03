from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pytest import fixture


@fixture(scope="function")
def login_page(page):
    login_page = LoginPage(page)
    yield login_page

@given("我在登录页面", target_fixture="login_page")
def navigate_to_login_page(login_page):
    login_page.navigate_to_login("https://testcenter.qdhdkj.com/login")

@when('我输入用户名 "<username>" 和密码 "<password>"')
def login(login_page: LoginPage, username: str, password: str):
    login_page.fill_login_form(username, password)

@then("我应该看到登录成功后的页面")
def logged(login_page: LoginPage, dashboard_text: str):
    login_page.submit_login(dashboard_text)

