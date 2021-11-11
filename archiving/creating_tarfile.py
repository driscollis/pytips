import tarfile

with tarfile.open("sample.tar", "w") as tar:
    for name in ["foo.txt", "bar.pdf", "baz.xslx"]:
        tar.add(name)