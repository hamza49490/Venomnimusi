import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from  https://api.imgbb.com/
API_KEY = getenv("API_KEY", "0f5d932a8fdbedfb696b039a1f177a3f") 

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24066716"))
API_HASH = getenv("API_HASH", "09e30e6e0b1a4c71e43a055979c51b3b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6508386922:AAGZEJ921cisv5yoUKYP1z7cDdP6t5gRV_s")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kingbrukh:kingkhan@kingbruh.ra3pjgm.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002028213552"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7784476491"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/hamza49490/Venomnimusi",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/konnusanlar")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/konnusanlar")


AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGQinYAcTJcN9AEyEBRVIT4-Ly64BG4AwiwMuZEDxk9x1_x4Op9zGSOAuYbxxLHz-MNplvDFvgc9F0ui0PlLB35J7hQaQKQr_2zwpBnt_kfWoNzrnLiVQwtTUJ4Fvcr47Yn9eo-es043tB06BJiIb8CTavVMRSrm0-eRJAn7-IbRD5YRZ_C21Z8c8n6UQG6298VSNpvKt1bqYpv2quxqSNbCHn3rvf1Q2_FB6QipLTOcjvVGJBl3kL39jJtTkvnnEQ9xhBRoNHkmdGt3QMY4nzebPNwL1CqzatQH-sX0BI7rZ2f7c171j-QITr4EfwA6iwLdBsQAU2a7051m1ui_Xw-GULHUgAAAAGOWX0JAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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
