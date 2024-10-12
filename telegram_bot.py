# telegram_bot.py

import sys
import os
import telegram
import schedule
import time
import logging
from datetime import datetime
import importlib
from config import BOT_TOKEN, CHAT_ID, ACTIVE_MODULES, MODULE_CONFIG
from telegram.ext import Application
import asyncio
from modules import module_classes

# 添加当前目录到 Python 路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 确保正确导入 schedule
try:
    import schedule
except ImportError:
    print("schedule 模块未安装。请使用 pip install schedule 安装它。")
    sys.exit(1)

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# bot = telegram.Bot(token=BOT_TOKEN)
application = Application.builder().token(BOT_TOKEN).build()

async def send_message(chat_id, text):
    await application.bot.send_message(chat_id=chat_id, text=text)

def load_modules():
    modules = []
    for module_name, module_class in module_classes.items():
        try:
            config = MODULE_CONFIG.get(module_name, {})
            instance = module_class(**config)
            modules.append(instance)
            logger.info(f"已加载模块: {module_name}")
        except Exception as e:
            logger.error(f"加载模块 {module_name} 时出错: {str(e)}")
    return modules

content_providers = load_modules()

async def send_update():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{current_time}]\n\n"

    for provider in content_providers:
        try:
            content = provider.get_content()
            message += f"{content}\n\n"
        except Exception as e:
            logger.error(f"Error getting content from {provider.__class__.__name__}: {str(e)}")

    try:
        await send_message(CHAT_ID, message)
        logger.info(f"Update sent successfully at {current_time}")
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")

async def main():
    logger.info("机器人已启动")

    # 设置定时任务
    try:
        schedule.every().day.at("09:00").do(lambda: asyncio.create_task(send_update()))
        schedule.every().day.at("12:00").do(lambda: asyncio.create_task(send_update()))
        schedule.every().day.at("14:00").do(lambda: asyncio.create_task(send_update()))
        schedule.every().day.at("19:00").do(lambda: asyncio.create_task(send_update()))
    except AttributeError:
        logger.error("schedule 模块似乎没有 every 法。请确保您安装了正确的版本。")
        return

    # 运行定时任务
    while True:
        try:
            schedule.run_pending()
            await asyncio.sleep(1)
        except Exception as e:
            logger.error(f"Error in main loop: {str(e)}")
            await asyncio.sleep(60)  # 如果发生错误，等待1分钟后继续

if __name__ == "__main__":
    asyncio.run(main())
