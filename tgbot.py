import tgflow as tgf
import pymysql.cursors
from tgflow import TgFlow as tgf_obj
from tgflow import handles as h
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from enum import Enum
#import main
import apiai, json
import sql
import requests
key='578778366:AAEvv14tDPTWt_d-7NEmBQgQpPTeESZ3Kak'

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='cxzaq15061999',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             init_command='SET NAMES UTF8')

class States(Enum):
    START=1
    INFO=2
    LOGIN=3
    PASS=4
    LOGGED=5
    CO=6
    LK=8
    FAQ=7
    BRIG=9
    PROBLEMS=10

def geo(i,d):
    print(i.location)
    a = i.location
    bi = str(a).split(",")[0].split(": ")[1]
    bi2 = str(a).split(",")[1].split(": ")[1].split("}")[0]
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=megaphone&radius=6000&language=ru&opennow&location='+bi+','+bi2+'&key=AIzaSyDMkPyS3cWd1qIDDXYQHSLJ4PrV6ILkgVw')
    tp = r.text
    par_json = json.loads(tp)
    ft2 = str(par_json['results'][0]['geometry']["location"]["lat"])
    ft3 = str(par_json['results'][0]['geometry']["location"]["lng"])
    tgf_obj.bot.send_location(i.chat.id,ft2,ft3)
    return States.CO

def send_image(i,d):
	photo = open('wave.png', 'rb')
	tgf_obj.bot.send_photo(i.message.chat.id,photo)
	return States.LOGIN

def telinet(i):
    q = sql.internet_tv_us()
    return States.INFO

def cabine(i,login=None):
    font_size=36
    width=500
    height=100
    back_ground_color=(255,255,255)
    font_size=36
    font_size1=24
    font_size2=14
    font_color=(0,0,0)
    unicode_text5=u"Тариф"
    unicode_text = u"3"
    unicode_text1= str(login)
    unicode_text2=u"Баланс"
    unicode_text3=u""+sql.tarif_plan(login)
    unicode_text4=str(sql.cost_teck(login))
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(((120, 80), (330, 120)), fill=(0 , 0 , 255 ))
    draw.rectangle(((122, 82), (280, 118)), fill=(0, 255, 0))
    draw.ellipse([(30, 30 ), (110, 110)],fill=(255,80,0) )
    draw.ellipse([(170, 260), (350, 450)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    unicode_font2 = ImageFont.truetype("DejaVuSans.ttf", font_size2)
    draw.text ( (60,51), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (120,30), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,340), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (180,340), unicode_text4, font=unicode_font, fill=font_color )
    draw.text ( (20,160), unicode_text5, font=unicode_font1, fill=font_color )

    draw.text ( (140,160), unicode_text3, font=unicode_font1, fill=font_color )
    image.save('sample.png')
    p = open('sample.png','rb')
    tgf_obj.bot.send_photo(i.message.chat.id,p)

    return States.LK


def faq(i):
	request = apiai.ApiAI('faba0d3df0894d3eb09715883b78375e').text_request()
	request.lang = 'ru'
	request.session_id = 'MentorMeBot'
	request.query = i.text
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech']
	if response:
		tgf_obj.bot.send_message(i.chat.id,response)
	else:
		tgf_obj.bot.send_message(i.chat.id,"Undefineded question")
	return States.PROBLEMS

def phone(i):
    tgf_obj.bot.send_message(i.message.chat.id,'Номер поддержки')
    tgf_obj.bot.send_message(i.message.chat.id,sql.telephone())
    return States.LOGGED

def rek(i,login=None):
    tgf_obj.bot.send_message(i.message.chat.id,sql.r_uslugi_rek(login))
    return States.LK

def login(i,d):
	return States.PASS,{'login':i.text}

def brig():
    return States.LOGGED


def uslugi(i):
    q = sql.internet_tv_us()
    font_size=36
    width=500
    height=100
    back_ground_color=(255,255,255)
    font_size=36
    font_size1=28
    font_color=(0,0,0)

    unicode_text = u"Услуга №1"
    unicode_text1= u"Скорость:"+ q[0][1]
    unicode_text2=u"Каналы: " + q[0][2]
    unicode_text3=q[0][3]
    unicode_text4=q[0][4]
    unicode_text5=q[0][0]+'%'
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(((30, 250), (330, 280)), fill=(0, 0, 255))
    draw.rectangle(((32, 252), (328, 278)), fill=(255, 255, 255))
    draw.rectangle(((32, 252), (32+int(q[0][1]), 278)), fill=(0, 255, 90))
    draw.ellipse([(140, 90), (230, 180)],fill=(255,80,0) )
    draw.ellipse([(75, 330), (285, 390)],fill=(230,230,230) )
    draw.ellipse([(75, 400), (285, 460)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    draw.text ( (30,30), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (30,200), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,280), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (160,340), unicode_text3, font=unicode_font1, fill=font_color )
    draw.text ( (160,410), unicode_text4, font=unicode_font1, fill=font_color )
    draw.text ( (150,112), unicode_text5, font=unicode_font, fill=font_color )
    image.save('sample.png')
    p = open('sample.png','rb')
    tgf_obj.bot.send_photo(i.message.chat.id,p)

    unicode_text = u"Услуга №2"
    unicode_text1= u"Скорость:"+ q[1][1]
    unicode_text2=u"Каналы: " + q[1][2]
    unicode_text3=q[1][3]
    unicode_text4=q[1][4]
    unicode_text5=q[1][0]+'%'
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(((30, 250), (330, 280)), fill=(0, 0, 255))
    draw.rectangle(((32, 252), (328, 278)), fill=(255, 255, 255))
    draw.rectangle(((32, 252), (32+int(q[1][1]), 278)), fill=(0, 255, 90))
    draw.ellipse([(140, 90), (230, 180)],fill=(255,80,0) )
    draw.ellipse([(75, 330), (285, 390)],fill=(230,230,230) )
    draw.ellipse([(75, 400), (285, 460)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    draw.text ( (30,30), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (30,200), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,280), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (160,340), unicode_text3, font=unicode_font1, fill=font_color )
    draw.text ( (160,410), unicode_text4, font=unicode_font1, fill=font_color )
    draw.text ( (150,112), unicode_text5, font=unicode_font, fill=font_color )
    image.save('sample.png')
    p = open('sample.png','rb')
    tgf_obj.bot.send_photo(i.message.chat.id,p)

    unicode_text = u"Услуга №3"
    unicode_text1= u"Скорость:"+ q[2][1]
    unicode_text2=u"Каналы: " + q[2][2]
    unicode_text3=q[2][3]
    unicode_text4=q[2][4]
    unicode_text5=q[2][0]+'%'
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(((30, 250), (330, 280)), fill=(0, 0, 255))
    draw.rectangle(((32, 252), (328, 278)), fill=(255, 255, 255))
    draw.rectangle(((32, 252), (32+int(q[2][1]), 278)), fill=(0, 255, 90))
    draw.ellipse([(140, 90), (230, 180)],fill=(255,80,0) )
    draw.ellipse([(75, 330), (285, 390)],fill=(230,230,230) )
    draw.ellipse([(75, 400), (285, 460)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    draw.text ( (30,30), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (30,200), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,280), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (160,340), unicode_text3, font=unicode_font1, fill=font_color )
    draw.text ( (160,410), unicode_text4, font=unicode_font1, fill=font_color )
    draw.text ( (150,112), unicode_text5, font=unicode_font, fill=font_color )
    image.save('sample.png')
    p = open('sample.png','rb')
    tgf_obj.bot.send_photo(i.message.chat.id,p)

    return States.LK

def uslugi(i):
    q = sql.internet_tv_us()
    font_size=36
    width=500
    height=100
    back_ground_color=(255,255,255)
    font_size=36
    font_size1=28
    font_color=(0,0,0)

    unicode_text = u"Услуга №1"
    unicode_text1= u"Скорость:"+ q[0][1]
    unicode_text2=u"Каналы: " + q[0][2]
    unicode_text3=q[0][3]
    unicode_text4=q[0][4]
    unicode_text5=q[0][0]+'%'
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(((30, 250), (330, 280)), fill=(0, 0, 255))
    draw.rectangle(((32, 252), (328, 278)), fill=(255, 255, 255))
    draw.rectangle(((32, 252), (32+int(q[0][1]), 278)), fill=(0, 255, 90))
    draw.ellipse([(140, 90), (230, 180)],fill=(255,80,0) )
    draw.ellipse([(75, 330), (285, 390)],fill=(230,230,230) )
    draw.ellipse([(75, 400), (285, 460)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    draw.text ( (30,30), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (30,200), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,280), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (160,340), unicode_text3, font=unicode_font1, fill=font_color )
    draw.text ( (160,410), unicode_text4, font=unicode_font1, fill=font_color )
    draw.text ( (150,112), unicode_text5, font=unicode_font, fill=font_color )
    image.save('sample.png')
    p = open('sample.png','rb')
    tgf_obj.bot.send_photo(i.message.chat.id,p)

    unicode_text = u"Услуга №2"
    unicode_text1= u"Скорость:"+ q[1][1]
    unicode_text2=u"Каналы: " + q[1][2]
    unicode_text3=q[1][3]
    unicode_text4=q[1][4]
    unicode_text5=q[1][0]+'%'
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(((30, 250), (330, 280)), fill=(0, 0, 255))
    draw.rectangle(((32, 252), (328, 278)), fill=(255, 255, 255))
    draw.rectangle(((32, 252), (32+int(q[1][1]), 278)), fill=(0, 255, 90))
    draw.ellipse([(140, 90), (230, 180)],fill=(255,80,0) )
    draw.ellipse([(75, 330), (285, 390)],fill=(230,230,230) )
    draw.ellipse([(75, 400), (285, 460)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    draw.text ( (30,30), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (30,200), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,280), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (160,340), unicode_text3, font=unicode_font1, fill=font_color )
    draw.text ( (160,410), unicode_text4, font=unicode_font1, fill=font_color )
    draw.text ( (150,112), unicode_text5, font=unicode_font, fill=font_color )
    image.save('sample.png')
    p = open('sample.png','rb')
    tgf_obj.bot.send_photo(i.message.chat.id,p)

    unicode_text = u"Услуга №3"
    unicode_text1= u"Скорость:"+ q[2][1]
    unicode_text2=u"Каналы: " + q[2][2]
    unicode_text3=q[2][3]
    unicode_text4=q[2][4]
    unicode_text5=q[2][0]+'%'
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle(((30, 250), (330, 280)), fill=(0, 0, 255))
    draw.rectangle(((32, 252), (328, 278)), fill=(255, 255, 255))
    draw.rectangle(((32, 252), (32+int(q[2][1]), 278)), fill=(0, 255, 90))
    draw.ellipse([(140, 90), (230, 180)],fill=(255,80,0) )
    draw.ellipse([(75, 330), (285, 390)],fill=(230,230,230) )
    draw.ellipse([(75, 400), (285, 460)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    draw.text ( (30,30), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (30,200), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,280), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (160,340), unicode_text3, font=unicode_font1, fill=font_color )
    draw.text ( (160,410), unicode_text4, font=unicode_font1, fill=font_color )
    draw.text ( (150,112), unicode_text5, font=unicode_font, fill=font_color )
    image.save('sample.png')
    p = open('sample.png','rb')
    tgf_obj.bot.send_photo(i.message.chat.id,p)

    return States.INFO

def check_user(i,login=None):
	passwd  =i.text
	if sql.isLogin(login)==0:
		check = 0
	else:
		if sql.passPols(login)==i.text:
			check = 1
	if check:
		return States.LOGGED
	else:
		tgf_obj.bot.send_message(i.chat.id,'Неверный логин или пароль')
		return States.LOGIN


UI = {
    States.START:
    {'t':'Здравствуйте. Вы уже подключены к нашим услугам?',
     'b': [
         {'Да':tgf.action(States.LOGIN)},
         {'Нет':h.action(States.INFO)},],
         'react':h.action(geo, react_to = 'location'),

    },
    States.INFO:{
        't':'Возможно вас заинтересуют наши услуги',
        'b':[{'Просмотреть':tgf.action(uslugi1)},
        	 {'Назад':tgf.action(States.START)},
        ]
    },
    States.CO:{
        't':'Чтобы найти ближайший сервисный центр, отправьте свою геолокацию',
        'b':[{'Назад':tgf.action(States.LOGGED)}],
        'react':h.action(geo, react_to = 'location'),
    },
    States.LOGIN:{
        't':'Введите логин',
        'react':h.action(login,
            react_to = 'text'),
    },
    States.BRIG:
    {   't':'Вызвать монтажную бригаду\nВаш адрес: '+sql.addressPols('81756453')+'\nОпишите, пожалуйста, причины вызова бригады',
        'b':[{'Назад':tgf.action(States.LOGGED,update_msg=False)},],
        'react':h.action(brig, react_to = 'text',update_msg=False),
    },
    States.LOGGED:
    {	't':'Страница пользователя',
    	'b':[{'Кабинет':tgf.action(cabine,update_msg=False)},
    	{'Услуги':tgf.action(uslugi,update_msg=False)},
    	{'Помощник':tgf.action(States.PROBLEMS,update_msg=False)},
        {'Вызов бригады':tgf.action(States.BRIG,update_msg=False)},
    	{'Центр обслуживания':tgf.action(States.CO,update_msg=False)},
    	]
    },
    States.LK:
    {	't':'Страница пользователя',
    	'b':[{'Телефон поддержки':tgf.action(phone,update_msg=False)},
        {'Рекомендации':tgf.action(rek,update_msg=False)},
    	{'Назад':tgf.action(States.LOGGED,update_msg=False)},
    	]
    },
    States.PROBLEMS:
    {
    	't':'Сообщите нам о своей проблеме',
    	'b':[{'Назад':tgf.action(States.LOGGED,update_msg=False)}],
    	'react':h.action(faq, react_to = 'text',update_msg=False),
    },
    States.PASS:{
        't':'Введите пароль',
        'react': h.action(check_user, react_to='text',update_msg=False)},
    }

tgf.configure(token=key,state=States.START,data={"foo":'bar'})
tgf.start(UI)