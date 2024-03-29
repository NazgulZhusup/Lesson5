class Task2():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description':
            description, "status" : "не выполнено"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "выполнено"
                self.tasks.remove(task)
                print(f"Задача {description} выполнена")


    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")


t = Task2()
t.add_task("02.04.2024","Прочитать книгу")
t.add_task("06.04.2024","Забрать посылку")
t.add_task("09.04.2024","Отправить письмо")

t.show_tasks()

t.complete_tasks("Прочитать книгу")

t.show_tasks()




