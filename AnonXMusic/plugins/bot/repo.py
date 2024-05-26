from pyrogram import filters
from AnonXMusic import app

@app.on_message(filters.command("repo"))
async def start(_, msg):
    await msg.reply_video(
        video="https://telegra.ph/file/c45acbf0c5107a79952c7.mp4"
    )
