class EmployeeRecords:
    def __init__(self):
        self.records = {}

    def add_project(self, employee_id: str, project_name: str) -> bool:
        if employee_id not in self.records:
            self.records[employee_id] = {}
        if project_name in self.records[employee_id]:
            return False
        else:
            self.records[employee_id][project_name] = []
            return True

    def add_task(self, employee_id: str, project_name: str, task: str) -> bool:
        if (
            employee_id not in self.records
            or project_name not in self.records[employee_id]
        ):
            return False
        self.records[employee_id][project_name].append(task)
        return True

    def get_tasks(self, employee_id: str, project_name: str) -> list | None:
        if (
            employee_id not in self.records
            or project_name not in self.records[employee_id]
        ):
            return None
        return self.records[employee_id][project_name]


if __name__ == "__main__":
    records = EmployeeRecords()

    records.add_project("E123", "ProjectA")
    records.add_task("E123", "ProjectA", "Task1")

    print(records.get_tasks("E123", "ProjectA"))
    print(records.get_tasks("E123", "NonExistentProject"))
