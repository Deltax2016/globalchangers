from PIL import Image, ImageDraw, ImageFont, ImageFilter
def sample():
    font_size=36
    width=500
    height=100
    back_ground_color=(255,255,255)
    font_size=36
    font_size1=28
    font_color=(0,0,0)
    unicode_text5=u"тариф"
    unicode_text = u"3"
    unicode_text1= u"чето там"
    unicode_text2=u"баланс"
    unicode_text3=u"надпись"
    unicode_text4=u"сэйм  щит"
    image = Image.new('RGBA', (360, 480),'white')
    draw = ImageDraw.Draw(image)
    #draw.line(((320, 0), (320, 480)), fill=(255, 0, 0), width=50)  # красная линия
    #draw.arc(((150, 150), (250, 250)), 45, 210, fill=(0, 255, 0))  # зелёная дуга
    draw.rectangle(((120, 80), (330, 120)), fill=(0 , 0 , 255 ))
    draw.rectangle(((122, 82), (328, 118)), fill=(255, 255, 255))
    #draw.rectangle(((32, 252), (128, 278)), fill=(0, 255, 90))
    #draw.line((100,200, 150,300), fill=128)
   # font = ImageFont.truetype("data/kaligrafica_allfont_ru.ttf", 32)
    draw.ellipse([(30, 30 ), (110, 110)],fill=(255,80,0) )
    #draw.border(((80, 0), (80, 480)), fill=(255, 0, 0))
    #draw.text((200, 200), 'амва'.encode('utf-8'), (255, 255, 0))  # жёлтый текст
    #image = image.rotate(90)  # поворот на 90 градусов
    #draw.ellipse([(150, 140), (350, 230)],fill=(230,230,230) )
    draw.ellipse([(170, 260), (350, 450)],fill=(0,255,70) )
    unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    unicode_font1 = ImageFont.truetype("DejaVuSans.ttf", font_size1)
    draw.text ( (60,51), unicode_text, font=unicode_font, fill=font_color )
    draw.text ( (120,30), unicode_text1, font=unicode_font, fill=font_color )
    draw.text ( (30,340), unicode_text2, font=unicode_font, fill=font_color )
    draw.text ( (175,165), unicode_text3, font=unicode_font1, fill=font_color )
    draw.text ( (190,340), unicode_text4, font=unicode_font1, fill=font_color )
    draw.text ( (30,160), unicode_text5, font=unicode_font, fill=font_color )

    image.save('sample.png')
if __name__ == "__main__":
    sample()
    


