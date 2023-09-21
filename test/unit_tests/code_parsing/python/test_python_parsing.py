import ast
from os.path import join, dirname
import pprint

module_filename = join(dirname(__file__), "code_example", "module1.py")

with open(module_filename, "r") as file:
    module_source_code = file.read()

module_ast = ast.parse(module_source_code)

pprint(ast.dump(module_ast))
