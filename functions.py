from typing import NewType, Union

FILEPATH = "todos.txt"


def get_todos(filepath: str = FILEPATH):
    """
    :param filepath: str
    :return: void

    Read a text file and return the list of
    to-do items.
    """

    with open(filepath) as files:
        todos_local: [str] = files.readlines()

    return todos_local


type_write = NewType("type_write", Union[str | list[str]])


def write_todos(argument: type_write, filepath: str = FILEPATH):
    """
    :param argument: str or lis[str]
    :param filepath: str
    :return: void

    Write the to-do items list in the text file
    """

    with open(filepath, 'w') as files:
        files.writelines(argument)
