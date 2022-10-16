import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

ch = '@Freentrn'
@bot.message_handler(commands=['start'])
def start(message):
 idd = message.from_user.id
 url = f"https://api.telegram.org/bot{BOT_TOKEN}/getchatmember?chat_id={ch}&user_id={idd}"
 req = requests.get(url)
 if 5384214726 == int(idd):
 	bot.reply_to(message,text='''*أهلا بك عزيزي ألادمن ألاوامر️*''',parse_mode='MarkDown')
 	checkmember='Admin'
 if 'member' in req.text:
 	checkmember='Member'
 	bot.reply_to(message,text='''*اهلا بك في بوت فحص البين الاول في التلكرام💵
💀 وظيفه البوت اعطاء معلومات على البن 
💀 المعلومات تشمل نوع البطاقه و قوتها و دولتها و هواي اشياء مفيده 💵
⚠️ كل العليك هو ارسال البن و رح يعطيك معلوماته او ارسال فيزا كامله رح يستخرجلك البن و يعطيك معلومات كامله عليه ⚠️*''',parse_mode='MarkDown')
 if 'left' in req.text:
 	checkmember='notmember'
 	key = types.InlineKeyboardMarkup()
 	b2=types.InlineKeyboardButton(text='أشترك ألان ✅', url='https://t.me/Freentrn')
 	key.row_width = 1
 	key.add(b2)
 	bot.reply_to(message,text=f'''*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- {ch}

‼️| اشترك ثم ارسل /start️*''',parse_mode='MarkDown',reply_markup=key)
@bot.message_handler(func= lambda m: True)
def mess(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='Chaneel', url='https://t.me/Freentrn')
	key.row_width = 1
	key.add(back)
	bin = message.text
	try:
		gbin = bin
		x1=gbin[0]
		x2=gbin[1]
		x3=gbin[2]
		x4=gbin[3]
		x5=gbin[4]
		x6=gbin[5]
		bin=x1+x2+x3+x4+x5+x6
	except:pass
	try:
		gbin = bin.split('|')[0]
		x1=gbin[0]
		x2=gbin[1]
		x3=gbin[2]
		x4=gbin[3]
		x5=gbin[4]
		x6=gbin[5]
		bin=x1+x2+x3+x4+x5+x6
	except:
		pass
	re=requests.get('https://lookup.binlist.net/'+bin).json()
	scheme=re['scheme']
	type = re['type']
	brand=re['brand']
	prepaid=re['prepaid']
	country=re['country']['name']
	emoji=re['country']['emoji']
	bank=re['bank']['name']
	currency=re['country']['currency']
	bot.reply_to(message,text=f"""<strong>﻿
𝒃𝒊𝒏 → <code>{bin}</code>	
	
𝒔𝒄𝒉𝒆𝒎𝒆 → {scheme}

𝒕𝒚𝒑𝒆  →  {type}

𝒑𝒓𝒆𝒑𝒂𝒊𝒅  → {prepaid}

𝒄𝒐𝒖𝒏𝒕𝒓𝒚 → {country} {emoji} {currency}

𝒃𝒂𝒏𝒌 𝒏𝒂𝒎𝒆 → {bank}
  </strong>""",parse_mode="html",reply_markup=key)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://tggbotp.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
