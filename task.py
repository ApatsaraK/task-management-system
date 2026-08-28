class Task:
    def __init__(self, task_id, title, priority, due_date):
        self.task_id = task_id  #การสร้าง Attribute
        self.title = title
        self.priority = priority
        self.status = "Pending"
        self.due_date = due_date