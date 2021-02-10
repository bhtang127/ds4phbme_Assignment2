import codecs
import re


if __name__ == "__main__":
    html = codecs.open("chewie.html", "r", "utf-8")
    f = html.read()
    title = re.compile("<title>Chewbacca - Wikipedia</title>")
    sent = re.compile("Chewbacca, a 200-year-old")
    ep2 = re.compile("Episode II – Attack of the Clones")

    assert len(title.findall(f)) > 0
    assert len(sent.findall(f)) > 0
    assert len(ep2.findall(f)) > 0
