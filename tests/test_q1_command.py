import codecs
import re


if __name__ == "__main__":
    f = codecs.open("q1.bat", "r", "utf-8").read()
    command1 = re.compile("wget")
    command2 = re.compile("curl")
    command3 = re.compile("web")
    html = re.compile("en.wikipedia.org/wiki/Chewbacca")
    assert len(command1.findall(f)) + len(command2.findall(f)) + len(command3.findall(f)) > 0
    assert len(html.findall(f)) > 0
