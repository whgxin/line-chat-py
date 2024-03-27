from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['aavP/1mJJ0u7P88eP5ZeT2q9a4G8LLTmgXIXzDDrtVFgEWwH08EZ7mo096FJhbSa1TX2FTcfC/2tZTnUQ9hY9E5ndlEiDaobPcwzG5f7Gn7Y1/i50AXbT3VZ/NuTOCKWHIsddVkkGZSwAaXeN0//fwdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['15cf9a5c6bc1ed3faaaafa12af25d464'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)