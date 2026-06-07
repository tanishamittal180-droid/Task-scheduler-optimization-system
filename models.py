from dataclasses import dataclass

@dataclass
class Task:
    task_id: str
    task_name: str
    duration: int
    deadline: int
    priority: int
    profit: int