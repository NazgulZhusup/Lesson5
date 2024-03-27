# создайте класс Product для управления товарами в магазине.  Каждый товар должен иметь
# название, категорию, стоимость и количество на складе.  Реализуйте методы для изменения
# количества товаров на складе (при продаже и поставке товара) и выводе информации о товаре

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_quantity(self, change):
        """Изменяет количество на складе. Положительное значение для поставки, отрицательное для продажи."""
        self.quantity += change

    def display_info(self):
        """Выводит информацию о продукте."""
        print(f"{self.name} ({self.category}) - {self.quantity} шт. по цене {self.price} за шт.")

class ProductManager:
    def __init__(self):
        self.products_by_category = {}

    def add_product(self, name, category, price, quantity):
        product = Product(name, category, price, quantity)
        if category not in self.products_by_category:
            self.products_by_category[category] = []
        self.products_by_category[category].append(product)

    def remove_product(self, name, category):
        if category in self.products_by_category:
            self.products_by_category[category] = [product for product in self.products_by_category[category] if product.name != name]
            if not self.products_by_category[category]:  # Если список продуктов в категории пуст, удаляем категорию
                del self.products_by_category[category]

    def get_all_products(self):
        print("В данное время на складе имеются следующие товары по категориям:")
        for category, products in self.products_by_category.items():
            print(f"Категория: {category}")
            for product in products:
                product.display_info()

# Пример использования
product_manager = ProductManager()
product_manager.add_product("Кольцо", "Бижутерия", 230, 150)
product_manager.add_product("Ожерелье", "Бижутерия", 1500, 150)
product_manager.add_product("Браслет", "Бижутерия", 850, 300)
product_manager.add_product("Чайный набор", "Посуда", 5000, 50)

product_manager.get_all_products()

# Удаление продукта
product_manager.remove_product("Браслет", "Бижутерия")
product_manager.get_all_products()



