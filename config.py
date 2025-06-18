import os

API_ID = os.environ.get("API_ID", "24388008")

API_HASH = os.environ.get("API_HASH", "12ce0703fe21215c475dc041c8595b7b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7313903978:AAFkvWwVIWeoboUYOOaWq_OwHCrkrdnPO60")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6915427808))

LOG = -1002536425571,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[6915427808]
    for x in (os.environ.get("ADMINS", "6915427808").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
