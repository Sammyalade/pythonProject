from diary_module.diaries import Diaries


class DiariesTest:

    def setup_method(self, method):
        self.diaries = Diaries()

    def test_add_diary_diary_is_added(self):
        self.diaries.add("username", "password")
        assert self.diaries.getNumberOfDiaries() == 1
