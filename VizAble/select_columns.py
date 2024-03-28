from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module
from VizAble import functions

def select_columns_ui() -> ui.nav_panel:
    """ user interface for selecting columns(step 4)

    :return: a nav_panel including all the ui components for selecting columns
    :rtype: ui.nav_panel
    """
    return ui.nav_panel(
        "Step 4",
        ui.tags.header(ui.tags.h1("Select Columns"),
        ),
        ui.tags.br(),
        ui.card(
            ui.layout_sidebar(
                ui.sidebar(
                    # Add condition: if user selects "Line Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Line Plot'",
                        # add dropdown for x-axis and y-axis
                        functions.xaxis_input_select("line"),
                        functions.yaxis_input_select("line"),
                    ),
                    # Add condition: if user selects "Bar Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Bar Plot'",
                        # add dropdown for x-axis
                        functions.xaxis_input_select("bar"),
                    ),
                    # Add condition: if user selects "Box Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Box Plot'",
                        # add dropdown for x-axis
                        functions.xaxis_input_select("box"),
                    ),
                    # Add condition: if user selects "Histogram" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Histogram'",
                        # add dropdown for x-axis
                        functions.xaxis_input_select("histogram"),
                    ),
                    # Add condition: if user selects "Scatter Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Scatter Plot'",
                        # add dropdown for x-axis and y-axis
                        functions.xaxis_input_select("scatter"),
                        functions.yaxis_input_select("scatter"),
                    ),
                    open="always",
                ),
                ui.tags.main(
                    ui.output_data_frame("get_output_selected_cols"),
                ),
                height="80vh",
            ),
        ),
    )