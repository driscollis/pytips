import tarfile

tar = tarfile.open("sample.tar.gz")
tar.extractall()
tar.close()