from shiny import ui, render, App, Inputs, Outputs, Session, reactive
from shiny.types import FileInfo
from htmltools import css
import shinyswatch
import pandas as pd
import openpyxl, xlrd
import functions


app_ui = ui.page_navbar(
    # theme for the app
    shinyswatch.theme.superhero(),
    ui.nav(
        "Instructions",
        ui.markdown(
            """
            This is an app for **Accessible Data Visualization**.

            Instructions to be added...
            """
        )
    ),

    # Step1: Upload a File
    ui.nav_panel(
        "Step 1",
        ui.panel_title(ui.tags.h2("Upload a File")),
                    # window_title= "Accessible Data Visualization"),
        ui.tags.br(),

        ui.card(
        ui.layout_sidebar(
            
            ui.sidebar(
                ui.input_selectize(id = "file_format",
                                label = ui.strong("File Format"),
                                choices = [".csv", ".tsv", ".xlsx"],
                                width = "100%"),

                # Add condition: if user selects ".csv" on file_format, they need to select separator/quote character
                # and only allowed to upload .csv file 
                ui.panel_conditional("input.file_format == '.csv'",
                                    functions.sep_input_radio_buttons(),
                                    ui.tags.hr(),
                                    functions.quotechar_input_radio_buttons(),
                                    ui.tags.hr(),
                                    functions.input_file(".csv")
                ),

                # Add condition: if user selects ".tsv" on file_format, they need to select quote character
                # and only allowed to upload .tsv file 
                ui.panel_conditional("input.file_format == '.tsv'",
                                    ui.tags.hr(),
                                    functions.input_file(".tsv")
                ),

                # Add condition: if user selects ".xlsx" on file_format, they are only allowed to upload .xlsx file 
                ui.panel_conditional("input.file_format == '.xlsx'",
                                    ui.input_text(id = "sheet_name",
                                                  label = ui.strong("Sheet Name"),
                                                  placeholder = "Type in sheet name...",),
                                    ui.tags.hr(),
                                    functions.input_file(".xlsx")
                ),  
            ),            

            ui.output_data_frame("output_dataframe"),

            open = "always",  
        ),

        height = "80vh",
        )    
    ),

    # Step2: Select Plot Types
    ui.nav_panel(
        "Step 2",
        ui.panel_title(ui.tags.h2("Select Plot Types")),

        ui.tags.br(),

        ui.card(
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_selectize(id = "plot_types",
                                       label = ui.strong("Plot Types"),
                                       choices = ["Line Plot", "Bar Plot", "Box Plot", "Histogram", "Scatter Plot"],
                                       selected = None,
                                       multiple = False
                    ),
                ),
            ),
        
        height = "80vh",
        )
    ),
    # Step3: Select Columns
    ui.nav_panel(
        "Step 3",
        ui.panel_title(ui.tags.h2("Select Columns")),
    ),

    # Step4: Generate Plots
    ui.nav_panel(
        "Step 4",
        ui.panel_title(ui.tags.h2("Generate Plots")),
    ),
    title="Accessible Data Visualization",
)


def server(input: Inputs, output: Outputs, session: Session):
    
    @output
    @render.data_frame

    def output_dataframe():
        # Seperator
        if input.sep() == "Comma( , )":
            sep = ","
        elif input.sep() == "Semicolon( ; )":
            sep = ";"
        else:
            sep = "\t"

        # Quote Character
        if input.quotechar() == "Double Quote( \" )":
            quotechar = "\""
        else:
            quotechar = "\'"

        # Get file id
        file_id = functions.get_file_id(input.file_format())
        file_input = getattr(input, file_id)

        file: list[FileInfo] | None = file_input()
        if file is None:
            return render.DataGrid(pd.DataFrame())
        
        if file_id == "csv_file":
            data_frame = pd.read_csv(file[0]["datapath"],
                                        sep = sep,
                                        quotechar = quotechar,
                                        header = 0)\
                                    .reset_index()\
                                    .fillna("N/A")
            
        elif file_id == "tsv_file":
            data_frame = pd.read_table(file[0]["datapath"],
                                        sep = "\t",
                                        quotechar = quotechar,
                                        header = 0)\
                                    .reset_index()\
                                    .fillna("N/A")
            
        else:
            data_frame = pd.read_excel(file[0]["datapath"],
                                    sheet_name = input.sheet_name(),
                                    header = 0,
                                    engine = 'openpyxl')\
                                    .reset_index()\
                                    .fillna("N/A")
            
        return render.DataGrid(data_frame,
                                filters = True)

app = App(app_ui, server)
