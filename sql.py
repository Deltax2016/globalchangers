import pymysql.cursors
import requests
import bs4
import random
# Connect to the database

def internet_tv_us():
    s = requests.get('https://www.wifire.ru/wifirepackets')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p3 = b.find(class_='wrapper_dop_usligi_pakets')
    d = []
    for i in range(1, 8, 3):
        pr_scid = str(p3).split("id")[i].split("span")[1].split("<")[0][1:]
        sk_inet = str(p3).split("id")[i].split("span")[7].split("<")[0][1:]
        vol_kan = str(p3).split("id")[i].split("span")[9].split("<")[0][1:]
        cost_without_sk = str(p3).split("id")[i].split("<s>")[1].split("<")[0][0:]
        cost_with_sk = str(p3).split("id")[i].split("<s>")[1].split("span")[1].split("<")[0][1:]
        d.append([pr_scid, sk_inet, vol_kan, cost_without_sk, cost_with_sk])
    return d


def tv_us():
    s = requests.get('https://www.wifire.ru/wifiretv')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p3 = b.find(class_='filler')
    d = []
    for i in range(1,12,10):
        tf = str(p3).split("id=")[i].split("span")[1].split(" ")[-1].split("+")[0]
        cost = str(p3).split("id=")[i].split("span")[2].split("em>")[1].split("<")[0]
        vol_knl = str(p3).split("id=")[i].split("span")[4].split("em>")[1].split("<")[0]
        d.append([tf, cost, vol_knl])
    for i in range(7,18,10):
        tf = str(p3).split("id=")[i].split(" ")[3].split("+")[0]
        cost = str(p3).split("id=")[i].split("price=\"")[1].split("\"")[0]
        vol_knl = str(p3).split("id=")[i].split("speed=\"")[1].split("\"")[0]
        d.append([tf, cost, vol_knl])
    d[3][1]=str(p3).split("id=")[18].split("em>")[1].split("<")[0]
    py = d[3][1]
    d[3][1] = d[3][2]
    d[3][2] = py
    pf = d[1]
    d[1] = d[2]
    d[2] = pf
    return d

def inet_us():
    return [[50,50,400],[100,100,600],[150,150,800],[300,300,1750]]

def inet_mob_us():
    return [[1,1,150],[4,4,400],[16,16,590],[36,36,890]]

def dop_uslug():
    return [["Турбокнопка", "Дополнительная услуга «100 Мбит/c на весь год» действительна для действующих Абонентов и позволяет увеличивать скорость на тарифном плане до 100 Мбит/c на 12 мес. с момента подключения.",1,599],
            ["Автоплатёж", "Данная услуга позволяет автоматически пополнять лицевой счет Wifire с вашей банковской карты.Теперь вы всегда будете на связи.", 0],
            ["Обещанный платеж", "Если средств на Вашем лицевом счете недостаточно, а внести платеж нет возможности, воспользуйтесь услугой «Обещанный платеж», которая будет предоставлена на 5 дней. Это позволит избежать блокировки Ваших аккаунтов.", 0],
            ["Переезд", "C услугой «Переезд» вы сможете использовать все ваши старые данные по новому адресу.", 0],
            ["Блокировка лицевого счета", "Услуга Оператора, неразрывно связанная с услугами связи, заключающаяся в блокировке Абонентской линии при временном неиспользовании услуг связи по инициативе Абонента.", 0],
            ["Магазин антивирусов", "Подключение программного обеспечения за абонентскую плату.", 0],
            ["Компьютерная помощь", "Вызов мастера для настройки программного обеспечения, лечение вирусов, ремонта персонального компьютера.", 1, "+74959802400"],
            ["Статический IP адрес", "При подключении услуги конкретный IP-адрес закрепляется и остается неизменным до отключения услуги", 1, 160]]


def dop_vol_tv():
    #name, vol_tv_kanal, cost , [name_kanal]
    return [["Позновательный", 12 , 119, ["Ocean TV", "Наука 2.0", "Galaxy", "НАНО ТВ", "Оружие", "Доктор", "История", "24 Техно", "Eureka HD", "ID Investigation Discovery", "DTX", "Планета HD"]],
            ["HD", 10, 279, ["Fox HD", "Fox Life HD", "Travel+Adventure HD", "National Geographic HD", "NatGeo Wild HD", "Outdoor channel HD", "Mezzo HD", "Fashion one HD", "HD Life", "MTV Live HD"]],
            ["Детям", 13, 169, ["Boomerang", "JimJam", "Мультимания", "Мультик HD", "Малыш", "Baby TV", "Тлум HD", "Детский мир", "Ginger HD", "Пингвин ЛОЛО", "Рыжий", "Nickelodeon HD", "TiJi"]],
            ["Чемпион", 7, 169, ["Extreme Sports Channel", "Футбол", "Авто 24", "Eurosport 2 HD", "КХЛ ТВ", "Авто Плюс"]],
            ["Amedia HD", 2, 219, ["Amedia HIT HD", "Amedia Premium HD"]],
            ["Наш футбол SD/HD", 2, 219, ["Наш Футбол", "Наш Футбол HD"]],
            ["Взрослый", 4, 169, ["O la la", "Playboy TV", "Brazzers Europe"]],
            ["Дождь", 1, 240, ["Дождь"]],
            ["Интернациональный", 6, 119, ["ТНВ Планета", "Телеканал «Майдан»", "ACB TV", "Беларусь 24", "Интер+", "NHK World"]],
            ["Настрой кино", 5, 380, ["Кинопремьера", "Киносвидание", "Кинохит", "Киносемья", "Мужское кино"]],
            ["Плюс Футбол", 3, 380, ["Футбол 1 HD", "Футбол 2 HD", "Футбол 3 HD"]]
            ]


def isLogin(login):
    print(login.isdigit(), len(login))
    if (login.isdigit() == 1) and (len(login) == 8):
        sql = "SELECT EXISTS(SELECT login FROM megathon.docs WHERE login = "+login+")"

        with connection.cursor() as cursor:
            # Create a new record
            # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
            cursor.execute(sql)
            results = cursor.fetchall()
            strf = "EXISTS(SELECT login FROM megathon.docs WHERE login = " + login + ")"
            print(results)
            print(strf)
            if results[0].get(strf) == 1:
                return 1
            else:
                return 0
    else:
        return 0

def telephone():
    return "+74959802400"
def passPols(login):
    sql = "select * from megathon.docs where login =" + login

    with connection.cursor() as cursor:
        cursor.execute(sql)

        results = cursor.fetchall()
        return results[0]["passwd"]

def addressPols(login):
    sql = "select * from megathon.docs where login =" + login

    with connection.cursor() as cursor:
        cursor.execute(sql)

        results = cursor.fetchall()
        return results[0]["address"]

def tarif_plan(login):
    sql = "select * from megathon.docs where login =" + login

    with connection.cursor() as cursor:
        cursor.execute(sql)

        results = str(cursor.fetchall()[0]["tf_plan"]).split("_")
        if results[0] == "tv-in":
            return "ТВ и Интернет " #+ internet_tv_us()[int(results[1])-1][1] + " мбит/с " + internet_tv_us()[int(results[1])-1][2] + " каналов"
        elif results[0] == "tv":
            return "Цифровое телевидение."# Тариф: " + tv_us()[int(results[1])-1][0] + "+. " + tv_us()[int(results[1])-1][2] + " каналов"
        elif results[0] == "in":
            return "Проводной интернет." # Тариф: " #+ str(inet_us()[int(results[1])-1][0]) + ". Скорость: " + str(inet_us()[int(results[1])-1][1]) + " мбит/с"
        else:
            return

def cost_tarif_plan(login):
    sql = "select * from megathon.docs where login =" + login

    with connection.cursor() as cursor:
        cursor.execute(sql)

        results = str(cursor.fetchall()[0]["tf_plan"]).split("_")
        if results[0] == "tv-in":
            return "Стоимость тарифа: " + internet_tv_us()[int(results[1]) - 1][4] + " руб/мес"
        elif results[0] == "tv":
            return "Стоимость тарифа: " + tv_us()[int(results[1]) - 1][1] + " руб/мес"
        elif results[0] == "in":
            return "Стоимость тарифа: " + str(inet_us()[int(results[1]) - 1][2]) + " руб/мес"
        else:
            return

def dop_uslugi_tv(login):
    sql = "select * from megathon.docs where login =" + login

    with connection.cursor() as cursor:
        cursor.execute(sql)

        results = str(cursor.fetchall()[0]["dop_uslugi_tv"])
        if results == "-1":
            return "Дополнительных пакетов каналов не подключено"
        else:
            stp = results.split("-")
            stric = "Подключены дополнительные пакеты каналов: \n"
            for pk in range(len(stp)):
                stric += dop_vol_tv()[int(stp[pk].split("_")[1])-1][0] + ": "
                for i in range(len(dop_vol_tv()[int(stp[pk].split("_")[1])-1][3])-1):
                    stric += dop_vol_tv()[int(stp[pk].split("_")[1])-1][3][i] + ", "
                stric += str(dop_vol_tv()[int(stp[pk].split("_")[1])-1][3][-1])
                stric += "\n"
            return stric



def r_uslugi_rek(login):
    sql = "select * from megathon.docs where login =" + login

    with connection.cursor() as cursor:
        cursor.execute(sql)

        results = str(cursor.fetchall()[0]["dop_uslugi_tv"])
        d = []
        if results != "-1":
            stp = results.split("-")
            for po in range(len(stp)):
                d.append(int(stp[po].split("_")[1])-1)
            t =100
            while t>0:
                i = random.randint(0, 10)
                if i in d:
                    t  = 100
                else:
                    t = -10
            stric = "Предлагаю вашему внимаю пакет услуг: " + dop_vol_tv()[i][0] + " с каналами: "
            for j in dop_vol_tv()[i][3]:
                stric += j +", "

            stric += "по цене: "+str(dop_vol_tv()[i][2])
            return stric


def cost_teck(login):
    sql = "select * from megathon.docs where login =" + login

    with connection.cursor() as cursor:
        cursor.execute(sql)

        results = str(cursor.fetchall()[0]["balance"])
        return results

def cost_update(login, cost):

    balance2 = str(cost + cost_teck(login))
    sql = "UPDATE megathon.docs SET balance = " + balance2 +" WHERE login=" + "login;"




connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='cxzaq15061999',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             init_command='SET NAMES UTF8')


