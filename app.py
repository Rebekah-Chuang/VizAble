from shiny import ui, render, App, Inputs, Outputs, Session, reactive
from shiny.types import FileInfo
from htmltools import css
# import htmltools
import shinyswatch
import pandas as pd
import great_tables as gt
import great_tables.shiny as gts
import openpyxl, xlrd
import functions


app_ui = ui.page_fixed(
    # theme for the app
    shinyswatch.theme.superhero(),
    ui.tags.br(),
    ui.tags.br(),
    ui.panel_title(ui.tags.h1("Upload a File"),
                   window_title= "Accessible Data Visualization"),

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

    height = "70vh",
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    
    @output
    @render.data_frame

    def output_dataframe():
        # Seperator
        seperator = str(input.sep())
        if seperator == "Comma( , )":
            sep = ","
        elif seperator == "Semicolon( ; )":
            sep = ";"
        else:
            sep = "\t"

        # Quote Character
        qc = str(input.quotechar())
        if qc == "Double Quote( \" )":
            quotechar = "\""
        else:
            quotechar = "\'"


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
