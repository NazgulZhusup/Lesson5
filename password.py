# Создайте класс User с атрибутами username, email, и password.
# Реализуйте метод change_password(old_password, new_password), который позволяет пользователю изменить свой пароль. Убедитесь, что старый пароль введен правильно, прежде чем установить новый.
# Добавьте метод display_user_info(), который выводит информацию о пользователе.
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("The old password is incorrect. Password change failed.")

    def display_user_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Password: {'*' * len(self.password)}")  # Не показываем пароль напрямую

# Пример использования
user1 = User("john_doe", "john@example.com", "password123")
user1.display_user_info()

# Попытка изменения пароля с неправильным старым паролем
user1.change_password("wrongpassword", "newpassword123")

# Успешное изменение пароля
user1.change_password("password123", "newpassword123")
user1.display_user_info()
