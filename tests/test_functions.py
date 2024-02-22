import pytest
from unittest.mock import patch
from typing import List
import apps.functions as functions
import pandas as pd

def test_get_file_id():
    """
    Test the `get_file_id()` function. This function generates a `file_id` based on the file format selected by the user. For example, if the user selects ".csv", the returned `file_id` will be "csv_file". Similarly, if ".xlsx" is selected, the returned `file_id` will be "xlsx_file".
    """
    assert functions.get_file_id(".csv") == "csv_file"
    assert functions.get_file_id(".tsv") == "tsv_file"
    assert functions.get_file_id(".xlsx") == "xlsx_file"

def test_get_excel_sheet_names():
    """
    Test the `get_excel_sheet_names()` function. This function returns the names of the sheets in an Excel file.
    """
    assert functions.get_excel_sheet_names("tests/test_dataframe/xlsx_example_file.xlsx") == ["Sheet1", "Sheet2", "Sheet3"]

def test_get_excel_sheet_names_invalid():
    """
    Test the `get_excel_sheet_names()` function. This function returns an empty list if the file path is invalid or there is an error reading the file.
    """
    assert functions.get_excel_sheet_names("tests/test_dataframe/invalid_file.xlsx") == []

@pytest.mark.parametrize("plot_type,expected_columns",
                         [
                             ("Line Plot", ["Select an option", "Entity", "Code", "Year", "Users"]),
                             ("Bar Plot", ["Select an option", "Entity", "Code"]),
                             ("Box Plot", ["Select an option", "Year", "Users"]),
                             ("Histogram", ["Select an option", "Year", "Users"]),
                             ("Scatter Plot", ["Select an option", "Year", "Users"])
                         ])

def test_return_choices_for_columns(plot_type, expected_columns):
    """ Test the `return_choices_for_columns()` function. This function returns the expected columns based on the plot type selected by the user.

    :param plot_type: the plot type passed to the function
    :type plot_type: str
    :param expected_columns: the expected columns returned by the function
    :type expected_columns: List[str]
    """
    data_frame = pd.read_csv("tests/test_dataframe/csv_comma_no_quote.csv")
    columns = functions.return_choices_for_columns(data_frame, plot_type=plot_type)
    assert columns == expected_columns

@pytest.mark.parametrize("plot_type, expected_id",
                         [
                             ("Line Plot", "line_y_axis"),
                             ("Bar Plot", "bar_y_axis"),
                             ("Box Plot", "box_y_axis"),
                             ("Histogram", "histogram_y_axis"),
                             ("Scatter Plot", "scatter_y_axis")
                         ])

def test_update_yaxis_input_select(plot_type: str, expected_id: str):
    """ Test the `update_yaxis_input_select()` function. This function updates the y-axis dropdown based on the selected plot type.

    :param plot_type: the plot type passed to the function
    :type plot_type: str
    :param expected_id: the expected id for the updated input select
    :type expected_id: str
    """
    choices = ["col1", "col2", "col3"]

    with patch("apps.functions.ui.update_select") as mock_update_select:
        functions.update_yaxis_input_select(plot_type, choices)
        mock_update_select.assert_called_once_with(id=expected_id, choices=choices, selected=None)