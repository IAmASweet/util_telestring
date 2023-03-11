from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
import os
import dotenv

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
dotenv.load_dotenv()
dotenv_file = dotenv.find_dotenv()


def set_env(key, value):
    os.environ[key] = value
    dotenv.set_key(dotenv_file, key, os.environ[key])
    return value


async def set_telestring():
    async with TelegramClient(StringSession(), int(api_id), api_hash) as client:
        telethon_string = client.session.save()
        set_env(key='TELETHON_STRING', value=telethon_string.strip())
        return telethon_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(set_telestring())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
