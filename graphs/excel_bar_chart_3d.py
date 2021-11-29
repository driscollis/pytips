# bar_chart_3d.py

from openpyxl import Workbook
from openpyxl.chart import BarChart3D, Reference


def create_excel_data(sheet):
    data_rows = [
        ["", "Kindle", "Paperback"],
        ["Python 101", 9.99, 25.99],
        ["Python 201: Intermediate Python", 9.99, 25.99],
        ["wxPython Cookbook", 9.99, 25.99],
        ["ReportLab: PDF Processing with Python", 4.99, 29.99],
        ["Jupyter Notebook 101", 4.99, 29.99],
        ["Creating GUI Applications with wxPython", 24.99, 29.99],
        ["Python Interviews", 24.99, 65.00],
        ["Pillow: Image Processing with Python", 24.99, 69.00],
        ["Automating Excel with Python", 24.99, 69.00],
    ]

    for row in data_rows:
        sheet.append(row)


def create_bar_chart(sheet):
    bar_chart = BarChart3D()
    bar_chart.title = "Book Prices by Type"
    bar_chart.height = 20
    bar_chart.width = 30

    data = Reference(worksheet=sheet,
                     min_row=2,
                     max_row=10,
                     min_col=2,
                     max_col=3)
    titles = Reference(sheet, min_col=1, min_row=2, max_row=10)
    bar_chart.add_data(data, titles_from_data=True)
    bar_chart.set_categories(titles)
    sheet.add_chart(bar_chart, "E2")


def main():
    workbook = Workbook()
    sheet = workbook.active
    create_excel_data(sheet)
    create_bar_chart(sheet)
    workbook.save("bar_chart_3d.xlsx")


if __name__ == "__main__":
    main()