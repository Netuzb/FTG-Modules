#    ████░████░███░███░██░██░████░
#    ░██░░██░░░██░█░██░██░██░███░░
#    ░██░░████░██░░░██░█████░█████
#    ═════════════════════════════════════════
#    ████░████░░██░██░██░███░░██░█████░██░░░██
#    ██░░░███░░░████░░██░██░█░██░██░██░░██░██░
#    ████░█████░██░██░██░██░░███░█████░░░███░░
#    ═════════════════════════════════════════
#    Litsenziya: https://t.me/UModules/112
#    Taqdim qilingan manzil: https://telegram.me/umodules

__version__ = (1, 2, 0)

# meta developer: @netuzb
# meta channel: @umodules

from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 

@loader.tds
class SpotifyDownloaderMod(loader.Module):
    """Musiqa izlash moduli"""
    strings = {
        "name": "Musiqachi",
        "yoq": "<b>🥷 Qidirilmoqda...\n├╴╴╴╴╴╴╴╴╴╴\n└ 👾 Hechnima topilmadi!</b>",
        "qidiryapman": "<b>🥷 Qidirilmoqda...</b>",
        "eshe": "<b>🥷 Qidirilmoqda...\n├╴╴╴╴╴╴╴╴╴╴\n└ 👾 Qayta urunib koʻring!</b>",
        "spisok": "<b>🥷 Musiqalar roʻyhati bazasi</b> @mephbot!</b>",
        "topmadim": "<b>🥷 Qidirilmoqda...\n├╴╴╴╴╴╴╴╴╴╴\n└ 👾 Musiqa topilmadi. Balkim nomini xato yozgandursiz?</b>"}
    
    async def client_ready(self, client, db):
        self.client = client
        self._db = db
        self._me = await client.get_me()
        
    @loader.unrestricted
    async def vkcmd(self, message):
        """musiqa nomi"""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit(self.strings("yoq", message))

        message = await message.edit(self.strings("qidiryapman", message))
        try:
            message = message[0]
        except: pass
        music = await self.client.inline_query('spotifysavebot', args)
        for mus in music:
            if mus.result.type == 'audio':
                await self.client.send_file(message.peer_id, mus.result.document, reply_to=message.reply_to_msg_id)
                return await message.delete()

        return await message.edit(self.strings("topmadim", message))

    async def spotycmd(self, message): 
        """musiqa yoki albom nomi""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit(self.strings("yoq", message))
        try: 
            await message.edit(self.strings("qidiryapman", message))
            music = await message.client.inline_query('lybot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, caption="<b>🥷 Musiqa topildi!</b>", reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>🥷 Qidirilmoqda...\n├╴╴╴╴╴╴╴╴╴╴\n└ 👾 {args} - Spotify'da topilmadi! Balkim <code>vk</code> orqali izlab ko'rarsiz?</b>")

    async def nomcmd(self, message): 
        """musiqa yoki esda bor albom nomi""" 
        try:
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@mephbot" 
            if not text and not reply: 
                await message.edit(self.strings("spisok", message))
                return 
            if text: 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=707444265)) 
                        await message.client.send_message(chat, text) and await message.delete()
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply(self.strings("udali", message))
                        return 
                    if not response.text: 
                        await message.edit(self.strings("eshe", message))
                        return
                    await self.client.send_message(message.to_id, response.text) 
                    await self.client.delete_dialog(chat)
        except TimeoutError: 
            return await message.edit(self.strings("oshibka", message))
