from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 715)
        MainWindow.setMinimumSize(QtCore.QSize(515, 715))
        MainWindow.setMaximumSize(QtCore.QSize(515, 715))
        MainWindow.setEnabled(True)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Select Media Group Box
        self.selectMedia = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.selectMedia.setGeometry(QtCore.QRect(10, 0, 491, 231))
        self.selectMedia.setObjectName("selectMedia")

        self.gridLayout = QtWidgets.QGridLayout(self.selectMedia)
        self.gridLayout.setObjectName("gridLayout")

        # Movie selection
        self.radio_movie = QtWidgets.QRadioButton(parent=self.selectMedia)
        self.radio_movie.setObjectName("radio_movie")
        self.gridLayout.addWidget(self.radio_movie, 0, 0, 1, 1)

        self.select_movie = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.select_movie.setObjectName("select_movie")
        self.gridLayout.addWidget(self.select_movie, 0, 1, 1, 2)

        self.selectErr_movie = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.selectErr_movie.setObjectName("selectErr_movie")
        self.gridLayout.addWidget(self.selectErr_movie, 0, 3, 1, 1)

        # Song selection
        self.radio_song = QtWidgets.QRadioButton(parent=self.selectMedia)
        self.radio_song.setObjectName("radio_song")
        self.gridLayout.addWidget(self.radio_song, 1, 0, 1, 1)

        self.select_song = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.select_song.setObjectName("select_song")
        self.gridLayout.addWidget(self.select_song, 1, 1, 1, 2)

        self.selectErr_song = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.selectErr_song.setObjectName("selectErr_song")
        self.gridLayout.addWidget(self.selectErr_song, 1, 3, 1, 1)

        # Artist selection
        self.label_artist_select = QtWidgets.QLabel(parent=self.selectMedia)
        self.label_artist_select.setObjectName("label_artist_select")
        self.gridLayout.addWidget(self.label_artist_select, 3, 1, 1, 1)

        self.select_artist = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.select_artist.setObjectName("select_artist")
        self.gridLayout.addWidget(self.select_artist, 3, 2, 1, 1)

        self.selectErr_artist = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.selectErr_artist.setObjectName("selectErr_artist")
        self.gridLayout.addWidget(self.selectErr_artist, 3, 3, 1, 1)

        # Book selection
        self.radio_book = QtWidgets.QRadioButton(parent=self.selectMedia)
        self.radio_book.setObjectName("radio_book")
        self.gridLayout.addWidget(self.radio_book, 4, 0, 1, 1)

        self.select_book = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.select_book.setObjectName("select_book")
        self.gridLayout.addWidget(self.select_book, 4, 1, 1, 2)

        self.selectErr_book = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.selectErr_book.setObjectName("selectErr_book")
        self.gridLayout.addWidget(self.selectErr_book, 4, 3, 1, 1)

        # Author selection
        self.label_author_select = QtWidgets.QLabel(parent=self.selectMedia)
        self.label_author_select.setObjectName("label_author_select")
        self.gridLayout.addWidget(self.label_author_select, 5, 1, 1, 1)

        self.select_author = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.select_author.setObjectName("select_author")
        self.gridLayout.addWidget(self.select_author, 5, 2, 1, 1)

        self.selectErr_author = QtWidgets.QLineEdit(parent=self.selectMedia)
        self.selectErr_author.setObjectName("selectErr_author")
        self.gridLayout.addWidget(self.selectErr_author, 5, 3, 1, 1)

        # Find Matches button
        self.button_match = QtWidgets.QPushButton(parent=self.selectMedia)
        self.button_match.setObjectName("button_match")
        self.gridLayout.addWidget(self.button_match, 8, 0, 1, 3)

        # Recommendations Group Box
        self.recMedia = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.recMedia.setGeometry(QtCore.QRect(10, 230, 491, 191))
        self.recMedia.setObjectName("recMedia")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.recMedia)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # Movie recommendation
        self.label_movie_3 = QtWidgets.QLabel(parent=self.recMedia)
        self.label_movie_3.setObjectName("label_movie_3")
        self.gridLayout_3.addWidget(self.label_movie_3, 0, 0, 1, 1)

        self.rec_movie = QtWidgets.QLineEdit(parent=self.recMedia)
        self.rec_movie.setObjectName("rec_movie")
        self.gridLayout_3.addWidget(self.rec_movie, 0, 1, 1, 2)

        # Song recommendation
        self.label_song_3 = QtWidgets.QLabel(parent=self.recMedia)
        self.label_song_3.setObjectName("label_song_3")
        self.gridLayout_3.addWidget(self.label_song_3, 1, 0, 1, 1)

        self.rec_song = QtWidgets.QLineEdit(parent=self.recMedia)
        self.rec_song.setObjectName("rec_song")
        self.gridLayout_3.addWidget(self.rec_song, 1, 1, 1, 2)

        # Artist recommendation
        self.label_artist_3 = QtWidgets.QLabel(parent=self.recMedia)
        self.label_artist_3.setObjectName("label_artist_3")
        self.gridLayout_3.addWidget(self.label_artist_3, 3, 1, 1, 1)

        self.rec_artist = QtWidgets.QLineEdit(parent=self.recMedia)
        self.rec_artist.setObjectName("rec_artist")
        self.gridLayout_3.addWidget(self.rec_artist, 3, 2, 1, 1)

        # Book recommendation
        self.label_book_3 = QtWidgets.QLabel(parent=self.recMedia)
        self.label_book_3.setObjectName("label_book_3")
        self.gridLayout_3.addWidget(self.label_book_3, 4, 0, 1, 1)

        self.rec_book = QtWidgets.QLineEdit(parent=self.recMedia)
        self.rec_book.setObjectName("rec_book")
        self.gridLayout_3.addWidget(self.rec_book, 4, 1, 1, 2)

        # Author recommendation
        self.label_author_3 = QtWidgets.QLabel(parent=self.recMedia)
        self.label_author_3.setObjectName("label_author_3")
        self.gridLayout_3.addWidget(self.label_author_3, 5, 1, 1, 1)

        self.rec_author = QtWidgets.QLineEdit(parent=self.recMedia)
        self.rec_author.setObjectName("rec_author")
        self.gridLayout_3.addWidget(self.rec_author, 5, 2, 1, 1)

        # Add New Media Group Box
        self.addMedia = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.addMedia.setGeometry(QtCore.QRect(10, 430, 491, 221))
        self.addMedia.setObjectName("addMedia")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.addMedia)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # New movie
        self.label_movie = QtWidgets.QLabel(parent=self.addMedia)
        self.label_movie.setObjectName("label_movie")
        self.gridLayout_2.addWidget(self.label_movie, 0, 0, 1, 1)

        self.new_movie = QtWidgets.QLineEdit(parent=self.addMedia)
        self.new_movie.setObjectName("new_movie")
        self.gridLayout_2.addWidget(self.new_movie, 0, 1, 1, 2)

        self.addErr_movie = QtWidgets.QLineEdit(parent=self.addMedia)
        self.addErr_movie.setObjectName("addErr_movie")
        self.gridLayout_2.addWidget(self.addErr_movie, 0, 3, 1, 1)

        # New song
        self.label_song = QtWidgets.QLabel(parent=self.addMedia)
        self.label_song.setObjectName("label_song")
        self.gridLayout_2.addWidget(self.label_song, 1, 0, 1, 1)

        self.new_song = QtWidgets.QLineEdit(parent=self.addMedia)
        self.new_song.setObjectName("new_song")
        self.gridLayout_2.addWidget(self.new_song, 1, 1, 1, 2)

        self.addErr_song = QtWidgets.QLineEdit(parent=self.addMedia)
        self.addErr_song.setObjectName("addErr_song")
        self.gridLayout_2.addWidget(self.addErr_song, 1, 3, 1, 1)

        # New artist
        self.label_artist = QtWidgets.QLabel(parent=self.addMedia)
        self.label_artist.setObjectName("label_artist")
        self.gridLayout_2.addWidget(self.label_artist, 3, 1, 1, 1)

        self.new_artist = QtWidgets.QLineEdit(parent=self.addMedia)
        self.new_artist.setObjectName("new_artist")
        self.gridLayout_2.addWidget(self.new_artist, 3, 2, 1, 1)

        self.addErr_artist = QtWidgets.QLineEdit(parent=self.addMedia)
        self.addErr_artist.setObjectName("addErr_artist")
        self.gridLayout_2.addWidget(self.addErr_artist, 3, 3, 1, 1)

        # New book
        self.label_book = QtWidgets.QLabel(parent=self.addMedia)
        self.label_book.setObjectName("label_book")
        self.gridLayout_2.addWidget(self.label_book, 4, 0, 1, 1)

        self.new_book = QtWidgets.QLineEdit(parent=self.addMedia)
        self.new_book.setObjectName("new_book")
        self.gridLayout_2.addWidget(self.new_book, 4, 1, 1, 2)

        self.addErr_book = QtWidgets.QLineEdit(parent=self.addMedia)
        self.addErr_book.setObjectName("addErr_book")
        self.gridLayout_2.addWidget(self.addErr_book, 4, 3, 1, 1)

        # New author
        self.label_author = QtWidgets.QLabel(parent=self.addMedia)
        self.label_author.setObjectName("label_author")
        self.gridLayout_2.addWidget(self.label_author, 5, 1, 1, 1)

        self.new_author = QtWidgets.QLineEdit(parent=self.addMedia)
        self.new_author.setObjectName("new_author")
        self.gridLayout_2.addWidget(self.new_author, 5, 2, 1, 1)

        self.addErr_author = QtWidgets.QLineEdit(parent=self.addMedia)
        self.addErr_author.setObjectName("addErr_author")
        self.gridLayout_2.addWidget(self.addErr_author, 5, 3, 1, 1)

        # Submit button
        self.button_submit = QtWidgets.QPushButton(parent=self.addMedia)
        self.button_submit.setObjectName("button_submit")
        self.gridLayout_2.addWidget(self.button_submit, 6, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Match"))

        # Select Media Group
        self.selectMedia.setTitle(_translate("MainWindow", "Select one media you already like:"))
        self.radio_movie.setText(_translate("MainWindow", "Movie"))
        self.radio_song.setText(_translate("MainWindow", "Song"))
        self.radio_book.setText(_translate("MainWindow", "Book"))
        self.label_artist_select.setText(_translate("MainWindow", "Artist"))
        self.label_author_select.setText(_translate("MainWindow", "Author"))
        self.button_match.setText(_translate("MainWindow", "Find Matches"))

        # Recommendations Group
        self.recMedia.setTitle(_translate("MainWindow",
                                          "                                         Match Recommendations                                       "))
        self.label_movie_3.setText(_translate("MainWindow", "Movie"))
        self.label_song_3.setText(_translate("MainWindow", "Song"))
        self.label_artist_3.setText(_translate("MainWindow", "Artist"))
        self.label_book_3.setText(_translate("MainWindow", "Book"))
        self.label_author_3.setText(_translate("MainWindow", "Author"))

        # Add Media Group
        self.addMedia.setTitle(_translate("MainWindow", "Add New Media Match"))
        self.label_movie.setText(_translate("MainWindow", "Movie"))
        self.label_song.setText(_translate("MainWindow", "Song"))
        self.label_artist.setText(_translate("MainWindow", "Artist"))
        self.label_book.setText(_translate("MainWindow", "Book"))
        self.label_author.setText(_translate("MainWindow", "Author"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())