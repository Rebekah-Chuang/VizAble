# poetry run pytest (run this at root directory of the project to test the functions when poetry shell is activated)
from shiny import ui, render, App, Inputs, Outputs, Session, reactive
import pytest
from unittest.mock import patch
from typing import List
import VizAble.functions as functions
import pandas as pd

# Test input_file()
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
    with patch("VizAble.functions.ui.input_file") as mock_input_file:
        functions.input_file(file_extension_str)
        mock_input_file.assert_called_once_with(id=expected_id,
                                                label="",
                                                accept=expected_accept,
                                                multiple=False)

# Test get_file_id()
def test_get_file_id():
    """ Test the `get_file_id()` function. This function generates a `file_id` based on the file format selected by the user. For example, if the user selects ".csv", the returned `file_id` will be "csv_file". Similarly, if ".xlsx" is selected, the returned `file_id` will be "xlsx_file".
    """
    assert functions.get_file_id(".csv") == "csv_file"
    assert functions.get_file_id(".tsv") == "tsv_file"
    assert functions.get_file_id(".xlsx") == "xlsx_file"

# Test read_csv_file() -> valid & invalid
@pytest.fixture
def mock_ui_modal():
    """ Fixture for the `ui.modal` function.

    :yield: A mock object representing the `ui.modal` function.
    :rtype: MagicMock
    """
    with patch("VizAble.functions.ui.modal") as mock_modal:
        yield mock_modal

@pytest.fixture
def mock_ui_modal_show():
    """ Fixture for the `ui.modal_show` function.

    :yield: A mock object representing the `ui.modal_show` function.
    :rtype: MagicMock
    """
    with patch("VizAble.functions.ui.modal_show") as mock_modal_show:
        yield mock_modal_show

def test_read_csv_file_valid(mock_ui_modal, mock_ui_modal_show):
    """ Test the `read_csv_file()` function with an incorrect format csv file. This test should return a DataFrame and not show a modal.

    :param mock_ui_modal: Mock object for `ui.modal` function.
    :type mock_ui_modal: MagicMock
    """
    test_file_path = "tests/test_dataframe/without_parser_error.csv"
    test_sep = ","
    test_quotechar = "'"
    expected_df = pd.DataFrame({"Index":[1, 2, 3, 4],
                                "Customer Id":["DD37Cf93aecA6Dc", "1Ef7b82A4CAAD10", "6F94879bDAfE5a6", "5Cef8BFA16c5e3c"],
                                "First Name":["Sheryl", "Preston", "Roy", "Linda"],
                                "Last Name":["Baxter", "Lozano", "Berry", "Olsen"],
                                "Company":["Rasmussen Group", "Vega-Gentry", "Murillo-Perry", "Dominguez  Mcmillan and Donovan"]}).reset_index().fillna("N/A")
    
    output_df = functions.read_csv_file(test_file_path, test_sep, test_quotechar)
    assert output_df.equals(expected_df)
    mock_ui_modal.assert_not_called()
    mock_ui_modal_show.assert_not_called()

def test_read_csv_file_invalid(mock_ui_modal, mock_ui_modal_show):
    """ test the `read_csv_file()` function with incorrect format csv file. This test should return an empty DataFrame and shows a modal with an error message.

    :param mock_ui_modal: Mock object for `ui.modal` function.
    :type mock_ui_modal: MagicMock
    :param mock_ui_modal_show: Mock object for `ui.modal_show` function.
    :type mock_ui_modal_show: MagicMock
    """
    test_file_path = "tests/test_dataframe/with_parser_error.csv"
    test_sep = ","
    test_quotechar = "'"
    test_error_message = f"An error occurred while processing the file. Please ensure that the file format is correct and try again. Error: Error tokenizing data. C error: Expected 5 fields in line 5, saw 6\n.\n Press Escape key or Dismiss button to close this message."
    expected_df = pd.DataFrame()

    output_df = functions.read_csv_file(test_file_path, test_sep, test_quotechar)
    assert output_df.equals(expected_df)
    mock_ui_modal.assert_called_once_with(test_error_message, easy_close=True)
    mock_ui_modal_show.assert_called_once()

# Test get_excel_sheet_names() -> valid & invalid
def test_get_excel_sheet_names():
    """ Test the `get_excel_sheet_names()` function. This function returns the names of the sheets in an Excel file.
    """
    assert functions.get_excel_sheet_names("tests/test_dataframe/xlsx_example_file.xlsx") == ["Sheet1", "Sheet2", "Sheet3"]

def test_get_excel_sheet_names_invalid():
    """ Test the `get_excel_sheet_names()` function. This function returns an empty list if the file path is invalid or there is an error reading the file.
    """
    assert functions.get_excel_sheet_names("tests/test_dataframe/invalid_file.xlsx") == []

# Test return_choices_for_columns()
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

# Test xaxis_input_select()
@pytest.mark.parametrize("plot_type_str, expected_id",
                         [
                             ("line", "line_x_axis"),
                             ("bar", "bar_x_axis"),
                             ("box", "box_x_axis"),
                             ("histogram", "histogram_x_axis"),
                             ("scatter", "scatter_x_axis")
                         ])

def test_xaxis_input_select(plot_type_str: str, expected_id: str):
    """ Test the `xaxis_input_select()` function. This function returns an empty dropdown for users to select the `x-axis`, where the input id is based on the provided `plot_type_str`.

    :param plot_type_str: Plot type string, e.g., "line", "bar", "box", "histogram", "scatter".
    :type plot_type_str: str
    :param expected_id: the expected id for the initial input select
    :type expected_id: str
    """
    with patch("VizAble.functions.ui.input_select") as mock_input_select:
        functions.xaxis_input_select(plot_type_str)
        mock_input_select.assert_called_once_with(id=expected_id,
                                                  label=ui.strong("X-axis"),
                                                  choices=[],
                                                  selected=None,
                                                  multiple=False)

# Test yaxis_input_select()
@pytest.mark.parametrize("plot_type_str, expected_id",
                         [
                             ("line", "line_y_axis"),
                             ("bar", "bar_y_axis"),
                             ("box", "box_y_axis"),
                             ("histogram", "histogram_y_axis"),
                             ("scatter", "scatter_y_axis")
                         ])

def test_yaxis_input_select(plot_type_str: str, expected_id: str):
    """ Test the `yaxis_input_select()` function. This function returns an empty dropdown for users to select the `y-axis`, where the input id is based on the provided `plot_type_str`.
    :param plot_type_str: Plot type string, e.g., "line", "bar", "box", "histogram", "scatter".
    :type plot_type_str: str
    :param expected_id: the expected id for the initial input select
    :type expected_id: str
    """
    with patch("VizAble.functions.ui.input_select") as mock_input_select:
        functions.yaxis_input_select(plot_type_str)
        mock_input_select.assert_called_once_with(id=expected_id,
                                                  label=ui.strong("Y-axis"),
                                                  choices=[],
                                                  selected=None,
                                                  multiple=False)

# Test update_xaxis_input_select()
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

    with patch("VizAble.functions.ui.update_select") as mock_update_select:
        functions.update_xaxis_input_select(plot_type, choices)
        mock_update_select.assert_called_once_with(id=expected_id, choices=choices, selected=None)

# Test update_yaxis_input_select()
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

    with patch("VizAble.functions.ui.update_select") as mock_update_select:
        functions.update_yaxis_input_select(plot_type, choices)
        mock_update_select.assert_called_once_with(id=expected_id, choices=choices, selected=None)