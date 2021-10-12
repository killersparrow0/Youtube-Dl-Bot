from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group", url="https://t.me/movies_songs_tj")],
        [InlineKeyboardButton("Report Bugs 😊", url="https://t.me/joinchat/vcOhk8tX214zNGQ1")]
        [InlinekeyboardButton("Donate 💰", url="https://paypal.me/AbdulMilas")]
    ])
        
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nI am a youtube video downloader bot send me youtube video url 🔗 only,for More info 👉🏻/help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

