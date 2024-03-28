from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module
from shinywidgets import output_widget, render_widget 

def generate_plots_ui() -> ui.nav_panel:
    """ user interface for generating plots(step 5)

    :return: a nav_panel including all the ui components for generating plots
    :rtype: ui.nav_panel
    """
    return ui.nav_panel(
        "Step 5",
        ui.tags.header(ui.tags.h1("Generate Plots"),
        ),
        ui.tags.br(),
        ui.card(
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_text(
                        id="plot_title",
                        label="Plot Title",
                        placeholder="Enter a plot title"
                    ),
                    ui.input_checkbox(
                        id="markers",
                        label="Show markers or not",
                    ),
                    # ui.input_select(
                    #     id="color_by",
                    #     label="Color by",
                    #     choices=["--------"]
                    # ),
                    ui.tooltip(
                        ui.input_action_button(
                        id = "generate",
                        label = "Generate Plot"
                        ),
                        "You can generate a plot by clicking this \"Generate Plot\" button, but if you have modify anything related to this plot, you need to click this button again to update the plot.",
                    ),
                ),
                output_widget("get_output_plot"),
            ),
            height="80vh",
        ),
    )