def serializer(todo) -> dict:
    return {
        "id"    : str(todo["_id"]),
        "name" : todo["name"],
        "student_id"  : todo["student_id"]
    }


def todos_serializers(todos) -> list:
    return [serializer(todo) for todo in todos]    