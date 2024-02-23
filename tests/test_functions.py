import pytest
from unittest.mock import patch
from typing import List
import apps.functions as functions
import pandas as pd

@pytest.mark.parametrize("file_extension_str, expected_id, expected_accept",
                         [
                             (".csv", "csv_file", [".csv"]),
                             (".tsv", "tsv_file", [".tsv"]),
                             (".xlsx", "xlsx_file", [".xlsx"])
                         ])

def test_input_file(file_extension_str: str, expected_id: str, expected_accept: List[str]):
    """ Test the `input_file()` function. This function creates a file input for users to upload a file.

    :param file_extension_str: File extension string, e.g., ".csv", ".tsv", ".xlsx".
    :type file_extension_str: str
    :param expected_id: Expected id for different file extensions, e.g., "csv_file", "tsv_file", "xlsx_file".
    :type expected_id: str
    :param expected_accept: Expected accept list for different file extensions, e.g., [".csv"], [".tsv"], [".xlsx"].
    :type expected_accept: List[str]
    """
    with patch("apps.functions.ui.input_file") as mock_input_file:
        functions.input_file(file_extension_str)
        mock_input_file.assert_called_once_with(id=expected_id,
                                                label="",
                                                accept=expected_accept,
                                                multiple=False)

def test_get_file_id():
    """ Test the `get_file_id()` function. This function generates a `file_id` based on the file format selected by the user. For example, if the user selects ".csv", the returned `file_id` will be "csv_file". Similarly, if ".xlsx" is selected, the returned `file_id` will be "xlsx_file".
    """
    assert functions.get_file_id(".csv") == "csv_file"
    assert functions.get_file_id(".tsv") == "tsv_file"
    assert functions.get_file_id(".xlsx") == "xlsx_file"

def test_get_excel_sheet_names():
    """ Test the `get_excel_sheet_names()` function. This function returns the names of the sheets in an Excel file.
    """
    assert functions.get_excel_sheet_names("tests/test_dataframe/xlsx_example_file.xlsx") == ["Sheet1", "Sheet2", "Sheet3"]

def test_get_excel_sheet_names_invalid():
    """ Test the `get_excel_sheet_names()` function. This function returns an empty list if the file path is invalid or there is an error reading the file.
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

def test_return_choices_for_columns(plot_type: str, expected_columns: List[str]):
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
                             ("Line Plot", "line_x_axis"),
                             ("Bar Plot", "bar_x_axis"),
                             ("Box Plot", "box_x_axis"),
                             ("Histogram", "histogram_x_axis"),
                             ("Scatter Plot", "scatter_x_axis")
                         ])

def test_update_xaxis_input_select(plot_type: str, expected_id: str):
    """ Test the `update_xaxis_input_select()` function. This function updates the x-axis dropdown based on the selected plot type.

    :param plot_type: the plot type passed to the function
    :type plot_type: str
    :param expected_id: the expected id for the updated input select
    :type expected_id: str
    """
    choices = ["col1", "col2", "col3"]

    with patch("apps.functions.ui.update_select") as mock_update_select:
        functions.update_xaxis_input_select(plot_type, choices)
        mock_update_select.assert_called_once_with(id=expected_id, choices=choices, selected=None)

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