FILEPATH = "todos.txt"
"""Adding git"""

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todo_local_list = file_local.readlines()
    return todo_local_list


def write_todos(todo_list_arg, filepath=FILEPATH):
    """ Write a  to-do items list int the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list_arg)


if __name__ == "__main__":
    print("Hello from functions.py")
