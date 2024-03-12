import tkinter as ak
from tkinter import simpledialog, messagebox

from diary_module import diaries
from diary_module.diary import Diary


class DiariesMain:

    def __init__(self):
        self.list_of_diaries = diaries.Diaries()

    def main_menu(self):
        root = ak.Tk()
        root.withdraw()

        response = self.take_input("""
           ************************
            Welcome to YoUr DiAry
            1. Add Diary
            2. Add Entry into Diary
            3. Find Diary
            4. Find Entry from Diary
            5. Delete Diary
            6. Delete Entry from Diary
            7. Check number of diary
            8. Exit App
           ************************
        """)

        if response is not None:
            self.match_case(response)

    @staticmethod
    def take_input(display):
        return simpledialog.askstring("Bank App", display)

    def match_case(self, response):
        match response:
            case '1':
                self.add_diary()
            case '2':
                self.add_entry_into_diary()
            case '3':
                self.find_diary()
            case '4':
                self.find_entry_from_diary()
            case '5':
                self.deleteDiary()
            case '6':
                self.delete_entry_from_diary()
            case '7':
                self.check_number_of_diaries()
            case '8':
                self.exit_app()

    def add_diary(self):
        name = self.take_input("Enter Name: ")
        password = self.take_input("Enter Password: ")
        self.list_of_diaries.diaries.add(name, password)
        self.display_message("New Diary Successfully  registered")

    @staticmethod
    def display_message(display):
        messagebox.showinfo(display)

    def add_entry_into_diary(self):
        username = self.take_input("Enter Diary Username: ")
        title = self.take_input("Enter Entry Title: ")
        body = self.take_input("Enter Entry Body: ")
        try:
            diary = self.list_of_diaries.find_diaries(username)
            self.display_message(f"{diary.create_entry(title, body)}")
        except Exception as e:
            self.display_message(f"{e.__repr__()}")

    def find_diary(self):
        username = self.take_input("Enter Diary Username: ")
        try:
            self.display_message(self.list_of_diaries.find_diaries(username))
        except Exception as e:
            self.display_message(f"{e.__repr__()}")
        finally:
            self.main_menu()

    def find_entry_from_diary(self):
        username = self.take_input("Enter Diary Username: ")
        i_d = self.take_input("Enter Entry ID: ")
        try:
            diary: Diary = self.list_of_diaries.find_diaries(username)
            self.display_message(f"{diary.find_entry(i_d)}")
        except Exception as e:
            self.display_message(f"{e.__repr__()}")
        finally:
            self.main_menu()

    def deleteDiary(self):
        username = self.take_input("Enter Diary Username: ")
        password = self.take_input("Enter Diary Password: ")
        try:
            self.list_of_diaries.delete(username, password)
            self.display_message(f"Diary {username} successfully deleted")
        except Exception as e:
            self.display_message(f"{e.__repr__()}")
        finally:
            self.main_menu()

    def delete_entry_from_diary(self):
        username = self.take_input("Enter Diary Username: ")
        entry_id = self.take_input("Enter Entry ID: ")
        try:
            diary: Diary = self.list_of_diaries.find_diaries(username)
            diary.delete_entry(entry_id)
        except Exception as e:
            self.display_message(f"{e.__repr__()}")
        finally:
            self.main_menu()

    def check_number_of_diaries(self):
        self.display_message(f"Number of Diaries is {self.list_of_diaries.numberOfDiaries}")
        self.main_menu()
    @staticmethod
    def exit_app():
        exit(0)



