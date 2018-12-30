# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybatibot.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import fbchat
import requests
import random
from time import sleep
from random import shuffle
from fbchat import Client
from fbchat.models import *
import mysql.connector
import os
import _thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global gametype
        global info_answer
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_box = QtWidgets.QGroupBox(self.centralwidget)
        self.login_box.setGeometry(QtCore.QRect(10, 0, 191, 121))
        self.login_box.setObjectName("login_box")
        self.login_u_name = QtWidgets.QLineEdit(self.login_box)
        self.login_u_name.setGeometry(QtCore.QRect(20, 20, 161, 20))
        self.login_u_name.setObjectName("login_u_name")
        self.login_u_pass = QtWidgets.QLineEdit(self.login_box)
        self.login_u_pass.setGeometry(QtCore.QRect(20, 50, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.login_u_pass.setFont(font)
        self.login_u_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_u_pass.setObjectName("login_u_pass")
        self.login_btn = QtWidgets.QPushButton(self.login_box)
        self.login_btn.setGeometry(QtCore.QRect(20, 80, 41, 21))
        self.login_btn.setObjectName("login_btn")
        self.status_box = QtWidgets.QGroupBox(self.centralwidget)
        self.status_box.setGeometry(QtCore.QRect(210, 0, 91, 51))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.status_box.setFont(font)
        self.status_box.setObjectName("status_box")
        self.status_isOnline = QtWidgets.QLabel(self.status_box)
        self.status_isOnline.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.status_isOnline.setFont(font)
        self.status_isOnline.setAlignment(QtCore.Qt.AlignCenter)
        self.status_isOnline.setObjectName("status_isOnline")
        self.commands_box = QtWidgets.QGroupBox(self.centralwidget)
        self.commands_box.setGeometry(QtCore.QRect(230, 130, 361, 221))
        self.commands_box.setObjectName("commands_box")
        self.commands_text = QtWidgets.QTextEdit(self.commands_box)
        self.commands_text.setGeometry(QtCore.QRect(10, 20, 341, 191))
        self.commands_text.setReadOnly(True)
        self.commands_text.setObjectName("commands_text")
        self.controls_box = QtWidgets.QGroupBox(self.centralwidget)
        self.controls_box.setGeometry(QtCore.QRect(10, 130, 201, 221))
        self.controls_box.setObjectName("controls_box")
        self.controls_room_box = QtWidgets.QGroupBox(self.controls_box)
        self.controls_room_box.setGeometry(QtCore.QRect(10, 20, 181, 111))
        self.controls_room_box.setObjectName("controls_room_box")
        self.controls_room_roomId = QtWidgets.QLineEdit(self.controls_room_box)
        self.controls_room_roomId.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.controls_room_roomId.setObjectName("controls_room_roomId")
        self.controls_room_roomBtn = QtWidgets.QPushButton(
            self.controls_room_box)
        self.controls_room_roomBtn.setGeometry(QtCore.QRect(130, 20, 41, 21))
        self.controls_room_roomBtn.setObjectName("controls_room_roomBtn")
        self.controls_room_roomNick = QtWidgets.QLineEdit(
            self.controls_room_box)
        self.controls_room_roomNick.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.controls_room_roomNick.setObjectName("controls_room_roomNick")
        self.controls_room_nickBtn = QtWidgets.QPushButton(
            self.controls_room_box)
        self.controls_room_nickBtn.setGeometry(QtCore.QRect(130, 50, 41, 21))
        self.controls_room_nickBtn.setObjectName("controls_room_nickBtn")
        self.controls_room_rounds = QtWidgets.QLineEdit(self.controls_room_box)
        self.controls_room_rounds.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.controls_room_rounds.setObjectName("controls_room_rounds")
        self.controls_room_roundsBtn = QtWidgets.QPushButton(
            self.controls_room_box)
        self.controls_room_roundsBtn.setGeometry(QtCore.QRect(130, 80, 41, 21))
        self.controls_room_roundsBtn.setObjectName("controls_room_roundsBtn")
        self.controls_pause = QtWidgets.QPushButton(self.controls_box)
        self.controls_pause.setGeometry(QtCore.QRect(10, 130, 181, 23))
        self.controls_pause.setObjectName("controls_pause")
        self.controls_newgame = QtWidgets.QPushButton(self.controls_box)
        self.controls_newgame.setGeometry(QtCore.QRect(10, 160, 181, 23))
        self.controls_newgame.setObjectName("controls_newgame")
        self.controls_exit = QtWidgets.QPushButton(self.controls_box)
        self.controls_exit.setGeometry(QtCore.QRect(10, 190, 181, 23))
        self.controls_exit.setObjectName("controls_exit")
        self.info_box = QtWidgets.QGroupBox(self.centralwidget)
        self.info_box.setGeometry(QtCore.QRect(310, 0, 281, 121))
        self.info_box.setObjectName("info_box")
        self.info_roomId_box = QtWidgets.QGroupBox(self.info_box)
        self.info_roomId_box.setGeometry(QtCore.QRect(10, 20, 261, 41))
        self.info_roomId_box.setObjectName("info_roomId_box")
        self.info_roomId = QtWidgets.QLabel(self.info_roomId_box)
        self.info_roomId.setGeometry(QtCore.QRect(10, 12, 241, 21))
        self.info_roomId.setAlignment(QtCore.Qt.AlignCenter)
        self.info_roomId.setObjectName("info_roomId")
        self.info_answer_box = QtWidgets.QGroupBox(self.info_box)
        self.info_answer_box.setGeometry(QtCore.QRect(10, 70, 261, 41))
        self.info_answer_box.setObjectName("info_answer_box")
        info_answer = QtWidgets.QLabel(self.info_answer_box)
        info_answer.setGeometry(QtCore.QRect(10, 10, 241, 21))
        info_answer.setAlignment(QtCore.Qt.AlignCenter)
        info_answer.setObjectName("info_answer")
        self.gametype_box = QtWidgets.QGroupBox(self.centralwidget)
        self.gametype_box.setGeometry(QtCore.QRect(210, 60, 91, 61))
        self.gametype_box.setObjectName("gametype_box")
        gametype = QtWidgets.QLabel(self.gametype_box)
        gametype.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        gametype.setFont(font)
        gametype.setAlignment(QtCore.Qt.AlignCenter)
        gametype.setObjectName("gametype")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionjamgph_com = QtWidgets.QAction(MainWindow)
        self.actionjamgph_com.setObjectName("actionjamgph_com")
        self.actionCreator = QtWidgets.QAction(MainWindow)
        self.actionCreator.setObjectName("actionCreator")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # options
        self.status_isOnline.setStyleSheet("color: red")
        self.controls_box.setEnabled(False)
        self.controls_newgame.hide()
        self.controls_room_nickBtn.setEnabled(False)
        self.controls_room_roundsBtn.setEnabled(False)
        self.controls_pause.setEnabled(False)

        # set window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("jamg.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # login button click event
        self.login_btn.clicked.connect(self.f_login)

        # room button click event
        self.controls_room_roomBtn.clicked.connect(self.f_setRoomId)

        # start game click event
        self.controls_pause.clicked.connect(self.f_startGame)

        # exit click event
        self.controls_exit.clicked.connect(self.close)

        # enter event
        self.login_u_pass.returnPressed.connect(self.f_login)

        # nick button
        self.controls_room_nickBtn.clicked.connect(self.f_changeNick)

        # round button
        self.controls_room_roundsBtn.clicked.connect(self.f_changeRound)

        # adding placeholders
        self.login_u_name.setPlaceholderText("Username")
        self.login_u_pass.setPlaceholderText("Password")
        self.controls_room_roomId.setPlaceholderText("Room ID")
        self.controls_room_roomNick.setPlaceholderText("Nickname")
        self.controls_room_rounds.setPlaceholderText("Rounds")

        
    def close(self):
        client.logout()
        exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBatibot"))
        self.login_box.setTitle(_translate("MainWindow", "Login"))
        self.login_u_name.setText(_translate("MainWindow", ""))
        self.login_u_pass.setText(_translate("MainWindow", ""))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.status_box.setTitle(_translate("MainWindow", "Status"))
        self.status_isOnline.setText(_translate("MainWindow", "OFFLINE"))
        self.commands_box.setTitle(_translate("MainWindow", "Commands"))
        self.commands_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!join</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - join game</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!clue</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - texttwist word definition</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!shuffle</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - texttwist shuffle word</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!score</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - show scores</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!repeat</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - repeat question</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!shuffle</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - shuffle word letters</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!pass</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - next question</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!rounds</span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"> - set max rounds</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">GAME MODES</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!texttwist</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!bugtong</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!opm</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!math</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; font-weight:600; color:#000000;\">!all</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:8pt; color:#000000;\">if you found a bug, kindly report immediately</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://jamhph.com\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://jamhph.com</span></a></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://facebook.com/jammmg\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://facebook.com/jammmg</span></a></p></body></html>"))
        self.controls_box.setTitle(_translate("MainWindow", "Controls"))
        self.controls_room_box.setTitle(
            _translate("MainWindow", "Room Settings"))
        self.controls_room_roomId.setText(_translate("MainWindow", ""))
        self.controls_room_roomBtn.setText(_translate("MainWindow", "SET"))
        self.controls_room_roomNick.setText(
            _translate("MainWindow", ""))
        self.controls_room_nickBtn.setText(_translate("MainWindow", "SET"))
        self.controls_room_rounds.setText(_translate("MainWindow", ""))
        self.controls_room_roundsBtn.setText(_translate("MainWindow", "SET"))
        self.controls_pause.setText(_translate("MainWindow", "START"))
        self.controls_newgame.setText(_translate("MainWindow", "NEW GAME"))
        self.controls_exit.setText(_translate("MainWindow", "LOGOUT AND EXIT"))
        self.info_box.setTitle(_translate("MainWindow", "Information"))
        self.info_roomId_box.setTitle(_translate("MainWindow", "Room ID"))
        self.info_roomId.setText(_translate("MainWindow", "-"))
        self.info_answer_box.setTitle(_translate("MainWindow", "Answer"))
        info_answer.setText(_translate("MainWindow", "-"))
        self.gametype_box.setTitle(_translate("MainWindow", "Game Type"))
        gametype.setText(_translate("MainWindow", "-"))
        self.actionjamgph_com.setText(_translate("MainWindow", "jamgph.com"))
        self.actionCreator.setText(_translate("MainWindow", "Creator"))

    def f_login(self):
        self.login_box.setEnabled(False)
        self.status_isOnline.setText("LOGGING")
        u_name = self.login_u_name.text()
        u_pass = self.login_u_pass.text()
        sub = subscription(u_name)
        if sub == "active":
            _thread.start_new_thread(self.f_auth, (u_name, u_pass))
        else:
            self.popup("FAILED", "Your account is not active")
            self.status_isOnline.setText("OFFLINE")
            self.login_box.setEnabled(True)
        

    def f_auth(self, u_name, u_pass):
        global client
        global session_cookies
        try:
            client = Client(u_name, u_pass)
            session_cookies = client.getSession()
            self.status_isOnline.setText("ONLINE")
            self.status_isOnline.setStyleSheet("color: green")
            self.controls_box.setEnabled(True)
        except fbchat.models.FBchatUserError:
            self.status_isOnline.setText("FAILED")
            self.status_isOnline.setStyleSheet("color: red")
            self.login_btn.show()
    
    def f_auth_gamebot(self):
        jamg = Jamg("", "", session_cookies=session_cookies)
        jamg.listen()

    
    def f_setRoomId(self):
        try:
            self.controls_room_roomId.setStyleSheet("color: black")
            room_id = int(self.controls_room_roomId.text())
            self.controls_room_roomId.setStyleSheet("color: green")
            self.info_roomId.setText(f'{room_id}')
            Jamg.thread_id = room_id
            self.controls_room_nickBtn.setEnabled(True)
            self.controls_room_roundsBtn.setEnabled(True)
            self.controls_pause.setEnabled(True)
            self.controls_room_roomBtn.setEnabled(False)
        except ValueError:
            self.popup("ERROR", "Invalid Room ID")

    def f_startGame(self):
        self.controls_pause.setEnabled(False)
        _thread.start_new_thread(self.f_auth_gamebot, ())

    def popup(self, error, msg):
        QMessageBox.about(MainWindow, error, msg)

    def f_gameType(self, title, ans):
        gametype.setText(title)
        info_answer.setText(ans)

    def f_changeNick(self):
        nickname = str(self.controls_room_roomNick.text())
        client.changeNickname(nickname, client.uid, thread_id=Jamg.thread_id, thread_type=ThreadType.GROUP)

    def f_changeRound(self):
        rounds = int(self.controls_room_rounds.text())
        Jamg.max_game_rounds = rounds
        send_msg(f"Round changed to {rounds}")


my_db = mysql.connector.connect(
    host="35.187.240.251",
    user="jamg",
    passwd="jamuel26",
    database="bot"
)
my_cursor = my_db.cursor()

def subscription(user):
    u = user
    my_cursor.execute(f"SELECT * FROM subs WHERE id = 1")
    my_result = my_cursor.fetchall()
    res = list(my_result)
    for x in res:
        res = x[2]
    return res


def define(word):
    app_id = '0d6c4d8a'
    app_key = '642dd9bb994eb786bea9ac1453dedb07'
    language = 'en'
    url = f'https://od-api.oxforddictionaries.com:443/api/v1/entries/{language}/{word.lower()}'
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    
    if r.status_code == 404:
        return "no data"
    else:
        da = r.json()
        try:
            res = da['results'][0]["lexicalEntries"][0]['entries'][0]['senses'][0]['definitions']
            return "".join(res)
        except KeyError:
            return "no data"
 


def rand_a():
    a = random.randint(0, 999)
    return a


def rand_b():
    b = random.randint(0, 999)
    return b

def send_msg(msg):
        client.send(Message(text=f"{msg}"),
                    thread_id=Jamg.thread_id, thread_type=ThreadType.GROUP)

class Jamg(Client):
    # main variables
    answer = "" # game answer
    thread_id = "" # game room id
    rounds = 1 # rounds
    users = {} # list of users
    users_count = 1 # count of users
    joined = 0 # if user is joined
    question = "" # game question
    admin_uid = "100005766793253" # admin uid

    # game options default
    game_math = 0 
    game_tt = 0
    game_all = 1
    game_opm = 0
    game_bugtong = 0
    paused = 0
    game_title = ""

    # misc
    game_tt_check = 0

    # next_game manager
    next_game = -1
    next_game_name = ""
    max_game_rounds = 50

    def set_defaults(self):
        self.answer = "" # game answer
        self.rounds = 1 # rounds
        self.question = "" # game question


    def post_msg(self, msg):
        client.send(Message(text=f"{msg}"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)

    def join_user(self, id, name):
        self.users[self.users_count] = [id, name, 0]
        self.users_count += 1
        

    def shuffle(self):
        x = [i for i in range(leng)]
        shuffle(x)
        shuff = []
        for y in x:
            shuff.append(word[y])
        shuff = "".join(shuff)
        self.question = f"{shuff}"
        self.repeat()

    def next_gamemode(self, game):
        if self.next_game > 0:
            self.next_game -= 1
        if self.next_game == 0:
            self.post_msg(f"Game changing to {game}")
            self.next_game = -1
            self.game_changer(game)

    def max_rounds(self):
        if self.rounds > self.max_game_rounds:
            self.post_msg("Congratulations!")
            high_score = 0
            for x in self.users:
                if self.users[x][2] > high_score:
                    high_score = self.users[x][2]
                    high_name = self.users[x][1]
            self.post_msg(f"{high_name} = {high_score}")
            self.post_msg("Restarting game...")
            sleep(3)
            for x in self.users:
                self.users[x][2] = 0
            self.set_defaults()
            self.game_changer("all")


    def game_manager(self):
        self.next_gamemode(self.next_game_name)
        self.max_rounds()
        # main
        if self.game_math == 1:
            self.game_tt_check = 0
            m_pick = random.randint(1, 2)
            if m_pick == 1:
                self.game_title = "ADDITION\n"
                return self.math_add()
            if m_pick == 2:
                self.game_title = "MINUS\n"
                return self.math_difference()

        if self.game_tt == 1:
            self.game_tt_check = 1
            self.game_title = "TEXTTWIST\n"
            return self.text_twist()

        if self.game_opm == 1:
            self.game_tt_check = 0
            self.game_title = "GTA\n"
            return self.opm()

        if self.game_bugtong == 1:
            self.game_tt_check = 0
            self.game_title = "BUGTONG\n"
            return self.bugtong()

        if self.game_all == 1:
            a_pick = random.randint(1, 4)
            if a_pick == 1:
                self.game_tt_check = 0
                m_pick = random.randint(1, 2)
                if m_pick == 1:
                    self.game_title = "ADDITION\n"
                    return self.math_add()
                if m_pick ==2:
                    self.game_title = "MINUS\n"
                    return self.math_difference()
            if a_pick == 2:
                self.game_tt_check = 1
                self.game_title = "TEXTTWIST\n"
                return self.text_twist()
            if a_pick == 3:
                self.game_tt_check = 0
                self.game_title = "GTA\n"
                return self.opm()
            if a_pick == 4:
                self.game_tt_check = 0
                self.game_title = "BUGTONG\n"
                return self.bugtong()
            

    def bugtong(self):
        with open('bugtong.txt', encoding="utf8") as f:
            bugtong = []
            for x in f:
                bugtong.append(x)
        ran = random.randint(0, 158)
        bugtong = bugtong[ran]
        bugtong = bugtong.split('#')
        self.question = bugtong[0]
        self.answer = bugtong[1].rstrip()
        client.send(Message(text=f"ROUND {self.rounds}\nBUGTONG"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        self.repeat()

    def opm(self):
        with open('opm.txt', 'r') as f:
            opm = []
            for x in f:
                opm.append(x)
        ran = random.randint(0, 551)
        opm = opm[ran]
        opm = opm.split(',')
        self.question = f"{opm[1]}"
        self.answer = opm[2].rstrip()
        client.send(Message(text=f"ROUND {self.rounds}\nGUESS OPM ARTIST"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        self.repeat()


    def text_twist(self):
        global leng
        global word
        # opening file putting word in words
        with open('words.txt', 'r') as f:
            words = []
            for x in f:
                words.append(x)
        # generating random line in words.txt
        ran = random.randint(0, 2047)
        # getting a line of word
        word = words[ran]  # answer

        # getting length of a word
        leng = len(word) - 1
        # rumbling range of number
        x = [i for i in range(leng)]

        shuffle(x)

        # referencing numbers in every char
        shuff = []
        for y in x:
            shuff.append(word[y])

        # joining array of letters
        shuff = "".join(shuff)
        self.question = f"{shuff}"
        self.answer = word.rstrip()
        client.send(Message(text=f"ROUND {self.rounds}\nTEXT TWIST"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        self.repeat()

    def math_add(self):
        a = rand_a()
        b = rand_b()
        self.answer = f"{a+b}"
        self.question = f"{a} + {b} = ?"
        client.send(Message(text=f"ROUND {self.rounds}\nMATH"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        self.repeat()

    def math_difference(self):
        a = rand_a()
        b = rand_b()
        self.answer = f"{a-b}"
        self.question = f"{a} - {b} = ?"
        client.send(Message(text=f"ROUND {self.rounds}\nMATH"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        self.repeat()

    def repeat(self):
        client.send(Message(text=f"{self.question}"), thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        print(self.answer)

    def onQprimer(self, **kwargs):
        client.changeNickname("PyBatibot", client.uid, thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        client.send(Message(text="Gamebot ON!"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        client.send(Message(text="Created by: Jamg"),
                    thread_id=self.thread_id, thread_type=ThreadType.GROUP)
        self.game_manager()
    
    def game_reset(self):
        self.game_all = 1
        self.game_tt = 0
        self.game_math = 0
        self.game_opm = 0
        self.game_bugtong = 0
    
    def game_changer(self, game):
        self.game_reset()
        if game == "bugtong":
            self.game_bugtong = 1
        if game == "opm":
            self.game_opm = 1
        if game == "math":
            self.game_math = 1
        if game == "tt":
            self.game_tt = 1
    
    def next_game_name_changer(self, name):
        self.next_game = 3
        self.next_game_name = name
        self.post_msg(f"Game mode will change to {name} after 3 questions")


    def onMessage(self, author_id, message_object, thread_id, thread_type, metadata, msg, **kwargs):
        u_ui = Ui_MainWindow()
        u_ui.f_gameType(self.game_title.rstrip(), self.answer)
        command = message_object.text.lower()
        if self.paused == 1:
            if "!unpause" in command:
                self.post_msg("Bot Unpaused")
                self.paused = 0
                self.repeat()
        if self.paused == 0:
            print(self.thread_id, thread_id)
            # gamebot only selected thread
            if str(thread_id) == str(self.thread_id):
                print(command, 3)
                if author_id != self.uid:
                    print(command, 4)
                    if "!pause" in command:
                        self.post_msg("Bot Paused")
                        self.paused = 1
                    if "!about" in command:
                        self.post_msg("Gamebot for facebook")
                        self.post_msg("For bugs please report to my facebook\nJamuel Galicia")
                    if "!rounds" in command:
                        rounds = command.split()
                        try:
                            r = int(rounds[1])
                            self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                            self.max_game_rounds = r
                            self.post_msg(f"Max round changed to {r}")
                        except ValueError:
                            self.reactToMessage(
                                message_object.uid, MessageReaction.NO)

                    if "!about" in command:
                        self.post_msg("PyBatibot gamebot for facebook")
                        self.post_msg("Created by: Jamuel Galicia")
                    if "!bugtong" in command:
                        self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                        self.next_game_name_changer("bugtong")
                    if "!opm" in command:
                        self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                        self.next_game_name_changer("opm")
                    if "!math" in command:
                        self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                        self.next_game_name_changer("math")
                    if "!texttwist" in command:
                        self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                        self.next_game_name_changer("tt")
                    if "!all" in command:
                        self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                        self.next_game_name_changer("all")
                    if "!clue" in command:
                        if self.game_tt_check == 1:
                            self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                            self.send(Message(text=define(self.answer)),
                                    thread_id=thread_id, thread_type=thread_type)
                    if "!shuffle" in command:
                        if self.game_tt_check == 1:
                            try:
                                self.shuffle()
                                self.reactToMessage(
                                    message_object.uid, MessageReaction.YES)
                            except NameError:
                                self.reactToMessage(
                                    message_object.uid, MessageReaction.NO)
                                
                    if "!pass" in command:
                        self.reactToMessage(message_object.uid,
                                            MessageReaction.YES)
                        self.send(Message(text=f"the correct answer is:\n{self.answer}"),
                                        thread_id=thread_id, thread_type=thread_type)
                        sleep(3)
                        self.game_manager()
                    if "!repeat" in command:
                        self.reactToMessage(message_object.uid,
                                            MessageReaction.YES)
                        self.repeat()
                    if "!join" in command:
                        join = 0
                        u_join = self.fetchUserInfo(author_id)[author_id]
                        try:
                            name = u_join.first_name
                            for x in self.users:
                                if author_id in self.users[x][0]:
                                    join = 1
                            if join == 0:
                                self.reactToMessage(
                                    message_object.uid, MessageReaction.YES)
                                self.join_user(author_id, name)
                                self.send(Message(text=f"{name} joined."),
                                        thread_id=thread_id, thread_type=thread_type)
                            else:
                                self.reactToMessage(
                                    message_object.uid, MessageReaction.NO)
                                self.send(Message(text="You already joined."),
                                        thread_id=thread_id, thread_type=thread_type)
                        except IndexError:
                            self.reactToMessage(
                                message_object.uid, MessageReaction.NO)
                            print("Index error")
                    if "!score" in command:
                        self.reactToMessage(message_object.uid, MessageReaction.YES)
                        scores = ""
                        for x in self.users:
                            scores += self.users[x][1]
                            scores += " = "
                            scores += str(self.users[x][2])
                            scores += "\n"
                        self.post_msg(scores)
                    if "!help" in command:
                        self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                        self.send(Message(text="COMMAND LIST:\n\n"
                                                    "!join - join game\n\n"
                                                    "!clue - texttwist word definition\n\n"
                                                    "!shuffle - texttwist shuffle word\n\n"
                                                    "!score - show scores\n\n"
                                                    "!repeat - repeat question\n\n"
                                                    "!shuffle - shuffle word letters\n\n"
                                                    "!pass - next question\n\n"
                                                    "!rounds - set max rounds"),
                                        thread_id=thread_id,
                                        thread_type=thread_type)
                        self.send(Message(text=f"Pick a game\n!math\n!texttwist\n!opm\n!bugtong\n!all"),
                        thread_id=self.thread_id, thread_type=ThreadType.GROUP)
                        
                    if self.answer in command:
                        self.joined = 0
                        command = command.split()
                        command = " ".join(command[0:])
                        for x in self.users:
                            if author_id in self.users[x]:
                                self.reactToMessage(
                                    message_object.uid, MessageReaction.LOVE)
                                self.users[x][2] += 1
                                self.send(Message(text=f"{self.users[x][1]} got the correct answer!\n{self.users[x][1]} = {self.users[x][2]}"),
                                        thread_id=thread_id, thread_type=thread_type)
                                self.joined = 1
                                self.rounds += 1
                                self.game_manager()
                        if self.joined == 0:
                            self.reactToMessage(
                                message_object.uid, MessageReaction.YES)
                            self.send(Message(text="Type !join to participate"),
                                    thread_id=thread_id, thread_type=thread_type)


def main():
    url = "https://php.jamgph.com/cron.php?activatebot=jamgph.com"
    r = requests.get(url)
    res = r.text.rstrip()
    if res == "true":
        pass
    else:
        exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main()
    sys.exit(app.exec_())
