# cell_text_alignment.py

from openpyxl import Workbook
from openpyxl.styles import Alignment


def center_text(path, horizontal="center", vertical="center"):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Hello"
    sheet["A1"].alignment = Alignment(horizontal=horizontal,
                                      vertical=vertical)
    sheet["A2"] = "from"
    sheet["A3"] = "OpenPyXL"
    sheet["A3"].alignment = Alignment(text_rotation=90)
    workbook.save(path)


if __name__ == "__main__":
    center_text("alignment.xlsx")