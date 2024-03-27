class Contact:
    def __init__(self, firstname, lastname, mobile, email):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.email = email

class ContactsManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, firstname, lastname, mobile, email):
        contact = Contact(firstname, lastname, mobile, email)
        self.contacts.append(contact)

    def delete_contact(self, firstname, lastname):
        self.contacts = [contact for contact in self.contacts if contact.firstname != firstname or contact.lastname != lastname]

    def find_contact(self, firstname):
        found_contacts = [contact for contact in self.contacts if contact.firstname == firstname]
        return found_contacts

    def display_contacts(self):
        for contact in self.contacts:
            print(f"{contact.firstname} {contact.lastname}, Mobile: {contact.mobile}, Email: {contact.email}")


# Создаем экземпляр менеджера контактов
contacts_manager = ContactsManager()

# Добавляем контакты
contacts_manager.add_contact("John", "Doe", "123456789", "john.doe@example.com")
contacts_manager.add_contact("Jane", "Doe", "987654321", "jane.doe@example.com")
contacts_manager.add_contact("Mike", "Smith", "555444666", "mike.smith@example.com")

# Выводим все контакты после добавления
print("Контакты после добавления:")
contacts_manager.display_contacts()

# Удаляем один контакт
contacts_manager.delete_contact("Jane", "Doe")

# Выводим все контакты после удаления
print("\nКонтакты после удаления Jane Doe:")
contacts_manager.display_contacts()









