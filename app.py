import asyncio
from flask import Flask, render_template, request
from telegram import Bot

app = Flask(__name__, template_folder='.')

# Replace these values with your actual bot token and chat ID
TELEGRAM_BOT_TOKEN = '6691298966:AAG4XGVf2aPw47HBUxTLUSmxjPgLJPBkM7U'
TELEGRAM_CHAT_ID = '-4188089568'


@app.route('/')
def index():
    return render_template('index.html')


async def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)


@app.route('/register', methods=['POST'])
def register():
    # Get form data
    name = request.form['name']
    location = request.form['location']
    mobile = request.form['mobile']
    blood_group = request.form['blood_group']

    # Send data to Telegram group
    message = f'New user registered:\nName: {name}\nLocation: {location}\nMobile: {mobile}\nBlood Group: {blood_group}'

    # Run send_telegram_message coroutine asynchronously
    asyncio.run(send_telegram_message(message))

    return 'User registered successfully!'


if __name__ == '__main__':
    app.run(debug=True)
