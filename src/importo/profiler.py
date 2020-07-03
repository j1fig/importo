import subprocess


def profile(module, iterations):
    profiles = []
    for _ in range(iterations):
        cmd = ["python", "-X", "importtime", "-m", module]
        p = subprocess.run(cmd, capture_output=True)
        profiles.append(p.stderr.decode("utf-8").split("\n"))
    return profiles
