from pydantic import BaseModel


class Todo(BaseModel):
    name : str
    student_id : str
