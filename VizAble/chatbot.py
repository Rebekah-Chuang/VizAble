from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module
from shinywidgets import output_widget, render_widget 

def chatbot_ui() -> ui.nav_panel:
    """ user interface for chatbot(step 6)

    :return: a nav_panel including all the ui components for chatbot 
    :rtype: ui.nav_panel
    """

    return ui.nav_panel(
            "Step 6",
            ui.tags.header(ui.tags.h1("Chatbot"),
            ),
            ui.tags.br(),
            ui.card(
                ui.layout_sidebar(
                    ui.sidebar(
                        ui.input_text_area(
                            id="chatbot_input",
                            label="Type your question here:",
                            placeholder="Enter your message here",
                            rows=3,
                            width="100%",
                        ),
                        ui.input_action_button(
                            id="ask",
                            label="Ask",
                            class_="btn-primary",
                            width="100%",
                        ),
                    ),
                ui.output_text_verbatim("get_chatbot_output"),
                ),
                height="80vh",
            ),
        )