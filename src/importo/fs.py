import os


IGNORED_DIRS = set([
    ".hg", ".svn", ".git", ".tox", "__pycache__", "env", "venv", ".ruff_cache", "dist", ".pytest_cache"
])


def list_py(path: str, recursive: bool = True):
    root_path = resolve_to_absolute_path(path)
    all_files = list(os.walk(root_path))
    py_files = [f for f in all_files if not has_ignored_dir(f[0])]
    return py_files


def resolve_to_absolute_path(path):
    return os.path.abspath(os.path.expanduser(os.path.expandvars(path)))


def has_ignored_dir(dirpath):
    return any(i in dirpath for i in IGNORED_DIRS)
