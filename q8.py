class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def status_logger(update_status):
        def wrapper(self, new_status):
            old_status = self.status
            update_status(self, new_status)
            print(
                f"Status of Task '{self.name}' changed from '{old_status}' to '{new_status}'"
            )

        return wrapper

    @status_logger
    def update_status(self, new_status):
        self.status = new_status


task1 = Task("Task 1", "To Do")
task1.update_status("In Progress")
task1.update_status("Done")
