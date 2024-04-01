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
                    # Show when user selects "Line Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Line Plot'",
                        ui.input_text(
                            id="line_plot_title",
                            label="Plot Title",
                            placeholder="Enter a plot title"
                        ),
                        ui.input_text(
                            id="line_x_axis_title",
                            label="X-axis Title",
                            placeholder="Enter a title for the x-axis"
                        ),
                        ui.input_text(
                            id="line_y_axis_title",
                            label="Y-axis Title",
                            placeholder="Enter a title for the y-axis"
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
                    ),

                    # Show when user selects "Box Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Box Plot'",
                        ui.input_text(
                            id="box_plot_title",
                            label="Plot Title",
                            placeholder="Enter a plot title"
                        ),
                        ui.input_text(
                            id="box_y_axis_title",
                            label="Y-axis Title",
                            placeholder="Enter a title for the y-axis"
                        ),
                    ),

                    # Show when user selects "Bar Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Bar Plot'",
                        ui.input_text(
                            id="bar_plot_title",
                            label="Plot Title",
                            placeholder="Enter a plot title"
                        ),
                        ui.input_text(
                            id="bar_x_axis_title",
                            label="X-axis Title",
                            placeholder="Enter a title for the x-axis"
                        ),
                        ui.input_text(
                            id="bar_y_axis_title",
                            label="Y-axis Title",
                            placeholder="Enter a title for the y-axis"
                        ),
                    ),

                    # Show when user selects "Histogram" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Histogram'",
                        ui.input_text(
                            id="histogram_plot_title",
                            label="Plot Title",
                            placeholder="Enter a plot title"
                        ),
                        ui.input_text(
                            id="histogram_x_axis_title",
                            label="X-axis Title",
                            placeholder="Enter a title for the x-axis"
                        ),
                        ui.input_text(
                            id="histogram_y_axis_title",
                            label="Y-axis Title",
                            placeholder="Enter a title for the y-axis"
                        ),
                        ui.input_numeric(
                            id="histogram_bin_size",
                            label="Bin Size",
                            value=10,
                        ),
                    ),

                    # Show when user selects "Scatter Plot" on plot_types
                    ui.panel_conditional(
                        "input.plot_types == 'Scatter Plot'",
                        ui.input_text(
                            id="scatter_plot_title",
                            label="Plot Title",
                            placeholder="Enter a plot title"
                        ),
                        ui.input_text(
                            id="scatter_x_axis_title",
                            label="X-axis Title",
                            placeholder="Enter a title for the x-axis"
                        ),
                        ui.input_text(
                            id="scatter_y_axis_title",
                            label="Y-axis Title",
                            placeholder="Enter a title for the y-axis"
                        ),
                    ),
                    
                    # Show the "Generate Plot" button no matter what plot type is selected
                    ui.tooltip(
                        ui.input_action_button(
                            id = "generate",
                            label = "Generate Plot",
                        ),
                        "You can generate a plot by clicking this \"Generate Plot\" button, but if you have modify anything related to this plot, you need to click this button again to update the plot.",
                    ), 
                ),
                output_widget("get_output_plot"),
                height="80vh",
            ),
        ),
    )