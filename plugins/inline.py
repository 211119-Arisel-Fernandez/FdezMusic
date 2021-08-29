
from pyrogram.handlers import InlineQueryHandler
from youtubesearchpython import VideosSearch
from utils import USERNAME
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, errors
from config import Config
REPLY_MESSAGE=Config.REPLY_MESSAGE
buttons = [
    [
        InlineKeyboardButton('🏃 Deploy to Heroku 🏃', url='https://heroku.com/deploy?template=https://github.com/LushaiMusic/VCMusicPlayer'),
    ],
    [
        InlineKeyboardButton('👨‍🎤 Play Music', url=f'https://t.me/{USERNAME}'),
        InlineKeyboardButton('Codigo fuente 🤓', url='https://github.com/211119-Arisel-Fernandez/FdezMusic.git'),
    ],
    [
        InlineKeyboardButton('🆘 Help & Commands 🆘', callback_data='help')       
    ]
    ]
@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "ORU_MANDAN_PM_VANNU":
        answers.append(
            InlineQueryResultArticle(
                title="Deploy",
                input_message_content=InputTextMessageContent(f"{REPLY_MESSAGE}\n\n<b>No puedes usar este bot en tu grupo, para eso tienes que hacer tu propio bot desde el [SOURCE CODE](https://github.com/211119-Arisel-Fernandez/FdezMusic.git) below.</b>", disable_web_page_preview=True),
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text=("Buscar videos de YouTube"),
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=50)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "/play https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("Nada Encontrado"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
