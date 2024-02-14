from .barcode_handler import BarcodeHandler


def test_create_barcode():
    barcode_handler = BarcodeHandler()

    result = barcode_handler.create_barcode("testando")

    assert result == "testando"
