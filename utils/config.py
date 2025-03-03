# config.py

class Config:
    ENVIRONMENTS = {
        'dev': 'localhost',
        'test': 'https://testcenter.qdhdkj.com/login',
        'prod': 'https://center.maxengine.cn/login'
    }
    DEFAULT_ENV = 'test'

config = Config()
