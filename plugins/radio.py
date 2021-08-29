
from pyrogram import Client, filters
from pyrogram.types import Message
from utils import mp, RADIO, USERNAME
from config import Config
from config import STREAM
CHAT=Config.CHAT
ADMINS=Config.ADMINS

@Client.on_message(filters.command(["radio", f"radio@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT) | filters.private))
async def radio(client, message: Message):
    if 1 in RADIO:
        k=await message.reply_text("Por favor, detenga la transmisión de radio existente / stopradio")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.start_radio()
    k=await message.reply_text(f"Iniciar Radio: <code>{STREAM}</code>")
    await mp.delete(k)
    await mp.delete(message)

@Client.on_message(filters.command(['stopradio', f"stopradio@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT) | filters.private))
async def stop(_, message: Message):
    if 0 in RADIO:
        k=await message.reply_text("Por favor, inicie Radio / radio")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.stop_radio()
    k=await message.reply_text("Finalizó la transmisión de radio.")
    await mp.delete(k)
    await mp.delete(message)
