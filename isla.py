import telebot
import mysql.connector
import mytoken
import calendar
import ast
import time

from telebot import apihelper
from telebot import types
from functools import wraps
from datetime import date
from datetime import datetime
from time import sleep
# from datetime import time

TOKEN = mytoken.TOKEN
isla = telebot.TeleBot(TOKEN)

tanggakskrng = date.today()
tanggalsekarang = date.today().strftime("%d %B, %Y")
tanggalwaktusekarang = datetime.now()

# database
myDbSiswa = mysql.connector.connect(host='localhost', user='root', password='', database='db_belajarbot')
sql = myDbSiswa.cursor() # untuk mengeksekusi perintah SQL atau query

class Isla:
    def __init__(self):
        self.message

#=================================================UTAMA=================================================================

    @isla.message_handler(commands=["start"])
    def start(message):
        teksStart = mytoken.START + "\nhari ini tanggal ("+str(tanggalsekarang)+")\n" \
                                    "hari ini adalah hari ("+calendar.day_name[tanggakskrng.weekday()]+")"

        isla.send_chat_action(message.from_user.id, action='typing')
        time.sleep(0.3)

        isla.reply_to(message, teksStart)

    @isla.message_handler(commands=['help'])
    def help(message):
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton('Hubungi developer saya', url = 't.me/Bayu_kartiko')
        )

        teksHelp = mytoken.HELP
        isla.send_chat_action(message.from_user.id, action='typing')
        time.sleep(0.3)

        isla.reply_to(message, teksHelp, reply_markup=keyboard)

#====================================================COBA-COBA==========================================================

    @isla.message_handler(commands=['about'])
    def about(message):
        teksAbout = mytoken.ABOUT

        isla.send_chat_action(message.from_user.id, action='typing')
        time.sleep(0.3)

        isla.reply_to(message, teksAbout)

    @isla.message_handler(commands=['pp'])
    def foto(message):
        markup = types.InlineKeyboardMarkup()
        textFoto = 'Isla harap kamu kamu suka dengan foto Isla 🥰'
        textFoto2 = 'tunggu sebentar yaa... Isla lagi foto selfie dulu nih 🤳'
        textFoto3 = 'itu foto Isla.. aku harap kamu suka ^_^'

        isla.reply_to(message, textFoto)
        isla.send_chat_action(message.from_user.id, action='typing')
        time.sleep(0.3)
        isla.send_message(message.from_user.id, textFoto2)

        photo = open('img/fotoBot.jpg', 'rb')
        isla.send_chat_action(message.from_user.id, action='upload_photo')
        time.sleep(1)
        isla.send_photo(message.from_user.id, photo)

        isla.send_chat_action(message.from_user.id, action='typing')
        time.sleep(0.3)
        isla.send_message(message.from_user.id, textFoto3)

#===============================================TUGAS===================================================================

    @isla.message_handler(commands=['datasiswa'])
    def datasiswa(message):
        query = "select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data = sql.fetchall() # mengambil semua baris di database
        jumlahData = sql.rowcount
        kumpulanData = ''
        if(jumlahData>0):
            # print(data)
            no = 0
            for x in data:
                no += 1
                kumpulanData = kumpulanData + str(x)
                print(kumpulanData)
                kumpulanData = kumpulanData.replace('(', str(no)+".} ")
                kumpulanData = kumpulanData.replace(')', '\n')
                kumpulanData = kumpulanData.replace("'", '')
                kumpulanData = kumpulanData.replace(",", '')
        else:
            print('data kosong')

        # isla.send_message()
        kirimData = "data siswa kelas XI RPL ada dibawah ini 👇👇\n\n" + str(kumpulanData)

        isla.send_chat_action(message.from_user.id, action='typing')
        time.sleep(0.5)
        isla.reply_to(message, kirimData)

print(myDbSiswa)
print("bot sedang berjalan")
isla.polling(none_stop=True)