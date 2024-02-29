import pytest

from diary_module import diary
from diary_module.entry import Entry
from diary_module.exception.dairy_is_empty_error import DiaryIsEmptyError
from diary_module.exception.diary_is_locked_exception import DiaryIsLockedError
from diary_module.exception.entry_does_not_exist_error import EntryDoesNotExistError


class TestDiary:

    def test_unlock_diary_diary_is_unlocked(self):
        my_diary = diary.Diary()
        assert my_diary.is_locked is False

    def test_lock_diary_is_locked(self):
        my_diary = diary.Diary()
        my_diary.lock_diary()
        assert my_diary.is_locked is True

    def test_lock_diary_unlock_diary_and_lock_diary(self):
        my_diary = diary.Diary()
        my_diary.lock_diary()
        assert my_diary.is_locked is True
        my_diary.unlock_diary()
        assert my_diary.is_locked is False

    def test_create_entry_number_of_entry_is_one(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is my first entry")

        assert my_diary.number_of_entries == 1

    def test_add_entry_and_delete_it_number_of_entries_is_zero_test(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is my first entry")

        my_diary.delete_entry()

        assert my_diary.number_of_entries == 0

    def test_create_entry_when_diary_is_locked_throws_diary_is_locked_error(self):
        my_diary = diary.Diary()
        my_diary.lock_diary()
        assert my_diary.is_locked is True

        with pytest.raises(DiaryIsLockedError):
            my_diary.create_entry("First Entry", "This is my first entry")

    def test_create_entry_and_lock_entry_delete_entry_throws_diary_is_locked_error(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is my first entry")
        my_diary.lock_diary()

        with pytest.raises(DiaryIsLockedError):
            my_diary.delete_entry()

    def test_add_entry_find_entry_when_diary_is_unlocked_returns_entry(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is my first entry")

        my_entry = my_diary.find_entry(1)

        assert isinstance(my_entry, Entry)

    def test_add_entry_update_entry_when_diary_is_unlocked_dairy_updated(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is my first entry")
        my_diary.update_entry(1, "First Entry", "This is the updated entry")

        updated_entry = my_diary.find_entry(1)

        assert updated_entry.get_body() == "This is the updated entry"

    def test_add_entry_update_entry_when_diary_is_locked_throws_diary_is_locked_exception(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is my first entry")
        my_diary.lock_diary()

        with pytest.raises(DiaryIsLockedError):
            my_diary.update_entry(1, "First Entry", "This is the updated entry")

    def test_delete_entry_in_diary_when_it_is_empty_throws_entry_is_empty_exception(self):
        my_diary = diary.Diary()

        with pytest.raises(DiaryIsEmptyError):
            my_diary.delete_entry()

    def test_find_entry_when_entry_is_empty_throws_entry_is_empty_exception(self):
        my_diary = diary.Diary()
        with pytest.raises(DiaryIsEmptyError):
            my_diary.find_entry(1)

    def test_add_two_entries_find_entry_that_does_not_exist_throws_entry_does_not_exist_exception(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is my first entry")
        my_diary.create_entry("Second Entry", "This is my second entry")

        with pytest.raises(EntryDoesNotExistError):
            my_diary.find_entry(100)

    def test_delete_entry_find_entry_that_was_deleted_throws_entry_does_not_exist_exception(self):
        my_diary = diary.Diary()
        my_diary.create_entry("First Entry", "This is first entry")
        my_diary.create_entry("Second Entry", "This is my second entry")
        my_diary.delete_entry()
        with pytest.raises(EntryDoesNotExistError):
            my_diary.find_entry(1)

   # def test_delete_entry_that_does_not_exist_throws_entry_does_not_exist_exception(self):
    #    my_diary = diary.Diary()
     #   my_diary.create_entry("First Entry", "This is first entry")
      #  my_diary.create_entry("Second Entry", "This is my second entry")
       # my_diary.delete_entry()
        #with pytest.raises(EntryDoesNotExistError):
          #  my_diary.find_entry(1)
