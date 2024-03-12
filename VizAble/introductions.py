from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module

def introductions_ui() -> ui.nav_panel:
    """ user interface for introducing the app

    :return: a nav_panel including all the ui components for introductions
    :rtype: ui.nav_panel
    """
    return ui.nav_panel(
        "Instructions",
        ui.tags.header(ui.tags.h1("Instructions")),
        ui.tags.main(
            ui.markdown(
                """
            This is an web app for **Accessible Data Visualization**.
        
            Instructions to be added...
            """
            ),
        ),
    ),