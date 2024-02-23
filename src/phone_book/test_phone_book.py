import pytest
import phone_book


class TestPhoneBook:
    def test_save_contact(self):
        my_phone_book = phone_book.PhoneBook()
        my_phone_book.save_contact("sammy", "07033675033")
        assert my_phone_book.my_dict["sammy"] == "07033675033"

    def test_delete_contact(self):
        my_phone_book = phone_book.PhoneBook()
        my_phone_book.save_contact("sammy", "07033675033")
        my_phone_book.delete_contact("sammy")
        assert "sammy" not in my_phone_book.my_dict

    def test_search_contact_with_name(self):
        my_phone_book = phone_book.PhoneBook()
        my_phone_book.save_contact("sammy", "07033675033")
        assert my_phone_book.search_contact_with_name("sammy") == "07033675033"

    def test_search_contact_number(self):
        my_phone_book = phone_book.PhoneBook()
        my_phone_book.save_contact("sammy", "07033675033")
        assert my_phone_book.search_contact_with_number("07033675033") == 'Contact : sammy, Number : 07033675033'

    def test_update_contact(self):
        my_phone_book = phone_book.PhoneBook()
        my_phone_book.save_contact("sammy", "07033675033")
        assert my_phone_book.update_contact("sammy", "07017097004") == 'Updated Contact sammy and Updated number 07017097004'

