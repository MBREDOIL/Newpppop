import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # Telegram API ki ID
    API_ID = 21705536
    # Telegram API ki hash key
    API_HASH = "c5bb241f6e3ecf33fe68a444e288de2d"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '6556141430'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = os.environ.get("DB_URL", "")
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002349402727
    # Authentication log channel ki ID
    AUTH_LOG = -1002349402727
    # Hit log channel ki ID
    HIT_LOG = -1002349402727
    # DRM dump channel ki ID
    DRM_DUMP = -1002349402727
    # Main channel ki ID
    CHANNEL = -1002349402727
    # Channel ka link
    CH_URL = "https://t.me/uihash"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/uihash"
    # Thumbnail image ka URL
    THUMB_URL = "https://envs.sh/ajv.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

