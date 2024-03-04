class Diaries:

    def __init__(self):
        self.numberOfDiaries = 0

    def add(self, username, password):
        self.numberOfDiaries += 1

    def getNumberOfDiaries(self):
        return self.numberOfDiaries

    def delete(self, param, param1):
        self.numberOfDiaries -= 1

