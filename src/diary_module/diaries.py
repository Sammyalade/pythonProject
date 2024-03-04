from diary_module import diary
from diary_module.diary import Diary


class Diaries:

    def __init__(self):
        self.diaries = []
        self.numberOfDiaries = 0

    def add(self, username, password):
        if len(username) == 0:
            raise ValueError("Username is empty")
        self.diaries.append(Diary(username, password))
        self.numberOfDiaries += 1

    def getNumberOfDiaries(self):
        return self.numberOfDiaries

    def delete(self, username, password):
        for file in self.diaries:
            if file.username == username and file.password == password:
                self.diaries.remove(file)
        self.numberOfDiaries -= 1

    def find(self, username):
        for file in self.diaries:
            if file.username == username:
                return file
        raise FileNotFoundError("No such diary")

