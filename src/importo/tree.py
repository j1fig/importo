import ast


def parse_imports(filename):
    with open(filename) as f:
        content = "".join(f.readlines())
        return ast.dump(ast.parse(content))
