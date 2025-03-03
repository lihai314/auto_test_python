from pytest_bdd import given, when, then, parsers
from pages.search_page import SearchPage
from pytest import fixture

# 直接使用已登录的 authed_page
@fixture(scope="function")
def search_page(authed_page):
    search_page = SearchPage(authed_page)
    yield search_page

@given('我在百度搜索页面',target_fixture="search_page")
def navigate_to_search_page(search_page):
    search_page.navigate("https://www.baidu.cn")

@when(parsers.parse('我输入搜索词 "<search_term>"'))
def enter_search_term(search_page, search_term: str):
    search_page.search(search_term)

@when('我输入空的搜索词')
def enter_empty_search_term(search_page):
    search_page.search(" ")

@when('点击搜索按钮')
def click_search_button(search_page):
    search_page.click_search_button()

@then('我应该看到搜索结果')
def see_search_results(search_page):
    search_page.assert_search_results_visible()

