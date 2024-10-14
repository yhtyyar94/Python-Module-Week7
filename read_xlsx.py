from openpyxl import load_workbook


def read_xlsx(file_name):
    # Load the .xlsx file
    workbook = load_workbook(filename=file_name)

    # Select the active worksheet
    sheet = workbook.active

    # Accessing a specific cell value
    cell_value = sheet["A1"].value  # Get the value of cell A1
    print(f"Value of A1: {cell_value}")

    rows = []

    # Loop through all rows and columns
    for row in sheet.iter_rows(min_row=1, values_only=True):
        print(row)  # Tuple of values in the row
        rows.append(row)
    return rows
