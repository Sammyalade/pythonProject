class PhoneBook:
    def __init__(self):
        self.my_dict = {}

    def save_contact(self, name, phone) -> str:
        if name in self.my_dict:
            return 'Contact Already Exist in Contact List'
        else:
            self.my_dict = {name: phone}
            return f'Contact {name} and number {phone} successfully saved'

    def update_contact(self, name, phone):
        if name in self.my_dict:
            self.my_dict[name] = phone
            return f'Updated Contact {name} and Updated number {phone}'
        return f"Contact doesn't exist"

    def delete_contact(self, contact_name) -> str:
        if contact_name in self.my_dict:
            del self.my_dict[contact_name]
            return f'Contact {contact_name} successfully deleted'
        else:
            return f'Contact {contact_name} not found'

    def search_contact_with_name(self, name) -> str:
        if name in self.my_dict:
            return self.my_dict[name]
        else:
            return 'Contact not found'

    def search_contact_with_number(self, number) -> str:
        for name, num in self.my_dict.items():
            if num == number:
                return f'Contact : {name}, Number : {number}'
        return 'Contact not found'

    def main_menu(self):
        user_input = 0
        while user_input != 4:
            print("""
            1. Add new contact
            2. Update contact
            3. Search contact with name
            4. Search contact with number
            5. Delete contact
            6. Exit
            """)
            try:
                user_input = int(input('Enter your choice: '))
                if user_input < 1 or user_input > 6:
                    print('Invalid Input. Please enter a number between 1 and 6')
                    continue
                match user_input:
                    case 1:
                        print("ADD NEW CONTACT")
                        name = input('Enter contact name: ')
                        number = input('Enter contact number: ')
                        print(self.save_contact(name, number))
                    case 2:
                        print("UPDATE CONTACT")
                        name = input('Enter contact name: ')
                        number = input('Enter contact number: ')
                        print(self.update_contact(name, number))
                    case 3:
                        print("SEARCH CONTACT WITH NAME")
                        name = input('Enter contact name to search: ')
                        print(self.search_contact_with_name(name))
                    case 4:
                        print("SEARCH CONTACT WITH NUMBER")
                        number = input('Enter contact number to search: ')
                        print(self.search_contact_with_number(number))
                    case 5:
                        print("DELETE CONTACT")
                        name = input('Enter contact to delete: ')
                        print(self.delete_contact(name))
                    case 6:
                        print('Exiting phonebook now. Thank you for using')
            except ValueError:
                print('Enter an Integer between 1 and 6')


if __name__ == '__main__':
    my_phone_book = PhoneBook()
    my_phone_book.main_menu()
