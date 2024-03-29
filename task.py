# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач

class Task():
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):

        self.is_completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):

        self.tasks.append(Task(description, due_date))

    def mark_task_completed(self, description):

        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                break

    def get_current_tasks(self):

        return [task.description for task in self.tasks if not task.is_completed]


task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2024-03-30")
task_manager.add_task("Оплатить счета", "2024-04-05")
task_manager.add_task("Забрать посылку", "2024-05-06")
task_manager.add_task("Заполнить форму для отчета", "2024-06-07")


task_manager.mark_task_completed("Купить продукты")


current_tasks = task_manager.get_current_tasks()
print(current_tasks)
