"""
邮件发送系统配置文件示例
复制此文件为 config.py 并修改相应配置
"""

# ==================== 邮箱配置 ====================
EMAIL_CONFIG = {
    # 发件人邮箱
    'sender_email': 'xingyun1982314@126.com',
    
    # 发件人邮箱授权码（不是登录密码！）
    # 126邮箱授权码获取方法：
    # 1. 登录 mail.126.com
    # 2. 设置 → POP3/SMTP/IMAP
    # 3. 开启SMTP服务
    # 4. 生成授权码
    'sender_password': 'MKYurXXfTuE9uZ4p',
    
    # 收件人邮箱（可以和发件人相同）
    'receiver_email': 'xingyun1982314@126.com',
    
    # SMTP服务器地址
    'smtp_server': 'smtp.126.com',
    
    # SMTP端口（SSL加密端口）
    'smtp_port': 465
}

# ==================== 其他邮箱配置参考 ====================
"""
# QQ邮箱配置
EMAIL_CONFIG = {
    'sender_email': 'your_email@qq.com',
    'sender_password': 'your_auth_code',  # QQ邮箱授权码
    'receiver_email': 'receiver@email.com',
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 465
}

# 163邮箱配置
EMAIL_CONFIG = {
    'sender_email': 'your_email@163.com',
    'sender_password': 'your_auth_code',  # 163邮箱授权码
    'receiver_email': 'receiver@email.com',
    'smtp_server': 'smtp.163.com',
    'smtp_port': 465
}

# Gmail配置（需要科学上网）
EMAIL_CONFIG = {
    'sender_email': 'your_email@gmail.com',
    'sender_password': 'your_app_password',  # Gmail应用专用密码
    'receiver_email': 'receiver@email.com',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587  # 或 465
}
"""

# ==================== 时间配置 ====================
# 每天发送时间（24小时格式）
SEND_TIME = "08:00"

# 学习计划起始日期
# Day 1 对应的日期
STUDY_START_DATE = {
    'year': 2026,
    'month': 1,
    'day': 29
}

# ==================== 路径配置 ====================
# 学习任务文件夹名称
DAILY_TASKS_FOLDER = 'DailyTasks'

# 输出Word文档的文件夹名称
OUTPUT_FOLDER = 'output_docs'

# ==================== 日志配置 ====================
# 日志文件名
LOG_FILE = 'study_mailer.log'

# 日志级别（DEBUG, INFO, WARNING, ERROR, CRITICAL）
LOG_LEVEL = 'INFO'

