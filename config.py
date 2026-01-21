import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)

BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_USERNAME = getenv("OWNER_USERNAME","liar_neo")
BOT_USERNAME = getenv("BOT_USERNAME" , "KurumiMusicRobot")
BOT_NAME = getenv("BOT_NAME" , "𝐊ᴜʀᴜᴍɪ")
ASSUSERNAME = getenv("ASSUSERNAME" , "neo")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://snaxmusic:snaxmusic@cluster0.fat4j0o.mongodb.net/?appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1003536603139))
OWNER_ID = int(getenv("OWNER_ID", 1008989961))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "snaxymng")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/txsn4x/snaxymng",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "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")

API_URL = getenv("API_URL", 'https://pytdbotapi.thequickearn.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", None)
API_KEY = getenv("API_KEY", 'NxGBNexGenBots790d34') # youtube song api key, generate free key or buy paid plan from panel.thequickearn.xyz


PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-YukkiMusic-08-30")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/aniweb_bots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/aniweb_nexus")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
STRING1 = getenv("STRING_SESSION", None) 
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/e2ccdc8f93a67b995072c-37cdfd36f3dd2f4dbb.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/95e7a771b14e2da41d7c7-54f29bec291e2ad228.jpg")

PLAYLIST_IMG_URL = "https://graph.org/file/01f6bff76d899c77153ba-112d924074f9890051.jpg"
STATS_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
STREAM_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
