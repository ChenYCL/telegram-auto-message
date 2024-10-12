# Telegram 自动消息机器人

这是一个基于 Python 的 Telegram 自动消息机器人，可以定时发送消息，支持拓展。

## 功能

- 定时发送消息
- 获取并发送最新新闻头条

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/ChenYCL/telegram-auto-message.git
   cd telegram-auto-message
   ```

2. 创建并激活虚拟环境（可选但推荐）：
   ```
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 配置

1. 参考`config.exmaple.py`，新建 `config.py` 文件中，并设置以下变量：
   - `BOT_TOKEN`：您的 Telegram 机器人令牌
   - `CHAT_ID`：目标聊天或频道的 ID
   - `NEWS_API_KEY`：您的 NewsAPI 密钥
 - 参考获取token和chatid ，https://telegramcnweb.com/post/telegram%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96chat-id/

2. 如果需要，可以在 `config.py` 中调整 `ACTIVE_MODULES` 和 `MODULE_CONFIG`。
3. 调整指定发送时间参考代码
   ```python
    # 设置定时任务
    try:
        schedule.every().day.at("09:00").do(lambda: asyncio.create_task(send_update()))
        schedule.every().day.at("12:00").do(lambda: asyncio.create_task(send_update()))
        schedule.every().day.at("14:00").do(lambda: asyncio.create_task(send_update()))
        schedule.every().day.at("19:00").do(lambda: asyncio.create_task(send_update()))
   ```

## 使用

运行机器人：

机器人将开始运行，并按照预定的时间表发送消息。

## 模块

目前，该项目包含以下模块：

- NewsProvider：获取并发送最新新闻头条

您可以通过修改 `modules/__init__.py` 文件来添加或删除模块。

## 贡献

欢迎贡献！请随时提交 pull 请求或开启 issue。

## 许可

[MIT License](LICENSE)
