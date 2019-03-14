"""
    pyexcel_xlsbr.xlsbr
    ~~~~~~~~~~~~~~~~~~~
    The lower level xlsb file format handler
    :copyright: (c) 2018 by Onni Software Ltd & its contributors
    :license: New BSD License
"""
from pyexcel_io._compact import OrderedDict
from pyexcel_io.book import BookReader
from pyexcel_io.sheet import SheetReader
from pyxlsb import open_workbook


class XLSBSheet(SheetReader):
    def __init__(
        self,
        sheet,
        auto_detect_int=True,
        auto_detect_float=True,
        auto_detect_datetime=True,
        **keywords
    ):
        SheetReader.__init__(self, sheet, **keywords)
        self.__auto_detect_int = auto_detect_int
        self.__auto_detect_float = auto_detect_float
        self.__auto_detect_datetime = auto_detect_datetime

    @property
    def name(self):
        return self._native_sheet.name

    def row_iterator(self):
        return self._native_sheet.rows()

    def column_iterator(self, row):
        for cell in row:
            yield self.__convert_cell(cell)

    def __convert_cell(self, cell):
        return cell.v


class XLSBBook(BookReader):
    def open(self, file_name, **keywords):
        BookReader.open(self, file_name, **keywords)
        self._load_from_file()

    def read_sheet_by_name(self, sheet_name):
        sheet = self._native_book.get_sheet(sheet_name)
        sheet.name = sheet_name
        return self.read_sheet(sheet)

    def read_sheet_by_index(self, sheet_index):
        sheet = self._native_book.get_sheet(sheet_index)
        sheet.name = self._native_book.sheets[sheet_index]
        return self.read_sheet(sheet)

    def read_all(self):
        result = OrderedDict()
        for sheet_name in self._native_book.sheets:
            sheet = self._native_book.get_sheet(sheet_name)
            sheet.name = sheet_name
            xlsb_sheet = XLSBSheet(sheet, **self._keywords)
            result[xlsb_sheet.name] = xlsb_sheet.to_array()
        return result

    def read_sheet(self, native_sheet):
        sheet = XLSBSheet(native_sheet, **self._keywords)
        return {sheet.name: sheet.to_array()}

    def _load_from_file(self):
        self._native_book = open_workbook(self._file_name)
