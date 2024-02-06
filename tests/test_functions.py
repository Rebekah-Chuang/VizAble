import pytest
import apps.functions as functions

def test_get_file_id():
    """
    Test the `get_file_id()` function. This function generates a `file_id` based on the file format selected by the user. For example, if the user selects ".csv", the returned `file_id` will be "csv_file". Similarly, if ".xlsx" is selected, the returned `file_id` will be "xlsx_file".
    """
    result = functions.get_file_id(".csv")
    assert result == "csv_file"