"""
    pyexcel_xlsbr.xlsbr
    ~~~~~~~~~~~~~~~~~~~
    The lower level xlsb file format handler
    :copyright: (c) 2018-2020 by Onni Software Ltd & its contributors
    :license: New BSD License
"""
from pyexcel_io.plugin_api import IReader, ISheet, NamedContent
from pyxlsb import open_workbook


class XLSBSheet(ISheet):
    def __init__(
        self,
        sheet,
        auto_detect_int=True,
        auto_detect_float=True,
        auto_detect_datetime=True,
    ):
        self.__auto_detect_int = auto_detect_int
        self.__auto_detect_float = auto_detect_float
        self.__auto_detect_datetime = auto_detect_datetime
        self._native_sheet = sheet

    def row_iterator(self):
        return self._native_sheet.rows()

    def column_iterator(self, row):
        for cell in row:
            yield self.__convert_cell(cell)

    def __convert_cell(self, cell):
        return cell.v


class XLSBBook(IReader):
    def __init__(self, file_name, file_type, **keywords):
        self._native_book = open_workbook(file_name)
        self._keywords = keywords
        self.content_array = []
        for sheet_index, sheet_name in enumerate(self._native_book.sheets, 1):
            sheet = self._native_book.get_sheet(sheet_index)
            self.content_array.append(NamedContent(sheet_name, sheet))

    def read_sheet(self, sheet_index):
        native_sheet = self.content_array[sheet_index].payload
        sheet = XLSBSheet(native_sheet, **self._keywords)
        return sheet

    def close(self):
        self._native_book.close()
