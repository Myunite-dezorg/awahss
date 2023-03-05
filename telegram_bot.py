

# Initialize Django app

import os
import django
django.setup()

from django.conf import settings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater
from django.core.wsgi import get_wsgi_application
from django.shortcuts import get_object_or_404
from apps.notes.models import Note
from telegram.ext import Updater

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()
# Telegram bot token
TOKEN = '5696672871:AAETCwCFO18bHSmpEDBMcmlY2Z5CORLUHlk'

# Define conversation states
SELECT_ACTION, ADD_NOTE_TITLE, ADD_NOTE_TEXT, SEARCH_NOTES_QUERY, DELETE_NOTE_ID = range(5)

# Define command handlers
def start(update, context):
    keyboard = [[InlineKeyboardButton("Add Note", callback_data='add_note'),
                 InlineKeyboardButton("Search Notes", callback_data='search_notes')],
                [InlineKeyboardButton("Delete Note", callback_data='delete_note')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to the Notes Bot! Please select an action:",
                             reply_markup=reply_markup)
    return SELECT_ACTION

def help(update, context):
    text = '''
Available commands:
/add_note <title> <text> - add a new note
/search_notes <query> - search notes by title or text
/delete_note <id> - delete a note by ID
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def add_note_title(update, context):
    context.user_data['title'] = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please enter the note text:")
    return ADD_NOTE_TEXT

def add_note_text(update, context):
    title = context.user_data['title']
    text = update.message.text
    note = Note.objects.create(title=title, text=text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Note '{title}' added with ID {note.id}")
    return ConversationHandler.END

def search_notes_query(update, context):
    query = update.message.text
    notes = Note.objects.filter(title__icontains=query) | Note.objects.filter(text__icontains=query)
    if notes:
        text = 'Search results:\n' + '\n'.join([f'{note.title} (ID {note.id})' for note in notes])
    else:
        text = 'No notes found.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    return ConversationHandler.END

def delete_note_id(update, context):
    note_id = int(update.message.text)
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Note '{note.title}' (ID {note.id}) deleted.")
    return ConversationHandler.END

# Define callback handlers
def select_action(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [[InlineKeyboardButton("Add Note", callback_data='add_note'),
                 InlineKeyboardButton("Search Notes", callback_data='search_notes')],
                [InlineKeyboardButton("Delete Note", callback_data='delete_note')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Please select an action:", reply_markup=reply_markup)
    return SELECT_ACTION

def add_note_callback(update, context):
    query = update.callback_query
    query.answer()
    context.user_data['title'] = None
    query.edit_message_text(text="Please enter the note title:")
    return ADD_NOTE_TITLE

def search_notes_callback(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please enter the search query:")
    return SEARCH_NOTES_QUERY

def delete_note_callback(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please enter the note ID to delete:")
    return DELETE_NOTE_ID

# Define conversation handler
# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler('start', start)],
#     states={
#         SELECT_ACTION: [CallbackQueryHandler(select_action,
#                                               pattern='^' + 'add_note' + '$|^' + 'search_notes' + '$|^' + 'delete_note' + '$')],
#         ADD_NOTE_TITLE: [MessageHandler(filters.Text & ~filters.Command, add_note_title)],
#         ADD_NOTE_TEXT: [MessageHandler(filters.text & ~filters.command, add_note_text)],
#         SEARCH_NOTES_QUERY: [MessageHandler(filters.text & ~filters.command, search_notes_query)],
#         DELETE_NOTE_ID: [MessageHandler(filters.text & ~filters.command, delete_note_id)],
#     },
#     fallbacks=[CommandHandler('help', help)]
# )

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        SELECT_ACTION: [CallbackQueryHandler(select_action)],
        ADD_NOTE_TITLE: [MessageHandler(Filters.text, add_note_title)],
        ADD_NOTE_TEXT: [MessageHandler(Filters.text, add_note_text)],
        SEARCH_NOTES_QUERY: [MessageHandler(Filters.text, search_notes_query)],
        DELETE_NOTE_ID: [MessageHandler(Filters.text, delete_note_id)],
    },
    fallbacks=[CommandHandler('help', help)]
)

# Define main function
def main():
    updater = Updater('5696672871:AAETCwCFO18bHSmpEDBMcmlY2Z5CORLUHlk', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(add_note_callback, pattern='^' + 'add_note' + '$'))
    dp.add_handler(CallbackQueryHandler(search_notes_callback, pattern='^' + 'search_notes' + '$'))
    dp.add_handler(CallbackQueryHandler(delete_note_callback, pattern='^' + 'delete_note' + '$'))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
