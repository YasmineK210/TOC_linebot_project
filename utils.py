import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

id = "U9a40632f656b43a4e638fa0c29f8e334"

def send_text_message_push(text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TextSendMessage(text=text))
    return "OK"

def send_text_message_reply(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_line_sticker(package, sticker):
    line_bot_api = LineBotApi(channel_access_token)
    sticker_msg = StickerSendMessage(
        package_id = package,
        sticker_id = sticker
    )
    line_bot_api.push_message(id, sticker_msg)

    return "OK"

def send_quick_reply_five(textA, textB, textC, textD, textE):
    line_bot_api = LineBotApi(channel_access_token)
    flex_message = TextSendMessage(text="Select a reply: ",
        quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(label=textA, text=textA)),
            QuickReplyButton(action=MessageAction(label=textB, text=textB)),
            QuickReplyButton(action=MessageAction(label=textC, text=textC)),
            QuickReplyButton(action=MessageAction(label=textD, text=textD)),
            QuickReplyButton(action=MessageAction(label=textE, text=textE))      
            ])
    )

    line_bot_api.push_message(id, flex_message)
    return "OK"

def send_quick_reply_two(textA, textB):
    line_bot_api = LineBotApi(channel_access_token)
    flex_message = TextSendMessage(text="Select a reply: ",
        quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(label=textA, text=textA)),
            QuickReplyButton(action=MessageAction(label=textB, text=textB)),
        ])
    )
    line_bot_api.push_message(id, flex_message)
    return "OK"

