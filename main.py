
from pyrogram import Client, idle
import os
from config import Config
from utils import mp
from pyrogram.raw import functions, types

CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()

bot.run(main())
bot.start()
bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Verifica si el bot está Online"
            ),
            types.BotCommand(
                command="help",
                description="Muestra mensaje de ayuda"
            ),
            types.BotCommand(
                command="play",
                description="Reproducir la canción de youtube / audiofile"
            ),
            types.BotCommand(
                command="dplay",
                description="No Funciona esta en proceso"
            ),
            types.BotCommand(
                command="player",
                description="Muestra la canción que se está reproduciendo actualmente con controles"
            ),
            types.BotCommand(
                command="playlist",
                description="Muestra la lista de reproducción"
            ),
            types.BotCommand(
                command="skip",
                description="Omitir la canción actual"
            ),
            types.BotCommand(
                command="join",
                description="Únir bot al ChatV"
            ),
            types.BotCommand(
                command="leave",
                description="Expulsar bot del ChatV"
            ),
            types.BotCommand(
                command="vc",
                description="Comprobar si el bot está unido al ChatV"
            ),
            types.BotCommand(
                command="stop",
                description="Detener Bot"
            ),
            types.BotCommand(
                command="radio",
                description="Iniciar radio XD"
            ),
            types.BotCommand(
                command="stopradio",
                description="Detener radio XD"
            ),
            types.BotCommand(
                command="replay",
                description="Repetir desde el principio"
            ),
            types.BotCommand(
                command="clean",
                description="Limpia archivos RAW"
            ),
            types.BotCommand(
                command="pause",
                description="Pausa la canción"
            ),
            types.BotCommand(
                command="resume",
                description="Reanudar la canción pausada"
            ),
            types.BotCommand(
                command="mute",
                description="Mutear el ChatV (BETA)"
            ),
            types.BotCommand(
                command="volume",
                description="Establecer volumen entre 0-200 (BETA)"
            ),
            types.BotCommand(
                command="unmute",
                description="Desmutear el ChatV"
            ),
            types.BotCommand(
                command="restart",
                description="Reinicia el bot"
            )
        ]
    )
)

idle()
bot.stop()
