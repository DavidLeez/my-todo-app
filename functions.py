FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ read a text file and return the list of to-do items
        filepath get from the txt file from todo_file variable
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


#  print(help(get_todos))  #help on get_todos function


def write_todo(todos_arg, filepath=FILEPATH):
    """ write the todo-items to the file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(help(write_todo))  #help on write_todo function

# print(__name__)
# print("I am outside!!")
if __name__ == "__main__":
    print("hello from function")
    print(get_todos())
