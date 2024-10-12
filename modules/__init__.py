# modules/__init__.py

from .news_module import NewsProvider

# 如果你后续添加了更多模块，也可以在这里导入
# from .stock_module import StockProvider

# 创建一个字典，将模块名称映射到对应的类
module_classes = {
    'NewsProvider': NewsProvider,
    # 'StockProvider': StockProvider,  # 如果你添加了股票模块，可以取消这行的注释
}
