from shiny import ui, render, App, Inputs, Outputs, Session, reactive

def sep_input_radio_buttons():
    return ui.input_radio_buttons(id = "sep",
                                   label = ui.strong("Separator"),
                                   choices = ["Comma( , )", "Semicolon( ; )", "Tab( \\t )"],
                                   selected = None)

def quotechar_input_radio_buttons():
    return ui.input_radio_buttons(id = "quotechar",
                                   label = ui.strong("Quote Character"),
                                   choices= ["Double Quote( \" )", "Single Quote( \' )"],
                                   selected = None)

def input_file(file_extension_str):
    file_suffix = file_extension_str.replace(".", "")

    return ui.input_file(id = f"{file_suffix}_file",
                         label = "",
                         accept = [file_extension_str],
                         multiple = False)

def get_file_id(input_file_format_str):
    file_suffix = input_file_format_str.replace(".", "")
    file_id = f"{file_suffix}_file"
    return file_id