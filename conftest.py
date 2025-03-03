from pathlib import Path
import pytest
import logging
from playwright.sync_api import sync_playwright
from utils.config import Config


# 初始化日志
log = logging.getLogger(__name__)
root_path = Path(__file__).resolve().parent

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium", help="要使用的浏览器: chromium, firefox, or webkit")
    parser.addoption("--headless", action="store_true", default=False, help="运行浏览器无头模式")
    parser.addoption("--env", action="store", default=Config.DEFAULT_ENV, help="要测试的环境: dev, test, or prod")

@pytest.fixture(scope="session")
def playwright():
    """创建 Playwright 实例（整个测试会话只执行一次）"""
    with sync_playwright() as p:
        log.info("初始化 Playwright")
        yield p

@pytest.fixture(scope="function")
def browser_type(playwright, request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chromium":
        return playwright.chromium
    elif browser_name == "firefox":
        return playwright.firefox
    elif browser_name == "webkit":
        return playwright.webkit
    else:
        raise ValueError(f"不支持的浏览器: {browser_name}")

@pytest.fixture(scope="function")
def base_url(request):
    env = request.config.getoption("--env")
    if env not in Config.ENVIRONMENTS:
        raise ValueError(f"不支持的环境: {env}")
    return Config.ENVIRONMENTS[env]


@pytest.fixture(scope="session")
def browser(browser_type, request):
    headless = request.config.getoption("--headless")
    browser = browser_type.launch(headless=headless)
    log.info(f"启动浏览器: {browser_type.name}, 无头模式: {headless}")
    yield browser
    browser.close()
    log.info("关闭 Chromium 浏览器")

@pytest.fixture(scope="function")
def context(browser):
    """为每个测试用例创建新上下文（隔离 cookies 和缓存）"""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    yield context
    context.close()  # 关闭上下文时会自动关闭所有关联页面

@pytest.fixture(scope="function")
def page(context):
    """为每个测试用例创建新页面，失败时自动截图"""
    page = context.new_page()
    yield page
    # 不需要显式关闭页面，因为关闭上下文时会自动关闭所有页面
