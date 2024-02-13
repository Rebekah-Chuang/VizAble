from typing import List
from pathlib import Path
from shiny import ui, render, App, Inputs, Outputs, Session, reactive
import openpyxl

def sep_input_radio_buttons() -> ui.input_radio_buttons:
    """ Create a radio button group for users to select a separator for input.

    Returns:
        ui.input_radio_buttons: A radio button group for selecting a separator.
            Users can choose from Comma (`,`), Semicolon (`;`), and Tab (`\t`).
    """
    return ui.input_radio_buttons(
        id = "sep",
        label = ui.strong("Separator"),
        choices = ["Comma( , )", "Semicolon( ; )", "Tab( \\t )"],
        selected = None
    )

def quotechar_input_radio_buttons() -> ui.input_radio_buttons:
    """ Create a radio button group for users to select a quote character for input.

    Returns:
        ui.input_radio_buttons: A radio button group for selecting a quote character.
            Users can choose from Double Quote (`"`) and Single Quote (`'`).
    """
    return ui.input_radio_buttons(
        id = "quotechar",
        label = ui.strong("Quote Character"),
        choices= ["Double Quote( \" )", "Single Quote( \' )"],
        selected = None
    )

def input_file(file_extension_str: str) -> ui.input_file:
    """ Create a file input for users to upload a file.

    Args:
        file_extension_str (str): File extension string, e.g., ".csv", ".tsv", ".xlsx".

    Returns:
        ui.input_file: File input for users to upload a file, with the input id based on the provided `file_extension_str`.
    """
    file_suffix = file_extension_str.replace(".", "")

    return ui.input_file(
        id = f"{file_suffix}_file",
        label = "",
        accept = [file_extension_str],
        multiple = False
    )

def get_file_id(input_file_format_str: str) -> str:
    """ Generate a `file_id` based on the file format selected by the user.

    Args:
        input_file_format_str (str): File format string, e.g., ".csv", ".tsv", ".xlsx".

    Returns:
        str: The `file_id` based on the provided file format string.
    """
    file_suffix = input_file_format_str.replace(".", "")
    file_id = f"{file_suffix}_file"
    return file_id

def xaxis_input_select(plot_type_str: str) -> ui.input_select:
    """ Create a dropdown for users to select the x-axis.

    Args:
        plot_type_str (str): Plot type string, e.g., "line", "bar", "box", "histogram", "scatter".

    Returns:
        ui.input_select: An empty dropdown for users to select the `x-axis`, where the input id is based on the provided `plot_type_str`.
    """
    x_axis_id = f"{plot_type_str}_x_axis"
    return ui.input_select(
        id = x_axis_id,
        label = ui.strong("X-axis"),
        choices = [],
        selected = None,
        multiple = False
    )

def yaxis_input_select(plot_type_str: str) -> ui.input_select:
    """ Create a dropdown for users to select the y-axis.

    Args:
        plot_type_str (str): Plot type string, e.g., "line", "bar", "box", "histogram", "scatter".

    Returns:
        ui.input_select: An empty dropdown for users to select the `y-axis`, where the input id is based on the provided `plot_type_str`.
    """
    y_axis_id = f"{plot_type_str}_y_axis"
    return ui.input_select(
        id = y_axis_id,
        label = ui.strong("Y-axis"),
        choices = [],
        selected = None,
        multiple = False
    )

def get_excel_sheet_names(file_path: Path) -> List[str]:
    """ Get a list of all sheet names for the uploaded Excel file.

    Args:
        file_path (Path): Path to the uploaded Excel file.

    Returns:
        List[str]: A list of all sheet names for the uploaded Excel file. 
            Returns an empty list if the file path is invalid or there is an error reading the file.
    """
    try:
        workbook = openpyxl.load_workbook(file_path, read_only=True)
        sheet_names = workbook.sheetnames
        return sheet_names
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []