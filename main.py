import sys
import random
import vlc
import os

from os import listdir
from os.path import isfile, join
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

STATUS = True
NOW_SELECTED = ''
musics_list = []

class Main(QWidget):
    def __init__(self):
        """
        Initialized program.
        """
        super(Main, self).__init__()
        uic.loadUi('UI.ui', self)
        self.play_button.clicked.connect(self.play_song)
        self.stop_button.clicked.connect(self.stop_song)
        self.rand_button.clicked.connect(self.rand_song)
        self.toggle_button.clicked.connect(self.starting_list)
        self.music_list.itemSelectionChanged.connect(self.selectionChanged)
        self.starting_list()

    def starting_list(self):
        global STATUS
        global musics_list
        musics_list = []

        if STATUS:
            self.toggle_button.setText('ON')
            self.toggle_button.setStyleSheet('QPushButton {\n	color: white;\n	background-color: #7fff00;\n}\n\nQPushButton:pressed {\n	background-color: #006400;\n}')
            mypath = os.getcwd()
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            for _ in onlyfiles:
                file = _.split('.')
                if file[-1] == 'mp3' or file[-1] == 'wav':
                    musics_list.append(_)
                    self.music_list.addItem(_)
                    STATUS = False
        else:
            self.music_list.clear()
            self.toggle_button.setText('OFF')
            self.toggle_button.setStyleSheet('QPushButton {\n	color: white;\n	background-color: #cd5c5c;\n}\n\nQPushButton:pressed {\n	background-color: #8b0000;\n}')
            STATUS = True
            global NOW_SELECTED
            NOW_SELECTED = ''
            global music
            music.stop()
    def play_song(self):
        """"
        Blyat rabotai uze
        """
        global music
        music = vlc.MediaPlayer(NOW_SELECTED)
        music.play()


    def selectionChanged(self):
        global NOW_SELECTED
        NOW_SELECTED = self.music_list.selectedItems()[0].text()
        global NOW_PLAYED
        NOW_PLAYED = NOW_SELECTED

    def stop_song(self):
        """"
        Stopped songs
        """
        global music
        music.stop()

    def rand_song(self):
        """
        Randomise it
        """
        global musics_list
        new_list = []
        tmp = True
        while tmp:
            tmp_song = random.choice(musics_list)
            new_list.append(tmp_song)
            musics_list.remove(tmp_song)
            if len(musics_list) == 0:
                break

        musics_list = new_list
        self.music_list.clear()
        for song in musics_list:
            pass

        for _ in musics_list:
            file = _.split('.')
            if file[-1] == 'mp3' or file[-1] == 'wav':
                self.music_list.addItem(_)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    # sys args of program

    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())