import ast
from methods.for_loop import *

filename = './methods/for_loop.py'
with open(filename) as f:
    tree = ast.parse(f.read())
    print(ast.dump(tree, indent=4))
    print(".....tree end....")
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcName = node.name
            print("node.name", funcName)
        if isinstance(node, ast.For):
            print ("line no. ", node.lineno)
            targetRange = node.iter.args[0].value
            print("node.iter.args.value", targetRange)
