import subprocess


def profile(module, parallelism):
    cmd = ["python", "-X", "importtime", "-m" , module]
    p = subprocess.run(cmd, capture_output=True)
    return p.stderr.decode('utf-8').split('\n')
