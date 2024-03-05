from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module

def check_datatypes_ui() -> ui.nav_panel:
    """ user interface for checking/converting datatypes for columns(step 2)

    :return: a nav_panel including all the ui components for checking/converting datatypes for columns
    :rtype: ui.nav_panel
    """
    return ui.nav_panel(
        "Step 2",
        ui.tags.header(ui.tags.h1("Check datatypes for columns"),
        ),
        ui.tags.br(),
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select(
                    id="column_to_convert",
                    label=ui.strong("Column"),
                    choices=[],
                    selected=None,
                    multiple=False,
                ),
                ui.input_select(
                    id="convert_dtype",
                    label=ui.strong("Convert to"),
                    choices=[],
                    selected=None,
                    multiple=False,
                ),
                ui.tooltip(
                    ui.input_action_button(
                        id="convert",
                        label="Convert",
                        class_="btn-success"
                    ),
                    "You can convert the selected column to the selected data type by clicking this \"Convert\" button.",
                ),
            ),
            ui.tags.main(
                ui.layout_columns(
                    ui.div(
                        ui.tags.h5("Original Datatypes"),
                        ui.tags.hr(),
                        ui.output_data_frame("get_output_dtypes_df"),
                    ),
                    ui.div(
                        ui.tags.h5("Updated Datatypes"),
                        ui.tags.hr(),
                        ui.output_data_frame("get_updated_output_dtypes_df"),
                    ),
                    col_widths={"sm": (5, 5)},
                ),
            ),
            height="80vh",
        ),
    )