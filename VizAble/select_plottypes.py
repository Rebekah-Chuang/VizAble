from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module

def select_plottypes_ui() -> ui.nav_panel:
    """ user interface for selecting plot types(step 3)

    :return: a nav_panel including all the ui components for selecting plot types
    :rtype: ui.nav_panel
    """
    return ui.nav_panel(
        "Step 3",
        ui.tags.header(ui.tags.h1("Select Plot Types"),
        ),
        ui.tags.br(),
        ui.card(
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_select(
                        id="plot_types",
                        label=ui.strong("Plot Types"),
                        choices=[],
                        selected=None,
                        multiple=False,
                    )
                ),
                ui.tags.main(
                    ui.output_ui("get_plot_introductions"),
                ),
                
                open="always",
            ),
            height="80vh",
        ),
    )