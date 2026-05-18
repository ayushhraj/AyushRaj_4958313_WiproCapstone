import openpyxl


class ExcelUtils:

    @staticmethod
    def get_brand_data():

        workbook = openpyxl.load_workbook(
            "test_data/test_data.xlsx"
        )

        sheet = workbook["BrandFilters"]

        samsung = sheet.cell(2, 1).value
        lg = sheet.cell(2, 2).value
        sony = sheet.cell(2, 3).value

        return samsung, lg, sony

    @staticmethod
    def get_price_data():

        workbook = openpyxl.load_workbook(
            "test_data/test_data.xlsx"
        )

        sheet = workbook["PriceFilters"]

        min_price = sheet.cell(2, 1).value
        max_price = sheet.cell(2, 2).value

        return min_price, max_price