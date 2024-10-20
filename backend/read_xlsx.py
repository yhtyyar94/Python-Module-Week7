from openpyxl import load_workbook


def read_xlsx(file_name):
    # Load the .xlsx file
    workbook = load_workbook(filename=file_name)

    # Select the active worksheet
    sheet = workbook.active

    # Accessing a specific cell value
    cell_value = sheet["A1"].value  # Get the value of cell A1

    rows = []

    # Loop through all rows and columns and filter empty rows
    for row in sheet.iter_rows(min_row=1, values_only=True):
        if all(cell is None for cell in row):
            continue
        rows.append(row)
    rows = [list(row) for row in rows]
    return rows
