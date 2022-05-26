from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
CHANNEL = getenv("CHANNEL")
BOT_NAME = getenv("BOT_NAME","جمثون")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
IMG = getenv("IMG")