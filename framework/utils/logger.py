# ============================================
# 统一日志管理模块（唯一职责：日志）
# - 控制台 + 文件双输出
# - 统一格式
# - 支持不同日志级别
# - 不依赖 pytest，不侵入业务
# ============================================

import logging
import os
from datetime import datetime

# 日志目录（相对项目根目录）
LOG_DIR = os.path.join(os.getcwd(), "logs")

# 确保日志目录存在
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 日志文件名（按时间）
LOG_FILE = os.path.join(
    LOG_DIR,
    f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

# 全局 logger 名称（统一）
LOGGER_NAME = "automation_logger"


def get_logger():
    """
    获取全局统一 logger
    多次调用不会重复添加 handler
    """
    logger = logging.getLogger(LOGGER_NAME)

    # 避免重复初始化
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # ===============================
    # 日志格式
    # ===============================
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ===============================
    # 控制台 Handler
    # ===============================
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # ===============================
    # 文件 Handler
    # ===============================
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # ===============================
    # 绑定 handler
    # ===============================
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
