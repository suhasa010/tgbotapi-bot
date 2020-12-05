from telegram.ext import Updater
import os
from dotenv import load_dotenv
load_dotenv()

BOT_API = os.getenv("BOT_API")
updater = Updater(token=BOT_API, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I am here to help you browse the documentation of Telegram Bot API right here on Telegram using Instant View.")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#def echo(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

#from telegram.ext import MessageHandler, Filters
#echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#dispatcher.add_handler(echo_handler)

# def caps(update, context):
#     # if context.args == null:
#     #     context.bot.send_message(chat_id=update.effective_chat.id, text="send some text, you fool!")
#     print("arguments are" + context.args)
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)

from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    results = list()
    results.append(
    InlineQueryResultArticle(
            id=uuid4(),
            title='Telegram Bot API Documentation',
            input_message_content=InputTextMessageContent("https://core.telegram.org/bots/api/?v=1", disable_web_page_preview=False),
            description='Telegram Bot API Main page',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )
    #context.bot.answer_inline_query(update.inline_query.id, results)
    #results = list()

    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Announcements ➜ Recent Changes',
            input_message_content=InputTextMessageContent("""Recent Changes\nhttps://core.telegram.org/bots/api/?v=1#recent-changes""", parse_mode='HTML'),
            description='Telegram Bot API Announcements',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Making Requests',
            input_message_content=InputTextMessageContent("""Making Requests\nhttps://core.telegram.org/bots/api/?v=1#making-requests""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Using a Local Bot API Server',
            input_message_content=InputTextMessageContent("""Using a Local Bot API Server\nhttps://core.telegram.org/bots/api/?v=1#using-a-local-bot-api-server""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Getting Updates',
            input_message_content=InputTextMessageContent("""Getting Updates\nhttps://core.telegram.org/bots/api/?v=1#getting-updates""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Available Types',
            input_message_content=InputTextMessageContent("""Available Types\nhttps://core.telegram.org/bots/api/?v=1#available-types""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )    
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Available Methods',
            input_message_content=InputTextMessageContent("""Available Methods\nhttps://core.telegram.org/bots/api/?v=1#available-methods""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )  
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Updating Messages',
            input_message_content=InputTextMessageContent("""Updating Messages\nhttps://core.telegram.org/bots/api/?v=1#updating-messages""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )  
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Stickers',
            input_message_content=InputTextMessageContent("""Stickers\nhttps://core.telegram.org/bots/api/?v=1#stickers""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )  
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Inline Mode',
            input_message_content=InputTextMessageContent("""Inline Mode\nhttps://core.telegram.org/bots/api/?v=1#inline-mode""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )  
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Payments',
            input_message_content=InputTextMessageContent("""Payments\nhttps://core.telegram.org/bots/api/?v=1#payments""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Telegram Passport',
            input_message_content=InputTextMessageContent("""Telegram Passport\nhttps://core.telegram.org/bots/api/?v=1#telegram-passport""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )  
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title='Games',
            input_message_content=InputTextMessageContent("""Games\nhttps://core.telegram.org/bots/api/?v=1#games""", parse_mode='HTML'),
            description='Telegram Bot API Documentation',
            thumb_url='https://play-lh.googleusercontent.com/ZU9cSsyIJZo6Oy7HTHiEPwZg0m2Crep-d5ZrfajqtsH-qgUXSqKpNA2FpPDTn-7qA5Q=s180',
            thumb_width=30,
            thumb_height=30
        )
    )  
    if query.lower() == 'format':
            results = list()
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='Request Format',
            input_message_content=InputTextMessageContent("""<code>#request
Book's name
Author's name 
#ebook or #audiobook
[Amazon link to audiobook/KU book, if applicable]</code>""", parse_mode='HTML'),
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


updater.start_polling()