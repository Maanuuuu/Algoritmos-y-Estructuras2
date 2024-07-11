

class Tarea:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
        self.next = None  # For linked list

class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        if not self.head:
            self.head = task
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = task

    def list_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append({'id': current.id, 'name': current.name, 'status': current.status})
            current = current.next
        return tasks
    
    def display_sprint_info(self):
        print(f"Sprint ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Status: {self.status}")
        print(f"Objectives: {self.objectives}")
        print(f"Team: {self.team}")
        print("Tasks:")
        tasks = self.tasks.list_tasks()
        if not tasks:
            print("  No tasks assigned.")
        for task in tasks:
            print(f"  ID: {task['id']}, Name: {task['name']}, Status: {task['status']}")

class Sprint:
    def __init__(self, id, name, start_date, end_date, status, objectives, team):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.objectives = objectives
        self.team = team
        self.tasks = LinkedList()
        self.height = 1  # Para el balance del arbol

# Crear un sprint
sprint = Sprint(id=1, name="Sprint 1", start_date="2023-04-01", end_date="2023-04-15", status="Active", objectives="Complete the project", team="Team A")

# Añadir tareas al sprint
sprint.tasks.add_task(Tarea(id=101, name="Task 1", status="Not Started"))
sprint.tasks.add_task(Tarea(id=102, name="Task 2", status="In Progress"))
sprint.tasks.add_task(Tarea(id=103, name="Task 3", status="Completed"))

# Método para mostrar la información del sprint y sus tareas
def display_sprint_info(sprint):
    print(f"Sprint ID: {sprint.id}")
    print(f"Name: {sprint.name}")
    print(f"Start Date: {sprint.start_date}")
    print(f"End Date: {sprint.end_date}")
    print(f"Status: {sprint.status}")
    print(f"Objectives: {sprint.objectives}")
    print(f"Team: {sprint.team}")
    print("Tasks:")
    tasks = sprint.tasks.list_tasks()
    if not tasks:
        print("  No tasks assigned.")
    for task in tasks:
        print(f"  ID: {task['id']}, Name: {task['name']}, Status: {task['status']}")

# Mostrar la información del sprint y sus tareas
display_sprint_info(sprint)