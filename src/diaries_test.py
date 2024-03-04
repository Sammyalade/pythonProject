import pytest

from diary_module.diaries import Diaries
from diary_module.diary import Diary


def test_add_diaries():
    diaries = Diaries()
    diaries.add("username", "password")
    assert diaries.getNumberOfDiaries() == 1


def test_delete_diaries():
    diaries = Diaries()
    diaries.add("username", "password")
    diaries.delete("username", "password")
    assert diaries.getNumberOfDiaries() == 0


def test_find_diaries_by_username():
    diaries = Diaries()
    diaries.add("username", "password")
    assert isinstance(diaries.find("username"), Diary)


def test_delete_diaries_find_diaries_raises_file_not_found_error():
    diaries = Diaries()
    diaries.add("username", "password")
    diaries.add("username1", "password1")
    diaries.delete("username1", "password1")
    with pytest.raises(FileNotFoundError):
        assert diaries.find("username1")
