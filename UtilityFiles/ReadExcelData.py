import openpyxl


class ReadTD:

    @staticmethod
    def getTestData(rowIndex,colIndex):
        workbook=openpyxl.load_workbook(".\\TestData\\Data.xlsx")
        sheet=workbook["Sheet2"]
        cellData=sheet.cell(row=rowIndex,column=colIndex).value
        return cellData

