# config.py

BOT_TOKEN = ''
CHAT_ID = ''
NEWS_API_KEY = ''

# 定义要使用的模块
ACTIVE_MODULES = ['NewsProvider']

# 模块特定配置
MODULE_CONFIG = {
    'NewsProvider': {
        'api_key': NEWS_API_KEY
    }
}