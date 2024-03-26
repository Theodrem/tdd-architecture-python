# coding: utf-8
import os
from pathlib import Path


def get_or_create_test_file(base_path: str, list_elem_file_path: list) -> str:
    function_name = list_elem_file_path[-1]
    project_name = list_elem_file_path[0]
    base = f"{base_path}/{project_name}"
    if len(list_elem_file_path) >= 4:
        module_name = list_elem_file_path[-3]

        path_module_str = f"{base}/tests/tests_{module_name}"
        if not Path(path_module_str).exists():
            os.mkdir(path_module_str)
        init = Path(f"{path_module_str}/__init__.py")
        if not init.exists():
            init.touch()
        full_path_str = f"{path_module_str}/test_{function_name}.py"
    else:
        full_path_str = f"{base}/tests/test_{function_name}.py"

    full_path = Path(full_path_str)

    if not full_path.exists():
        full_path.touch()
    return full_path
