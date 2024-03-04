from diary_module.entry import (Entry)
from diary_module.exception.dairy_is_empty_error import DiaryIsEmptyError
from diary_module.exception.diary_is_locked_exception import DiaryIsLockedError
from diary_module.exception.entry_does_not_exist_error import EntryDoesNotExistError


class Diary:
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.entries = []
        self.number_of_entries = 0
        self.is_locked = False

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def lock_diary(self):
        self.is_locked = True

    def unlock_diary(self):
        self.is_locked = False

    def create_entry(self, title, body):
        if self.is_locked:
            raise DiaryIsLockedError
        else:
            self.number_of_entries += 1
            self.entries.append(Entry(self.number_of_entries, "First Entry", "This is my first entry"))

    def delete_entry(self, i_d):
        if self.is_locked:
            raise DiaryIsLockedError
        elif self.number_of_entries == 0:
            raise DiaryIsEmptyError
        else:
            self.entries.remove(self.find_entry(id))
            self.number_of_entries -= 1

    def find_entry(self, i_d):
        if self.number_of_entries == 0:
            raise DiaryIsEmptyError
        else:
            for entry in self.entries:
                if entry.get_id() is id:
                    return entry
        raise EntryDoesNotExistError

    def update_entry(self, i_d, title, body):
        if self.is_locked:
            raise DiaryIsLockedError
        elif self.number_of_entries == 0:
            raise EntryDoesNotExistError
        else:
            old_entry = self.find_entry(id)
            new_entry = Entry(id, title, body)
            self.entries.remove(old_entry)
            self.entries.append(new_entry)
