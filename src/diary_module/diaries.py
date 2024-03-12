from account_package.exception.InvalidPinError import InvalidPinError
from diary_module.diary import Diary


class Diaries:

    def __init__(self):
        self.diaries = []
        self.numberOfDiaries = 0

    def add(self, username, password):
        for diary_entry in self.diaries:
            if diary_entry.username == username:
                raise ValueError("Username is already taken")
        if len(username) == 0:
            raise ValueError("Username is empty")
        elif len(password) == 0:
            raise ValueError("Password is empty")
        self.diaries.append(Diary(username, password))
        self.numberOfDiaries += 1

    def getNumberOfDiaries(self):
        return self.numberOfDiaries

    def delete(self, username, password):
        diary_to_delete: Diary = self.find_diaries(username)
        if diary_to_delete.get_password() != password:
            raise InvalidPinError("Invalid password")
        else:
            self.diaries.remove(diary_to_delete)
        self.numberOfDiaries -= 1

    def find_diaries(self, username):
        for diary_entry in self.diaries:
            if diary_entry.username == username:
                return diary_entry
        raise ValueError("No such diary")
