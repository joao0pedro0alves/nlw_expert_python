from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    def create_barcode(self, code: str) -> str:
        barcode = Code128(code, writer=ImageWriter())
        path_from_barcode = self.__create_path_from_barcode(barcode)
        barcode.save(path_from_barcode)

        return path_from_barcode

    def __create_path_from_barcode(self, barcode: str) -> str:
        path_from_barcode = f"tmp/barcodes/{barcode}"
        return path_from_barcode
