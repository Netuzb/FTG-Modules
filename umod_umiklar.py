from .. import loader, utils 
 
@loader.tds 
class FiltersMod(loader.Module): 
    """Umiklar""" 
    strings = {"name": "Umiklar"} 
 
    async def client_ready(self, client, db): 
        self.db = db 
 
    async def umaddcmd(self, message): 
        """Roʻyxatga filtr qoʻshing.""" 
        filters = self.db.get("Filters", "filters", {}) 
        key = utils.get_args_raw(message) # .lower() 
        reply = await message.get_reply_message()  
        chatid = str(message.chat_id) 
 
        if not key and not reply: 
            return await message.reply("<b>Munozaralar va takrorlashlar yo'q.</b>") 
 
        if chatid not in filters: 
            filters.setdefault(chatid, {}) 
 
        if key in filters[chatid]: 
            return await message.reply("<b>Bu filtr allaqachon mavjud..</b>") 
 
        if reply: 
            if key: 
                msgid = await self.db.store_asset(reply) 
            else: 
                return await message.reply("<b>Filtrni saqlash uchun argumentlar kerak!</b>") 
        else: 
            try: 
                msgid = (await message.client.send_message(f'friendly-{(await message.client.get_me()).id}-assets', key.split(' / ')[1])).id 
                key = key.split(' / ')[0] 
            except IndexError: 
                return await message.reply("<b>🥷 Umiklash uchun reply ishlating.</b>") 
 
        filters[chatid].setdefault(key, msgid) 
        self.db.set("Filters", "filters", filters) 
        await message.reply(f"🥷 <b>\"{key}\" filtri saqlandi!</b>")  
 
 
    async def umdelcmd(self, message): 
        """Umik roʻyxatdan olib tashlaydi.""" 
        filters = self.db.get("Filters", "filters", {}) 
        args = utils.get_args_raw(message) 
        chatid = str(message.chat_id) 
 
        if chatid not in filters: 
            return await message.reply("<b>Bu chatda umik yo‘q.</b>") 
 
        if not args: 
            return await message.reply("<b>Hech qanday dalil yo'q.</b>") 
 
        if args: 
            try: 
                filters[chatid].pop(args) 
                self.db.set("Filters", "filters", filters) 
                await message.reply(f"<b>🥷 \"{args}\" umigi chatdan olib tashlandi!</b>") 
            except KeyError: 
                return await message.reply(f"<b>\"{args}\" filtri yo'q.</b>") 
        else: 
            return await message.reply("<b>Hech qanday dalil yo'q.</b>") 
 
 
    async def umdelallcmd(self, message): 
        """Chat ro'yxatidan barcha umiklarni olib tashlaydi.""" 
        filters = self.db.get("Filters", "filters", {}) 
        chatid = str(message.chat_id) 
  
        if chatid not in filters: 
            return await message.reply("<b>Bu chatda umik yo‘q.</b>") 
 
        filters.pop(chatid) 
        self.db.set("Filters", "filters", filters) 
        await message.reply("<b>Barcha umiklar chat roʻyxatidan olib tashlandi!</b>") 
 
 
    async def umiklarcmd(self, message): 
        """Suhbat umiklar roʻyxatini koʻrsatadi.""" 
        filters = self.db.get("Filters", "filters", {}) 
        chatid = str(message.chat_id) 
 
        if chatid not in filters: 
            return await message.reply("<b>Bu chatda umik yo‘q.</b>") 
 
        msg = "" 
        for _ in filters[chatid]: 
            msg += f"ㅤ{_}\n" 
        await message.reply(f"<b>🥷 umiklar roʻyxati:</b> {len(filters[chatid])}\n\nby <a href='tg://openmessage?user_id=605778538'>👾temur</a>\n<code>{msg}</code>")  
 
 
    async def watcher(self, message): 
        try: 
            filters = self.db.get("Filters", "filters", {}) 
            chatid = str(message.chat_id) 
            m = message.text.lower() 
            if chatid not in filters: return 
 
            for _ in filters[chatid]: 
                msg = await self.db.fetch_asset(filters[chatid][_]) 
                def_pref = self.db.get("friendly-telegram.main", "command_prefix") 
                pref = '.' if not def_pref else def_pref[0] 
 
                if len(_.split()) == 1: 
                    if _.lower() in m.split(): 
                        await self.exec_comm(msg, message, pref) 
                else: 
                    if _.lower() in m: 
                        await self.exec_comm(msg, message, pref) 
        except: pass
 
    async def exec_comm(self, msg, message, pref): 
        try: 
            if msg.text[0] == pref: 
                smsg = msg.text.split() 
                return await self.allmodules.commands[smsg[0][1:]](await message.reply(smsg[0] +  ' '.join(_ for _ in smsg if len(smsg) > 1))) 
            else: pass 
        except: pass 
        await message.reply(msg)
