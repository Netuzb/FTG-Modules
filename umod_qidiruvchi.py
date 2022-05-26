# ▀█▀ █▀▀ █▀▄▀█ █░█ █▀█
# ░█░ ██▄ █░▀░█ █▄█ █▀▄
# ═══════════════════════
# █▀▀ █▀█ █▄▀ █ █▄░█ █▀█ █░█
# ██▄ █▀▄ █░█ █ █░▀█ █▄█ ▀▄▀
# ═════════════════════════════
# meta developer: @netuzb
# meta channel: @umodules

__version__ = (4, 3, 28)

from .. import loader, utils 
def register(cb):
	cb(QidiruvMod()) 
	
umod = " <b>#umoduz</b>"
umod_paren = "<b>[</b>"
umod_paren_end = "<b>]</b> "
	
class QidiruvMod(loader.Module):
	"""Kontent qidirish moduli""" 
	strings = {
               "name": "Qidiruvchi", 
               "umodules": umod_paren + "<b>Qidiruv</b>",
               "easyapk": umod_paren + "<b>EasyApk</b>",
               "ftgchatuz": umod_paren + "<b>Qidiruv</b>",
               "tgraphuz": umod_paren + "<b>TGraphUz #kanali</b>",
               "yoq": "Buyruqdan keyin soʻz yozing deb qoʻyibman!?",
               "topilmadi": "Hechnima topilmadi! Buyruqdan keyin faqat bitta soʻz yozishga urinib koʻring!"
               }
               
	async def tgraphcmd(self, message):
		"""qidirish uchun soʻz yoki raqam"""
		try:
			title = utils.get_args_raw(message)
			if not title:
				await message.reply(self.strings("tgraphuz", message) + umod_paren_end + self.strings("yoq", message))
			else:
				umods = message.input_chat
				await [i async for i in message.client.iter_messages("tgraphuz", search=title)][0].forward_to(umods)
				await message.delete()
		except:
			await message.reply(self.strings("tgraphuz", message) + umod_paren_end + self.strings("topilmadi", message))
	async def umodcmd(self, message):
		"""qidirish uchun modul nomi yoki buyrugʻi"""
		try:
			title = utils.get_args_raw(message)
			if not title:
				await message.reply(self.strings("umodules", message) + umod + umod_paren_end + self.strings("yoq", message))
			else:
				umods = message.input_chat
				await [i async for i in message.client.iter_messages("umodules", search=title)][0].forward_to(umods)
				await message.delete()
		except:
			await message.reply(self.strings("umodules", message) + umod + umod_paren_end + self.strings("topilmadi", message))
	async def umodgrcmd(self, message):
		"""qidirish uchun soʻz (kirilchada faqat)"""
		try:
			title = utils.get_args_raw(message)
			if not title:
				await message.reply(self.strings("ftgchatuz", message) + umod + umod_paren_end + self.strings("yoq", message))
			else:
				umods = message.input_chat
				await [i async for i in message.client.iter_messages("ftgchatuz", search=title)][0].forward_to(umods)
				await message.delete()
		except:
			await message.reply(self.strings("ftgchatuz", message) + umod + umod_paren_end + self.strings("topilmadi", message))
	async def apkcmd(self, message):
		"""dastur yoki oʻyin nomi"""
		try:
			title = utils.get_args_raw(message)
			if not title:
				await message.reply(self.strings("easyapk", message) + umod + umod_paren_end + self.strings("yoq", message))
			else:
				umods = message.input_chat
				await [i async for i in message.client.iter_messages("easyapk", search=title)][0].forward_to(umods)
				await message.delete()
		except:
			await message.reply(self.strings("easyapk", message) + umod + umod_paren_end + self.strings("topilmadi", message))

			
