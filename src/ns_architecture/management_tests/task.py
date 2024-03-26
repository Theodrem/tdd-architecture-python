# coding: utf-8
import json
from ns_architecture.management_tests.test_file import FileTest
from ns_architecture.management_tests.utils import get_or_create_test_file


def create_test(json_file: json):
    file = open(json_file)
    content_json = json.load(file)
    base_path = content_json["base"]
    for divide_func in content_json["functions"]:
        path_func = divide_func["path"]
        list_elem_file = path_func.split('.')

        output_path = get_or_create_test_file(base_path, list_elem_file)
        file_test = FileTest(list_elem_file, output_path, divide_func["tests"])
        file_test.write_file()
