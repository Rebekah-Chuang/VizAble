import pytest
import apps.functions as functions

def test_get_file_id():
    result = functions.get_file_id(".csv")
    assert result == "csv_file"