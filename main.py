from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tiktok import TikTokApi

# TG token fron Bot father
TOKEN = 'TOKETN4'
api = TikTokApi()

def start(update, context):
    update.message.reply_text('Hi send me url ')

def download_tiktok_video(update, context):
    url = update.message.text
    try:
        video = api.get_video_by_url(url)
        if video:
            update.message.reply_video(video['url'])
        else:
            update.message.reply_text('video could not be found')
    except Exception as e:
        print(str(e))
        update.message.reply_text('An error occurred while uploading the video.')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_tiktok_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
