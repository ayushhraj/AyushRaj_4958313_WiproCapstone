import openpyxl


class ExcelUtils:

    @staticmethod
    def get_brand_data():

        workbook = openpyxl.load_workbook(
            "test_data/test_data.xlsx"
        )

        sheet = workbook["BrandFilters"]

        return (
            sheet.cell(2, 1).value,
            sheet.cell(2, 2).value,
            sheet.cell(2, 3).value
        )

    @staticmethod
    def get_price_data():

        workbook = openpyxl.load_workbook(
            "test_data/test_data.xlsx"
        )

        sheet = workbook["PriceFilters"]

        return (
            sheet.cell(2, 1).value,
            sheet.cell(2, 2).value
        )

    @staticmethod
    def get_invalid_price_data():

        workbook = openpyxl.load_workbook(
            "test_data/test_data.xlsx"
        )

        sheet = workbook["InvalidPriceFilters"]

        return (
            sheet.cell(2, 1).value,
            sheet.cell(2, 2).value
        )

    @staticmethod
    def get_invalid_brand_data():

        workbook = openpyxl.load_workbook(
            "test_data/test_data.xlsx"
        )

        sheet = workbook["InvalidBrandFilter"]

        return sheet.cell(2, 1).value

    @staticmethod
    def get_invalid_email_data():

        workbook = openpyxl.load_workbook(
            "test_data/test_data.xlsx"
        )

        sheet = workbook["InvalidEmail"]

        return sheet.cell(2, 1).value