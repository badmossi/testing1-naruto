import os

class Config(object):
    # Telegram Bot ka token
   BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    # Telegram API ki ID
    API_ID = os.getenv("API_ID", "25255466")
    API_HASH = os.getenv("API_HASH", "aa797f1169fb6bbee3de4869d6b76165")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    DB_URL = os.getenv("MONGO_DB", "mongodb+srv://magova4048:yT7D4gPAggGSRySe@cluster0.vh5qgb5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    ADMIN_ID = list(map(int, os.getenv("OWNER_ID", "7877249692").split())) # list seperated via space
    DB_NAME = os.getenv("DB_NAME", "magova4048")
    STRING = os.getenv("STRING", None) # optional
    TXT_LOG = int(os.getenv("TXT_LOG", "-1002628407675")) # optional with -100
    HIT_LOG = int(os.getenv("HIT_LOG", "-1002628407675")) # optional with -100
    DRM_DUMP = int(os.getenv("DRM_DUMP", "-1002628407675")) # optional with -100
    # Main channel ki ID
    CHANNEL = int(os.getenv("DRM_DUMP", "-1002542800168"))
    # Channel ka link
    CH_URL = "https://t.me/+Bc5r4pIjqkczMWVl"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/daddyfrrr"
    # Thumbnail image ka URL
    THUMB_URL = "https://iili.io/F57zSDv.md.jpg" #Replace by with your Thumb URL
