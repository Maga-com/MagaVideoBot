import requests
from telegram.ext import Updater, MessageHandler, Filters

# BotFather-dən aldığın tokeni bura yaz
TOKEN = "7905277975:AAG4VZg4oiEtsuNbshhw5DzxoEAruHv2L38"

def download_tiktok(update, context):
    url = update.message.text.strip()
    if "tiktok.com" not in url:
        update.message.reply_text("❌ Zəhmət olmasa düzgün TikTok linki göndər.")
        return

    api = f"https://api.tikwm.com/video/info?url={url}"
    try:
        r = requests.get(api).json()
        if "data" in r and "play" in r["data"]:
            video_url = r["data"]["play"]  # logosuz video linki
            update.message.reply_video(video_url, caption="✅ Buyur, logosuz video")
        else:
            update.message.reply_text("❌ Videonu yükləyə bilmədim.")
    except Exception as e:
        update.message.reply_text("⚠️ Xəta baş verdi, yenidən yoxla.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_tiktok))
    updater.start_polling()
    updater.idle()

if _name_ == "_main_":
    main()
