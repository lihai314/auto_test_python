import pytest
import logging
from playwright.sync_api import sync_playwright

# 初始化日志
log = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def playwright():
    """创建 Playwright 实例（整个测试会话只执行一次）"""
    with sync_playwright() as p:
        log.info("初始化 Playwright")
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    """启动 Chromium 浏览器（整个测试会话共用）"""
    browser = playwright.chromium.launch(headless=True)
    log.info("启动 Chromium 浏览器")
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


# 新增模块级登录上下文 + 分层页面fixture
@pytest.fixture(scope="module")
def logged_in_context(browser):
    """模块级登录上下文（每个测试模块共享登录状态）"""
    # 创建新上下文
    context = browser.new_context(
        viewport={"width":1920, "height":1080}
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def authed_page(logged_in_context):
    """基于已登录上下文的认证页面（每个测试用例独立页面）"""
    page = logged_in_context.new_page()
    yield page
    # 不需要显式关闭页面，因为关闭上下文时会自动关闭所有页面
