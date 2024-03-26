# coding: utf-8
from ns_architecture.utils import add_indentation, check_type_arg


class TestDynamic:
    def __init__(self, function_name, dict_test: list, list_import):
        self.function_name = function_name
        self.dict_test = dict_test
        self.list_content_test = []
        self.suffix = dict_test["suffix"]
        self.list_import = list_import

        self.result = check_type_arg(
            type_arg_str=dict_test["result"]["type_arg"],
            arg=dict_test["result"]["arg"],
        )

    def parse_args(self):
        args_dic_test = self.dict_test["args"]
        for arg_name in args_dic_test:
            type_arg_str = args_dic_test[arg_name]["type_arg"]
            arg_value = args_dic_test[arg_name]["arg"]
            new_arg = check_type_arg(
                type_arg_str=type_arg_str,
                arg=arg_value,
                list_import=self.list_import,
            )
            yield f"{arg_name} = {new_arg}"

    def create_test(self):
        func_test_name = f"test_{self.function_name}_{self.suffix}"
        formatted_func = add_indentation(f"def {func_test_name}")
        self.list_content_test.append(f"{formatted_func}(self):")
        exp_res = add_indentation(f"expected_result = {self.result}", 2)
        self.list_content_test.append(exp_res)
        for i in self.parse_args():
            formatted_line = add_indentation(i, 2)
            self.list_content_test.append(formatted_line)

        list_formatted_args = [
            f"{arg}={arg}" for arg in self.dict_test["args"]
        ]
        format_args = ", ".join(list_formatted_args)

        result_func = add_indentation(
            f"resp = {self.function_name}({format_args})", 2
        )
        self.list_content_test.append(result_func)
        assert_eq = 'self.assertEqual(expected_result, resp)'
        self.list_content_test.append(add_indentation(assert_eq, 2))
        return self.list_content_test
