import telegram, logging
import os

token = os.environ['MI_TOKEN_TELEGRAM']


from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

#bot = telegram.Bot(token='5565011914:AAGQIwbTN0mw6eZilq49sL97gBEsfgENqwk')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# Metodos
# Mensaje cuando inicio el bot desde telegram
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hola! \nSoy Keypra, te dare informacion sobre descuentos de teclados de Keychron.com \n"
                                  "Solo escribe /info para empezar")


def info(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="https://www.keychron.com/products/keychron-k2-hot-swappable-wireless-mechanical-keyboard")

def receptor_de_msj(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="La respuesta a mensajes normales esta en WIP\n"
                                                                    "Por ahora solo puedo responder comandos")


# Para recibir los mensajes, updater
updater = Updater(token=token, use_context=True)


# Despachador, puede recibir comandos el bot
dispatcher = updater.dispatcher

# start_handler = CommandHandler('start', start)

# Comandos
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('info', info))
dispatcher.add_handler(MessageHandler(Filters.text &(~Filters.command),receptor_de_msj))

updater.start_polling()
print('El bot se esta ejecutando')

updater.idle()
# bot.send_message(text='Esto es un mensaje!', chat_id=1900844579)
