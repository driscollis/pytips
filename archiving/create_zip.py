import pathlib
import zipfile

from typing import List


def create_zip(output_path: str, archive_objects: List[pathlib.Path]):
    with zipfile.ZipFile(output_path, "w") as zip_obj:
        for archive_object in archive_objects:
            zip_obj.write(archive_object,
                          arcname=archive_object.name)

if __name__ == "__main__":
    files_to_archive = [pathlib.Path("fileone_txt"),
                        pathlib.Path("filetwo.txt"),
                        pathlib.Path("filethree.txt")]
    create_zip("my_files.zip", files_to_archive)
