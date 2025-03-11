"""
`tree` contains Python syntax parsing functionality and utilities.
It is responsible for building the import dependency graph and
detecting cyclic imports.
"""
import ast


class UnsupportedNodeException(Exception):
    pass


def parse_imports(filename):
    """
    Parses all imports in a given Python file to a common format.

    :return:    a list of dicts, each dict containing information about
                an import.

    Example return:
    [
        {
            "type": "absolute" | "relative",
            "modules": List[str],
            "aliases": None | List[str]
        },
    ]

    NOTE:   this is not mapping from where within the file imports 
            are being made - so calling a circular dependency might
            happen prematurely.
            eventually an additional field will be added with the
            node path the import is originating from.
    """
    with open(filename) as f:
        content = "".join(f.readlines())
        root_node = ast.parse(content)
        import_nodes = [n for n in ast.walk(root_node) if is_import_node(n)]

        return [serialize_import(n) for n in import_nodes]


def is_import_node(node):
    # note: can be changed to a union type ast.Import | ast.ImportFrom
    #       once 3.9 is no longer supported.
    return isinstance(node, (ast.Import, ast.ImportFrom))


def serialize_import(node: ast.AST):
    match node:
        case ast.Import(names):
            return {
                "type": "absolute",
                "module": [a.name for a in names],
                "aliases": None
            }
        case ast.ImportFrom(module, names, level):
            return {
                "type": "absolute" if level == 0 else "relative",
                "module": [module],
                "aliases": [a.name for a in names]
            }
        case _:
            raise UnsupportedNodeException
