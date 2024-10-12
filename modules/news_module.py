# modules/news_module.py

import requests
from .bsse_module import BaseContentProvider

class NewsProvider(BaseContentProvider):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_content(self):
        url = f"https://newsapi.org/v2/top-headlines?country=cn&apiKey={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            articles = data['articles'][:3]  # 获取前3条新闻
            news_list = [f"- {article['title']}" for article in articles]
            return "今日头条新闻:\n" + "\n".join(news_list)
        except Exception as e:
            return f"无法获取新闻信息: {str(e)}"