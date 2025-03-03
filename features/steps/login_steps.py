from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pytest import fixture


@fixture(scope="function")
def login_page(authed_page):
    login_page = LoginPage(authed_page)
    yield login_page

@given("我在登录页面", target_fixture="login_page")
def navigate_to_login_page(login_page):
    login_page.navigate_to_login("https://testcenter.qdhdkj.com/login")

@when(parsers.parse('我输入用户名 "<username>" 和密码 "<password>"'))
def login(login_page, username: str, password: str):
    login_page.fill_login_form(username, password)

@when("点击登录按钮")
def submit_login(login_page):
    login_page.submit_login()

@then("我应该跳转到 Dashboard 页面")
def assert_logged(login_page):
    login_page.assert_logged()

