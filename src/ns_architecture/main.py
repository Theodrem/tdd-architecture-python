# coding: utf-8
import os
import json
from pathlib import Path
from ns_architecture.management_tests.test_file import FileTest
from ns_architecture.utils import (
    import_type,
    add_break_line_after_lines,
    add_indentation,
)
from ns_architecture.constants import FILE_ENCODING


def parse_func(args: list, function_name: str):
    content_file = [FILE_ENCODING]
    args_line = []
    for arg in args:
        type_args = arg["type_arg"].split(",")
        is_import = import_type(type_args)
        if is_import:
            content_file.extend(is_import)

        if len(type_args) > 1:
            type_arg = f"Union{[type_arg for type_arg in type_args]}"
        else:
            type_arg = type_args[0]

        args_line.append(f"{arg['name']}: {type_arg}")
    content_file.append(f"def {function_name}({','.join(args_line)}):")
    content_file.append(add_indentation("pass"))
    return content_file


def get_or_create_divide_func(list_elem_file_path: list, base_path: str, args):
    file = list_elem_file_path[-2]
    path_wo_file = f"{base_path}/{'/'.join(list_elem_file_path[:-2])}"
    print(path_wo_file)
    if not Path(path_wo_file).exists():
        os.mkdir(path_wo_file)
        Path(f"{path_wo_file}/__init__.py").touch()

    file_func = Path(f"{path_wo_file}/{file}.py")
    if not file_func.exists():
        file_func.touch()
    print("ALEr")
    print(args)
    content = parse_func(args=args, function_name=list_elem_file_path[-1])
    content_formatted = add_break_line_after_lines(content)
    print(content_formatted)
    file = open(file_func, "a")
    file.writelines(content_formatted)
    file.close()


def get_or_create_test_file(list_elem_file_path: list, base_path: str):
    function_name = list_elem_file_path[-1]
    if len(list_elem_file_path) >= 3:
        module_name = list_elem_file_path[-3]

        path_module_str = f"{base_path}/tests/tests_{module_name}"
        if not Path(path_module_str).exists():
            os.mkdir(path_module_str)
        init = Path(f"{path_module_str}/__init__.py")
        if not init.exists():
            init.touch()
        full_path_str = f"{path_module_str}/test_{function_name}.py"
    else:
        full_path_str = f"{base_path}/tests/test_{function_name}.py"

    full_path = Path(full_path_str)

    if not full_path.exists():
        full_path.touch()
    return full_path


def create_test(json_file: json):
    file = open(json_file)
    content_json = json.load(file)
    for divide_func in content_json:
        base = divide_func["base"]
        base_path = base.replace(".", "/")
        path = divide_func["path"]
        list_elem_file = path.split('.')
        get_or_create_divide_func(
            list_elem_file, base_path, divide_func["args"]
        )

        output_path = get_or_create_test_file(list_elem_file, base_path)
        file_test = FileTest(list_elem_file, output_path, divide_func["tests"])
        file_test.write_file()


def create_function():
    # TODO
    pass
