import secret as ass
import os
from PIL import Image, ImageEnhance, ImageFilter
import telebot, uuid
import pytesseract

bot = telebot.TeleBot(ass.API_key)
BASE_DIR = os.getcwd()


def process_image(img_path):
    custom_config = r'--psm 6'
    pytesseract.pytesseract.tesseract_cmd = BASE_DIR + r"\tes\tesseract"
    img = Image.open(img_path)
    # img = img.filter(ImageFilter.MedianFilter())
    # enhancer = ImageEnhance.Contrast(img)
    # img = enhancer.enhance(2)
    # img = img.convert('1')
    text = pytesseract.image_to_string(img, config=custom_config)
    return text

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 'Слыш, ты! Я к тебе обращаюсь! Ты мне даешь фотографию с текстом, а я тебе кидаю, шо там написано, если там не написано не на ангельском, то ты не человек.')

@bot.message_handler(content_types=["photo"])
def save(message):
    try:
        # How the fucking work telegramm image? Do we realy need to download the file on computer?
        # Downloading a file
        file_id = message.photo[-1].file_id
        path = bot.get_file(file_id)
        downloaded_file = bot.download_file(path.file_path)

        # Getting file extension
        extn = '.' + str(path.file_path).split('.')[-1]
        cname = str(uuid.uuid4()) + extn

        # Creating a file and writing there downloaded image
        with open(cname, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        text = process_image(cname)

        os.remove(cname)

        bot.reply_to(message, text)
    except:
        bot.reply_to(message, 'Ай, мля! Я еррорку поймал!')

bot.polling()