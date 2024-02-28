from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module

def generate_plots_ui() -> ui.nav_panel:
    """ user interface for generating plots(step 5)

    :return: a nav_panel including all the ui components for generating plots
    :rtype: ui.nav_panel
    """
    return ui.nav_panel(
        "Step 5",
        ui.tags.header(
            ui.panel_title(ui.tags.h1("Generate Plots")),
        ),
        ui.tags.br(),
        ui.card(
            height="80vh",
        ),
    )