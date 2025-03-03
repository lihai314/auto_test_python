import pytest
from pytest_bdd import scenario


@pytest.mark.smoke
@scenario('../features/login.feature', '成功登录')
def test_successful_login():
    """
    这里可以添加额外的测试逻辑,比如:
    - 添加详细的日志记录
    - 截图保存
    - 额外的断言检查
    - 测试数据清理等
    """
    pass

@pytest.mark.smoke
@scenario('../features/login.feature', '失败登录')
def test_failed_login():
    pass
