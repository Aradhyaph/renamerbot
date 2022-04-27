from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import UserNotParticipant
import humanize
import logging
from Translation import mr
from helper.database import  insert 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@Client.on_message(filters.private & not_subscribed)
async def not_subscribed(client, message):
    await message.reply_text(
       text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)]
           ])
       )
    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo="https://telegra.ph/file/2e2a07e86066538ed7406.jpg",
       caption=f"""👋 Hai {message.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! \n𝙱𝙾𝚃 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢: @mr_MKN & @Mr_MKN_TG \n 🤩""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("👨‍💻 OWNER 👨‍💻", url='https://t.me/mr_MKN')
          ],[
          InlineKeyboardButton('📢 UPDATES', url='https://t.me/mkn_bots_updates'),
          InlineKeyboardButton('ℹ️ SUPPORT', url='https://t.me/MKN_BOTZ_DISCUSSION_GROUP')
          ],[
          InlineKeyboardButton('🛡️ About', callback_data='about'),
          InlineKeyboardButton('ℹ️ Help', url='https://t.me/mrmoviesseries_print')
          ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = message.document or message.video or message.audio 
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename"),
        InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.username),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

async def is_subscribed(client, message):
   if not client.force_channel:
      return True
   try:             
      user = await client.get_chat_member(client.force_channel, message.from_user.id)
   except UserNotParticipant:
      pass
   else:
      if user.status != "kicked":
         return True 
   return False
