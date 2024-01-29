from shiny import ui, render, App, Inputs, Outputs, Session, reactive

def sep_input_radio_buttons():
    """
    Create a radio button for user to select separator as input
    """
    return ui.input_radio_buttons(id = "sep",
                                   label = ui.strong("Separator"),
                                   choices = ["Comma( , )", "Semicolon( ; )", "Tab( \\t )"],
                                   selected = None)

def quotechar_input_radio_buttons():
    """
    Create a radio button for user to select quote character as input
    """
    return ui.input_radio_buttons(id = "quotechar",
                                   label = ui.strong("Quote Character"),
                                   choices= ["Double Quote( \" )", "Single Quote( \' )"],
                                   selected = None)

def input_file(file_extension_str):
    """
    Create a file input for user to upload file
    """
    file_suffix = file_extension_str.replace(".", "")

    return ui.input_file(id = f"{file_suffix}_file",
                         label = "",
                         accept = [file_extension_str],
                         multiple = False)

def get_file_id(input_file_format_str):
    """
    Generate `file_id` based on file format user selected
    """
    file_suffix = input_file_format_str.replace(".", "")
    file_id = f"{file_suffix}_file"
    return file_id

def xaxis_input_selectize(plot_type_str):
    """
    Create a dropdown for user to select x-axis
    """
    x_axis_id = f"{plot_type_str}_x_axis"
    return ui.input_selectize(id = x_axis_id,
                              label = ui.strong("X-axis"),
                              choices = [],
                              selected = None,
                              multiple = False)

def yaxis_input_selectize(plot_type_str):
    """
    Create a dropdown for user to select y-axis
    """
    y_axis_id = f"{plot_type_str}_y_axis"
    return ui.input_selectize(id = y_axis_id,
                              label = ui.strong("Y-axis"),
                              choices = [],
                              selected = None,
                              multiple = False)