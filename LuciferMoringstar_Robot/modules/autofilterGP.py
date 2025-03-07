# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot
# License Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot/blob/LuciferMoringstar-Robot/LICENSE
 
import re, random, asyncio 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from LuciferMoringstar_Robot import temp, PICS, MOVIE_TEXT as REQUEST_TEXT
from LuciferMoringstar_Robot.functions import get_size, split_list, get_settings
from database.autofilter_mdb import get_filter_results

async def group_filters(client, update):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", update.text):
        return
    if 2 < len(update.text) < 100:    
        btn = []
        search = update.text
        settings = await get_settings(update.chat.id)
        MOVIE_TEXT = settings["template"]
        files = await get_filter_results(query=search)
        if not files:
            if settings["spellmode"]:
                try:
                    reply = search.replace(" ", '+')  
                    buttons = [[ InlineKeyboardButton("✅ 𝖧𝖮𝖶 𝖳𝖮 𝖲𝖤𝖠𝖱𝖢𝖧 ✅", url=f"https://t.me/Tamil_Roars/17") ],[ InlineKeyboardButton("🕵️ 𝖲𝖤𝖠𝖱𝖢𝖧 𝖨𝖭 𝖦𝖮𝖮𝖦𝖫𝖤 🕵️", url=f"https://www.google.com/search?q={reply}") ],[ InlineKeyboardButton("× 𝖢𝖫𝖮𝖲𝖤 ×", callback_data="close") ]]
                    spell = await update.reply_text(text=settings["spelltext"].format(query=search, first_name=update.from_user.first_name, last_name=update.from_user.last_name, title=update.chat.title, mention=update.from_user.mention), disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(buttons))           
                    await asyncio.sleep(60)
                    await spell.delete()
                except:
                    pass
            return
        if files:
            for file in files:
                file_id = file.file_id
                filesize = f"🎬 {get_size(file.file_size)} 🎬"
                filename = f"{file.file_name}"
                
                if settings["button"]:
                    try:
                        btn.append([InlineKeyboardButton(f"{filename}", url=f'https://playdisk.xyz/st?api=75c2abea01f77494fa5660a362e711bb2348fffb&url=https://telegram.dog/Tamil_Cinema2_Robot?start=muhammedrk-mo-tech-group-{file_id}')])
                        btn.append([InlineKeyboardButton(f"{filesize}", url=f"https://playdisk.xyz/st?api=75c2abea01f77494fa5660a362e711bb2348fffb&url=https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}")])
                    except:
                        btn.append([InlineKeyboardButton(f"{filesize}", url=f"https://playdisk.xyz/st?api=75c2abea01f77494fa5660a362e711bb2348fffb&url=https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}")])
                else:
                    try:
                        btn.append([InlineKeyboardButton(f"{filesize}", url=f'https://playdisk.xyz/st?api=75c2abea01f77494fa5660a362e711bb2348fffb&url=https://telegram.dog/Tamil_Cinema2_Robot?start=muhammedrk-mo-tech-group-{file_id}')])
                        btn.append([InlineKeyboardButton(f"{filename}", url=f'https://playdisk.xyz/st?api=75c2abea01f77494fa5660a362e711bb2348fffb&url=https://telegram.dog/Tamil_Cinema2_Robot?start=muhammedrk-mo-tech-group-{file_id}')])

                    except:
                        btn.append([InlineKeyboardButton(f"{filesize}", url=f"https://playdisk.xyz/st?api=75c2abea01f77494fa5660a362e711bb2348fffb&url=https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}")])
                        btn.append([InlineKeyboardButton(f"{filename}", url=f"https://playdisk.xyz/st?api=75c2abea01f77494fa5660a362e711bb2348fffb&url=https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}")])
        else:
            return

        if not btn:
            return

        if len(btn) > temp.filterBtns: 
            btns = list(split_list(btn, temp.filterBtns)) 
            keyword = f"{update.chat.id}-{update.id}"
            temp.BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append([InlineKeyboardButton("Pages 1/1",callback_data="pages"),
                            InlineKeyboardButton("Close 🗑️", callback_data="close")])

            buttons.append([InlineKeyboardButton("🎬 𝗛𝗢𝗪 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 🎬", url=f"https://t.me/Tamil_Roars/16")])

            buttons.append([InlineKeyboardButton("💯 𝗨𝗡𝗔𝗕𝗟𝗘 𝗧𝗢 𝗔𝗖𝗖𝗘𝗦 𝗦𝗢𝗟𝗩𝗘𝗗 💯", url=f"https://droplink.co/TamilRoarsFiles")])

            if settings["photo"]:
                await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
            else:
                await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)        
            return

        data = temp.BUTTONS[keyword]
        buttons = data['buttons'][0].copy()
   
        buttons.append([InlineKeyboardButton(f"⌸ 1/{data['total']}",callback_data="pages"),
                        InlineKeyboardButton("🗑️", callback_data="close"),
                        InlineKeyboardButton("⋙",callback_data=f"nextgroup_0_{keyword}")])

        buttons.append([InlineKeyboardButton("🎬 𝗛𝗢𝗪 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 🎬", url=f"https://t.me/Tamil_Roars/16")])

        buttons.append([InlineKeyboardButton("💯 𝗨𝗡𝗔𝗕𝗟𝗘 𝗧𝗢 𝗔𝗖𝗖𝗘𝗦 𝗦𝗢𝗟𝗩𝗘𝗗 💯", url=f"https://droplink.co/TamilRoarsFiles")])

        try:             
            if settings["photo"]:
                try:
                    await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                except Exception as error:
                    await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT, reply_to_message_id=update.id)
                    await client.send_photo(chat_id=update.chat.id, photo="https://telegra.ph/file/2602c9d464dc2b1a53e0f.jpg", caprion=f"‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
                    await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
            else:
                try:
                    await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                except Exception as error:
                    await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT, reply_to_message_id=update.id)
                    await client.send_message(chat_id=update.chat.id, text=f"‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
                    await client.send_message(chat_id=update.chat.id, text=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
        except Exception as error:
            await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT, reply_to_message_id=update.id)
            await client.send_photo(chat_id=update.chat.id, photo="https://telegra.ph/file/2602c9d464dc2b1a53e0f.jpg", caprion=f"""‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**""", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
            await client.send_message(chat_id=update.chat.id, text=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name=f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)


@Client.on_message(filters.private & filters.command('pmautofilter'))
async def pmautofilter(client, message):        
    try:
        cmd=message.command[1] 
        if cmd == "on":   
            if message.chat.id in temp.PMAF_OFF:
                temp.PMAF_OFF.remove(message.chat.id)
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙽..!")  
            else:
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙽..!")                           
        elif cmd == "off": 
            if message.chat.id in temp.PMAF_OFF:
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙵𝙵..!")                                             
            else:
                temp.PMAF_OFF.append(message.chat.id)
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙵𝙵..!")
        else:
            await message.reply_text("𝚄𝚂𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝙵𝙾𝚁𝙼𝙰𝚃.!\n\n • /pmautofilter on\n • /pmautofilter off")    
    except:
        pass

