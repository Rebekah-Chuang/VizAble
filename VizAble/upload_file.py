from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module
from VizAble import functions

def upload_ui() -> ui.nav_panel:
    """ user interface for uploading a file(step 1)

    :return: a nav_panel including all the ui components for uploading a file
    :rtype: ui.nav_panel
    """
    return ui.nav_panel(
        "Step 1",
        ui.tags.header(
            ui.panel_title(ui.tags.h1("Upload a File")),
        ),
        ui.tags.br(),
        ui.card(
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_select(
                        id="file_format",
                        label=ui.strong("File Format"),
                        choices=["Select an option", ".csv", ".tsv", ".xlsx"],
                        width="100%",
                        selected=["Select an option"],
                    ),
                    # Add condition: if user selects ".csv" on file_format, they need to select separator/quote character
                    # and only allowed to upload .csv file
                    ui.panel_conditional(
                        "input.file_format == '.csv'",
                        functions.sep_input_radio_buttons(),
                        ui.tags.hr(),
                        functions.quotechar_input_radio_buttons(),
                        ui.tags.hr(),
                        functions.input_file(".csv"),
                    ),
                    # Add condition: if user selects ".tsv" on file_format, they need to select quote character
                    # and only allowed to upload .tsv file
                    ui.panel_conditional(
                        "input.file_format == '.tsv'",
                        ui.tags.hr(),
                        functions.input_file(".tsv"),
                    ),
                    # Add condition: if user selects ".xlsx" on file_format, they are only allowed to upload .xlsx file
                    ui.panel_conditional(
                        "input.file_format == '.xlsx'",
                        functions.input_file(".xlsx"),
                        ui.tags.hr(),
                        ui.input_select(
                            id="sheet_name",
                            label=ui.strong("Sheet Name"),
                            choices=["Select an option"],
                            selected=None,
                            multiple=False,
                        ),
                    ),
                    ui.tooltip(
                        ui.input_action_button(
                            id="reset",
                            label="Reset",
                            class_="btn-danger",
                        ),
                        "You can reset all selections and uploaded file by clicking this \"Reset\" button.",
                    ),
                ),
                ui.tags.main(
                    ui.output_data_frame("get_output_df"),
                ),
                open="always",
            ),
            height="80vh",
        ),
    )