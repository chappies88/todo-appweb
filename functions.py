FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todo_varg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_varg)


if __name__ == "__main__":
    todos = get_todos()
    print(todos)