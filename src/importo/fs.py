import os


IGNORED_DIRS = set([
    ".hg", ".svn", ".git", ".tox", "__pycache__", "env", "venv", ".ruff_cache", "dist", ".pytest_cache"
])


def list_py(path: str, recursive: bool = True):
    root_path = resolve_to_absolute_path(path)
    all_dirs = list(os.walk(root_path))
    filtered_dirs = [f for f in all_dirs if not has_ignored_dir(f[0])]

    py_files = [
        os.path.join(dirpath, filename)
        for dirpath, dirnames, filenames in filtered_dirs
        for filename in filenames
        if filename.endswith(".py")
    ]
    return py_files


def resolve_to_absolute_path(path):
    return os.path.abspath(os.path.expanduser(os.path.expandvars(path)))


def has_ignored_dir(dirpath):
    return any(i in dirpath for i in IGNORED_DIRS)
