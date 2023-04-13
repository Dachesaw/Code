import openai
import telebot

bot = telebot.TeleBot('token')
openai.api_key = ('token')

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    responce = openai.Completion.create(
    model='text-davinci-003',
    prompt=message.text,
    temperature=0.3,
    max_tokens=2048,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    )    
    bot.send_message(chat_id=message.from_user.id, text=responce['choices'][0]['text'])
    print(f'\nCooбщение пользователя: {message.text}')
    print(responce['choices'][0]['text'])
bot.polling()
