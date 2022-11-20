from project.task import Task

class Section:

    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self,new_task:Task):
        for task in self.tasks:
            if new_task.name == task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"


    def complete_task(self, task_name: str):
        for el in self.tasks:
            if el.name == task_name:
                el.completed = True
                return f"Completed task {task_name}"
            return f"Could not find task with the name {self.name}"

    def clean_section(self):
        taskL = len(self.tasks)
        [self.tasks.remove(task) for task in self.tasks if task.completed]
        return f"Cleared {taskL - len(self.tasks)} tasks."

    def view_section(self):
        task_print = f"Section {self.name}"
        for task in self.tasks:
            task_print += f"\n{task.details()}"
        return task_print

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())