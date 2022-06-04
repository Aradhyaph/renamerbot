from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from Translation import mr
from helper.database import  insert 
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**sorry bro നിങ്ങൾ ഞങ്ങളുടെ ഗ്രൂപ്പിൽ ജോയിൻ ചെയ്തിട്ടില്ല താഴെയുള്ള ബട്ടനിൽ ക്ലിക്ക് ചെയ്ത് join ചെയ്യൂ എന്നിട്ട് വീണ്ടും start കൊടുക്കൂ 🙏**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="📢Join My Group", url=client.invitelink)]
           ])
       )
    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo="https://telegra.ph/file/2e2a07e86066538ed7406.jpg",
       caption=f"""👋 Hai {message.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! \n𝙱𝙾𝚃 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢: @mr_MKN & @Mr_MKN_TG \n 🤩""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("OWNER", url='https://t.me/POPCORN_SCOPE')
          ],[
          InlineKeyboardButton('MOVIE REQUEST GROUP', url='https://t.me/POPCORN_SCOPE_MOVIEZ'),
          InlineKeyboardButton('MAIN GROUP', url='https://t.me/POPCORN_SCOPE')
          ],[
          InlineKeyboardButton(' About', callback_data='about'),
          ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- `{filesize}`",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("⚡️RENAME⚡️ ",callback_data = "rename"),
        InlineKeyboardButton("🔴CANCEL🔴",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.username),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(" 𝙲𝙻𝙾𝚂𝙴", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
