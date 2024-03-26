# coding: utf-8
from ns_architecture.constants import FILE_ENCODING, IMPORT_UNITTEST, SETUP
from ns_architecture.utils import convert_snake_case_to_camel_case
from ns_architecture.management_tests.test_dynamic import TestDynamic


class FileTest:
    def __init__(
        self, list_import_func: list, output_path: str, list_test: list
    ):
        self.content_file = []
        self.output_path = output_path

        self.function_name = list_import_func[-1]
        self.import_module = ".".join(list_import_func[:-1])
        self.list_import_func = list_import_func
        self.list_test = list_test
        self.list_import = []
        self.content_test = []

    def add_break_line_after_lines(self):
        self.content_file = [f"{line}\n" for line in self.content_file]

    def add_break_line(self, list_content: list, nb_break_line: int = 1):
        for i in range(nb_break_line):
            list_content.append(" ")

    def add_header(self):
        self.list_import.append(FILE_ENCODING)
        self.list_import.append(IMPORT_UNITTEST)
        self.list_import.append(
            f"from {self.import_module} import {self.function_name}"
        )
        self.add_break_line(self.list_import, 2)

        # self.content_file.append(add_indentation(SETUP))

    def build_data(self):
        self.add_header()
        test_name = convert_snake_case_to_camel_case(self.function_name)
        self.content_test.append(
            f"class {test_name}TestCase(unittest.TestCase):"
        )
        for test in self.list_test:
            test_dyn = TestDynamic(self.function_name, test, self.list_import)
            self.content_test.extend(test_dyn.create_test())
            self.add_break_line(self.content_test)

        self.content_file.extend(self.list_import)
        self.content_file.extend(self.content_test)

    def write_file(self):
        self.build_data()
        self.add_break_line_after_lines()
        file = open(self.output_path, "w")
        file.writelines(self.content_file)
        file.close()
