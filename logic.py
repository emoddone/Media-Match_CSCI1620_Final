import csv
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Make automatically filled places non typable there
        self.selectErr_movie.setReadOnly(True)
        self.selectErr_song.setReadOnly(True)
        self.selectErr_artist.setReadOnly(True)
        self.selectErr_book.setReadOnly(True)
        self.selectErr_author.setReadOnly(True)
        self.rec_movie.setReadOnly(True)
        self.rec_song.setReadOnly(True)
        self.rec_artist.setReadOnly(True)
        self.rec_book.setReadOnly(True)
        self.rec_author.setReadOnly(True)

        # Connect buttons to their respective functions
        self.button_match.clicked.connect(lambda: self.find_match())
        self.button_submit.clicked.connect(lambda: self.submit_new_media())

        # Connect radio buttons to enable/disable
        self.radio_movie.clicked.connect(self.toggle_fields)
        self.radio_song.clicked.connect(self.toggle_fields)
        self.radio_book.clicked.connect(self.toggle_fields)

        # Disable all input fields on start until a media is selected
        self.toggle_fields()

    def toggle_fields(self):
        # Clear all error messages
        self.clear_errors()

        # Clear recommendations
        self.clear_recommendation_fields()

        # Reset all selections
        self.select_movie.setEnabled(False)
        self.select_song.setEnabled(False)
        self.select_artist.setEnabled(False)
        self.select_book.setEnabled(False)
        self.select_author.setEnabled(False)

        # Clear all selections
        self.select_movie.clear()
        self.select_song.clear()
        self.select_artist.clear()
        self.select_book.clear()
        self.select_author.clear()

        # Enable fields based on selection
        if self.radio_movie.isChecked():
            self.select_movie.setEnabled(True)
        elif self.radio_song.isChecked():
            self.select_song.setEnabled(True)
            self.select_artist.setEnabled(True)
        elif self.radio_book.isChecked():
            self.select_book.setEnabled(True)
            self.select_author.setEnabled(True)

    def clear_errors(self):
        # Clear the errors
        error_fields = [
            self.selectErr_movie, self.selectErr_song, self.selectErr_artist,
            self.selectErr_book, self.selectErr_author, self.addErr_movie,
            self.addErr_song, self.addErr_artist, self.addErr_book, self.addErr_author
        ]
        for field in error_fields:
            field.clear()

    def clear_recommendation_fields(self):
        # Clear the recommendation fields
        self.rec_movie.clear()
        self.rec_song.clear()
        self.rec_artist.clear()
        self.rec_book.clear()
        self.rec_author.clear()

    def find_match(self):
        # Find matching media based on input
        self.clear_errors()
        self.clear_recommendation_fields()

        # Get current input values
        movie_input = self.select_movie.text().strip()
        song_input = self.select_song.text().strip()
        artist_input = self.select_artist.text().strip()
        book_input = self.select_book.text().strip()
        author_input = self.select_author.text().strip()

        # Check if any field has input based on selected media type
        has_input = False
        if self.radio_movie.isChecked() and movie_input:
            has_input = True
        elif self.radio_song.isChecked() and (song_input or artist_input):
            has_input = True
        elif self.radio_book.isChecked() and (book_input or author_input):
            has_input = True
        else:
            self.selectErr_movie.setText("Please enter media")

        if not has_input:
            return

        try:
            #look for media matches in the csv
            with open('data.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                match_found = False

                for row in reader:
                    row_values = list(row.values())
                    csv_movie, csv_song, csv_artist, csv_book, csv_author = row_values

                    # Check for matches based on selected media type
                    if self.radio_movie.isChecked() and movie_input:
                        if csv_movie.lower() == movie_input.lower():
                            self.display_match([csv_movie, csv_song, csv_artist, csv_book, csv_author])
                            match_found = True
                            break

                    elif self.radio_song.isChecked() and song_input and artist_input:
                        song_match = not song_input or csv_song.lower() == song_input.lower()
                        artist_match = not artist_input or csv_artist.lower() == artist_input.lower()

                        if song_match and artist_match and (song_input or artist_input):
                            self.display_match([csv_movie, csv_song, csv_artist, csv_book, csv_author])
                            match_found = True
                            break

                    elif self.radio_book.isChecked() and book_input and author_input:
                        book_match = not book_input or csv_book.lower() == book_input.lower()
                        author_match = not author_input or csv_author.lower() == author_input.lower()

                        if book_match and author_match and (book_input or author_input):
                            self.display_match([csv_movie, csv_song, csv_artist, csv_book, csv_author])
                            match_found = True
                            break

                if not match_found:
                    # Show no matches found if no match found
                    if self.radio_movie.isChecked():
                        self.selectErr_movie.setText("No matches found")
                    elif self.radio_song.isChecked():
                        if song_input and not artist_input:
                            self.selectErr_song.setText("Enter Artist")
                        elif artist_input and not song_input:
                            self.selectErr_artist.setText("Enter Song")
                        else:
                            self.selectErr_song.setText("No matches found")
                    elif self.radio_book.isChecked():
                        if book_input and not author_input:
                            self.selectErr_book.setText("Enter Author")
                        elif author_input and not book_input:
                            self.selectErr_author.setText("Enter Book")
                        else:
                            self.selectErr_book.setText("No matches found")

        except FileNotFoundError:
            self.selectErr_movie.setText("Database file not found")
        except Exception as e:
            self.selectErr_movie.setText(f"Error searching: {str(e)}")

    def display_match(self, row_data):
        # Display the matched media recommendation
        if len(row_data) >= 5:
            self.rec_movie.setText(row_data[0])
            self.rec_song.setText(row_data[1])
            self.rec_artist.setText(row_data[2])
            self.rec_book.setText(row_data[3])
            self.rec_author.setText(row_data[4])

    def submit_new_media(self):
        self.clear_errors()

        # Get all input values
        movie = self.new_movie.text().strip()
        song = self.new_song.text().strip()
        artist = self.new_artist.text().strip()
        book = self.new_book.text().strip()
        author = self.new_author.text().strip()

        # Check all inputs are filled
        errors = []
        if not movie:
            self.addErr_movie.setText("Required")
            errors.append("movie")
        if not song:
            self.addErr_song.setText("Required")
            errors.append("song")
        if not artist:
            self.addErr_artist.setText("Required")
            errors.append("artist")
        if not book:
            self.addErr_book.setText("Required")
            errors.append("book")
        if not author:
            self.addErr_author.setText("Required")
            errors.append("author")

        if errors:
            return

        # Check if this combo exists
        try:
            with open('data.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if (row.get('Movie', '').lower() == movie.lower() and
                            row.get('Song', '').lower() == song.lower() and
                            row.get('Book', '').lower() == book.lower()):
                        self.addErr_movie.setText("This combination already exists")
                        return
        except FileNotFoundError:
            pass

        # Add new media match to the csv file
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([movie, song, artist, book, author])

        # Clear input fields after submit
        self.new_movie.clear()
        self.new_song.clear()
        self.new_artist.clear()
        self.new_book.clear()
        self.new_author.clear()

        # Success message
        self.addErr_movie.setText("Successfully added!")