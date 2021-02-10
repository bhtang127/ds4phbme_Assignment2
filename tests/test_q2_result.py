import subprocess


if __name__ == "__main__":
    res = subprocess.Popen("bash q2.bat", shell=True, stdout=subprocess.PIPE)
    assert int(res.stdout.read()) == 9
