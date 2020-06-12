import telebot
import mysql.connector
import mytoken
import calendar

from telebot import types
from functools import wraps
from datetime import date
from datetime import datetime
from datetime import time
TOKEN = mytoken.TOKEN
isla = telebot.TeleBot(TOKEN)
tanggakskrng = date.today()
tanggalsekarang = date.today().strftime("%d %B, %Y")
tanggalwaktusekarang = datetime.now()

# database
myDbSiswa = mysql.connector.connect(host='localhost', user='root', password='', database='db_belajarbot')
sql = myDbSiswa.cursor()
from telebot import apihelper

class Isla:
    def __init__(self):
        self.message

    # @masBott.message_handler(commands=["start", "help"])
    @isla.message_handler(commands=["start"])
    def start(message):
        # photo = open('img/rpl1.png', 'rb')
        # myBot.send_photo(message.from_user.id, photo)
        teksStart = mytoken.START + "\nhari ini tanggal ("+str(tanggalsekarang)+")\n" \
                                    "hari ini adalah hari ("+calendar.day_name[tanggakskrng.weekday()]+")"
        isla.reply_to(message, teksStart)

    @isla.message_handler(commands=['help'])
    def help(message):
        teksHelp = mytoken.HELP
        isla.reply_to(message, teksHelp)

    @isla.message_handler(commands=['about'])
    def about(message):
        teksAbout = mytoken.ABOUT
        isla.reply_to(message, teksAbout)

    @isla.message_handler(commands=['datasiswa'])
    def datasiswa(message):
        query = "select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data = sql.fetchall()
        jumlahData = sql.rowcount
        kumpulanData = ''
        if(jumlahData>0):
            no=0
            for x in data:
                no += 1
                kumpulanData = kumpulanData + str(x)
                print(kumpulanData)
                kumpulanData = kumpulanData.replace('(', '')
                kumpulanData = kumpulanData.replace(')', '')
                kumpulanData = kumpulanData.replace("'", '')
                kumpulanData = kumpulanData.replace(",", '')
        else:
            print('data kosong')

        isla.reply_to(message, str(kumpulanData))

print(myDbSiswa)
print("bot sedang berjalan")
isla.polling(none_stop=True)