class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для товаров

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание магазинов
store1 = Store("Happy Fruits", "123 Green Street")
store2 = Store("Daily Needs", "456 Main Road")
store3 = Store("Tech Gadgets", "789 Tech Park")

# Добавление товаров
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("milk", 1.5)
store2.add_item("bread", 1.0)

store3.add_item("keyboard", 20.0)
store3.add_item("mouse", 10.0)

# Тестирование добавления товара
store1.add_item("oranges", 0.8)
print(store1.items)  # Должен показать apples, bananas и oranges

# Тестирование обновления цены товара
store1.update_price("apples", 0.55)
print(store1.get_item_price("apples"))  # Должен показать 0.55

# Тестирование удаления товара
store1.remove_item("bananas")
print(store1.items)  # Должен показать apples и oranges, но без bananas

# Тестирование получения цены товара
print(store1.get_item_price("milk"))  # Должен вернуть None, так как milk нет в ассортименте

