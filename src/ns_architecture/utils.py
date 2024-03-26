# coding: utf-8
from pydoc import locate
from typing import Union


def add_indentation(line: str, nb_indent: int = 1) -> str:
    indent = " " * (4 * nb_indent)
    return f"{indent}{line}"


def convert_snake_case_to_camel_case(file_str: str) -> str:
    # Using to build class name
    temp = file_str.split('_')

    return ''.join(ele.title() for ele in temp)


def check_type_arg(
    type_arg_str: str, arg: str, list_import: Union[str, list] = None
) -> Union[str, None]:
    type_arg = locate(type_arg_str)
    if type_arg:
        new_arg = type_arg(arg)
    else:
        if type_arg_str == "pendulum.Datetime":
            if list_import is not None:
                list_import.insert(1, 'import pendulum')
            new_arg = f'pendulum.parse("{arg}")'
        else:
            return None

    return new_arg


def import_type(list_type: list) -> list:
    format_import = lambda x, y: f"from {x} import {y}"
    dict_import = {
        "pendulum.Datetime": "import pendulum",
        "datetime": format_import("datetime", "datetime"),
        "date": format_import("datetime", "date"),
        "int": None,
        "str": None,
        "list": int,
        "dict": None,
    }
    return [
        dict_import[type_arg]
        for type_arg in list_type
        if dict_import[type_arg]
    ]


def add_break_line_after_lines(content_file: list):
    return [f"{line}\n" for line in content_file]
