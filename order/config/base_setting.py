DEBUG = False
SERVER_PORT = 8999
SQLALCHEMY_ECHO = False

AUTH_COOKIE_NAME = "Ordering_Meals"

#过滤URL
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE = 10
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}

MINA_APP = {
    "appid":  "wx643acb9b5d77b23a",
    "appkey": "12b57e355b228d940cc4801b421db87d",
    "paykey": "xxxxxxxxxxxxxxxx",
    "mch_id": "xxxxxxxxxxxxxxxx",
    "callback_url": "/api/order/callback"
}

UPLOAD = {
    "ext": ["jpg", "gif", "bmp", "jpeg", "png"],
    "prefix_path": "/web/static/upload/",
    "prefix_url": "/static/upload/"
}

APP = {
    "domain": "http://192.168.0.102:8999"
}

PAY_STATUS_MAPPING = {
    "1":  "已支付",
    "-8": "待支付",
    "0":  "已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":  "订单关闭",
    "1":  "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}