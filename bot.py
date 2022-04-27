import os 
import logging
from pyrogram import Client

logging.basicConfig(
  filename='rename-bot.txt',
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.username = me.username 
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)
            self.invitelink = link
         except Exception as e:
            logging.warning(e) 
            logging.warning("Make Sure Bot admin in force sub channel") 
            self.force_channel = None
       logging.info(f"{me.first_name} Started")
        
    async def stop(self, *args):
      await super().stop()
      logging.info("Bot Stopped")
        
bot = Bot()
bot.run()
